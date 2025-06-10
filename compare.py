from difflib import SequenceMatcher, HtmlDiff
import json

file_path = 'tekst.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    b = file.read()
a = """Hei, jeg hjelper deg med norsk uttale."""

seq_match = SequenceMatcher(None, a, b)
ratio = seq_match.ratio()
print(ratio)

d = HtmlDiff()
html_diff = d.make_file(a.splitlines(), b.splitlines())
with open("diff.html", "w", encoding="utf-8") as f:
    f.write(html_diff)

with open("result_data.json", "w", encoding="utf-8") as f:
    json.dump({
        "original": a,
        "transcribed": b,
        "score": ratio
    }, f, ensure_ascii=False)
