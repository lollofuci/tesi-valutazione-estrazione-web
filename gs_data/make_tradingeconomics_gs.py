import json

html_text = """"""

gold_text = """"""
data = [
    {
        "url": "https://tradingeconomics.com/germany/gdp",
        "domain": "tradingeconomics.com",
        "title": "Germany GDP",
        "html_text": html_text,
        "gold_text": gold_text
    }
]

with open("make_tradingeconomics_gs.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("File JSON creato correttamente!")