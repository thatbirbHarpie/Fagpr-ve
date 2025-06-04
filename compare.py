from difflib import SequenceMatcher, HtmlDiff

import json
file_path = 'tekst.py'

with open(file_path, 'r', encoding='utf-8') as file:
    b = file.read()
parsed_json = json.loads(b)
a = """Hei, jeg heter Aksel og jeg er norsk."""

seq_match = SequenceMatcher(None, a, parsed_json['text'])
ratio = seq_match.ratio()
print(ratio)

d = HtmlDiff()
html_diff = d.make_file(a.splitlines(), b.splitlines()) # a,b were defined earlier
with open("diff.html", "w", encoding="utf-8") as f:
    f.write(html_diff)