import json

html_text = """"""

gold_text = """"""
data = [
    {
        "url": "https://it.wikipedia.org/wiki/Guerra_di_Corea",
        "domain": "it.wikipedia.org",
        "title": "Guerra di Corea",
        "html_text": html_text,
        "gold_text": gold_text
    }
]

with open("make_wikipedia_gs.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("File JSON creato correttamente!")