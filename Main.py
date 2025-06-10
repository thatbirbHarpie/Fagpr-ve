from flask import Flask, render_template, redirect, url_for, request
import subprocess
import os
from flask import jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=['POST'] )
def process():
    uploaded_file = request.files['audio_file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)    
    subprocess.run(["python","transcriberApi.py", file_path])
    subprocess.run(["python","compare.py"])    
    return redirect(url_for("result"))

@app.route("/result")
def result():
    with open('diff.html', 'r') as f:
        diff_content = f.read()
    return render_template('result.html', diff=diff_content)

@app.route("/save", methods=['POST'])
def save():
    subprocess.run(["python","superbase.py"])
    return "<h2>Resultatet er lagret i databasen!</h2><a href='/'>Gå tilbake</a>"

@app.route("/results-list")
def results_list():
    from superbase import supabase  # gjenbruker klienten

    response = supabase.table("results").select("*").execute()
    rows = response.data

    return render_template("results_list.html", results=rows)


if __name__ == "__main__":
    app.run()