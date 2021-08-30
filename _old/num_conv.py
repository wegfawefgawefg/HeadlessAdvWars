from pprint import pprint
import json
with open("damage_chart.json", "r") as f:
    dmg_chart = json.load(f)

new_dmg_chart = {}
for attacker, defenders in dmg_chart.items():
    new_dmg_chart[attacker] = {}
    for defender_name, val in defenders.items():
        new_dmg_chart[attacker][defender_name] = int(val)

with open("damage_chart2.json", "w") as f:
    dmg_chart = json.dump(new_dmg_chart, f)