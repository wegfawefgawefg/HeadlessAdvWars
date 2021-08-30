import os
import csv

with open("damage_chart_raw.csv", "r") as f:
    r = csv.reader(f, csv.QUOTE_NONNUMERIC)
    vals = []
    for row in r:
        vals.append([v for v in row])
    vals = list(zip(*vals))

units = ["infantry", "mech", "recon", "tank", "mdtank", "neotank", "megatank", "artillery", "rocket", "antiair", "missile", "piperunner",
    "bcopter", "fighter", "bomber", "stealth", "cruiser", "sub", "battleship", "carrier"]
dunits = ["infantry", "mech", "recon", "tank", "mdtank", "neotank", "megatank", "apc","artillery", "rocket", "antiair", "missile", "piperunner",
    "blob", "bcopter", "tcopter", "fighter", "bomber", "stealth", "black_bomb", "lander", "cruiser", "sub", "battleship", "carrier", "black_boat", "pipe"]

unit_dmgs = {}
for unit, dmgs in zip(units, vals):
    unit_dmgs[unit] = {e:v for e,v in zip(dunits, dmgs)}
from pprint import pprint
pprint(unit_dmgs)

import json
with open("damage_chart.json", "w") as f:
    json.dump(unit_dmgs, f)
