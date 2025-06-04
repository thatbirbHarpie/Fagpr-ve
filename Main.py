from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=['POST'] )
def process():
    subprocess.run(["python","transcriberApi.py"])
    subprocess.run(["python","compare.py"])    
    return redirect(url_for("result"))

@app.route("/result")
def result():
    with open('diff.html', 'r') as f:
        diff_content = f.read()
    return render_template('result.html', diff=diff_content)

if __name__ == "__main__":
    app.run()