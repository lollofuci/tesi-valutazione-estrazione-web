import json

html_text = """"""

gold_text = """WTI crude oil futures slipped to $94.8 per barrel on Friday, reversing earlier gains and snapping a four-session winning streak as hopes of diplomatic progress between the US and Iran improved sentiment. Reports indicated Iranian Foreign Minister Abbas Araghchi was expected to arrive in Islamabad, with sources suggesting a high likelihood of a breakthrough in negotiations involving mediators such as Pakistan. Despite the pullback, oil remains on track for a weekly gain of about 14%. Markets continue to be influenced by US policy signals, including President Donald Trump’s continuation of a naval blockade on Iranian ports, which has restricted crude exports from the Persian Gulf since the conflict began. The blockade remains a key obstacle in negotiations. A sanctioned tanker carrying Iranian oil was also seen attempting to leave the Strait of Hormuz, highlighting ongoing tensions in the vital shipping route that has seen sharply reduced flows since the war began.
Crude Oil	95.500		0.35	-0.37%	5.28%	50.89%	16:07
Brent	105.496		0.426	0.41%	2.78%	59.67%	16:07
Natural gas	2.5268		0.0872	-3.34%	-13.47%	-19.08%	16:07
Gasoline	3.4434		0.0187	-0.54%	13.95%	61.88%	16:07
Heating Oil	3.9842		0.004	-0.10%	-0.86%	83.26%	16:07
Coal	129.10		-3.70	-2.79%	-7.62%	36.25%	Apr/23
Ethanol	1.92		0	0%	-4.00%	6.82%	Apr/23
Urals Oil	107.49		3.41	3.28%	8.59%	77.73%	Apr/23
Crude Oil
Crude oil is one of the most widely followed commodities in the world due to its central role in the global economy. It is a key source of energy, a critical input for transportation and manufacturing, and a major driver of inflation and geopolitical dynamics. As a result, movements in oil prices are closely monitored by governments, businesses, and investors alike. West Texas Intermediate (WTI) crude oil is classified as light and sweet, where “light” refers to its low density and “sweet” indicates its low sulfur content. The delivery point for WTI crude oil futures is the Cushing Hub in Oklahoma, and each futures contract represents 1,000 barrels of crude oil. Crude oil prices displayed on Trading Economics are based on over-the-counter (OTC) and contract for difference (CFD) financial instruments and are intended to provide a general market reference only. These prices do not represent official WTI crude oil prices. Official pricing and settlement data for WTI crude oil futures should be obtained directly from NYMEX. The data is supplied by a third party and, while efforts are made to ensure its reliability, Trading Economics does not verify the data and makes no representations or warranties.
Actual	Previous	Highest	Lowest	Dates	Unit	Frequency	
95.22	95.85	410.45	-40.32	1983 - 2026	USD/BBL	Daily"""
data = [
    {
        "url": "https://tradingeconomics.com/commodity/crude-oil",
        "domain": "tradingeconomics.com",
        "title": "Crude Oil",
        "html_text": html_text,
        "gold_text": gold_text
    }
]

with open("make_tradingeconomics_gs.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("File JSON creato correttamente!")