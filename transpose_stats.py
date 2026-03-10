"""Transpose armor, toughness, hull, shields from ships_canon.json to ships.json"""
import json

with open("ships_canon.json") as f:
    canon = json.load(f)

with open("ships.json") as f:
    ships = json.load(f)

canon_by_id = {s["id"]: s for s in canon["ships"]}

for ship in ships["ships"]:
    sid = ship["id"]
    if sid in canon_by_id:
        c = canon_by_id[sid]
        ship["armor"] = c["armor"]
        ship["toughness"] = c["toughness"]
        ship["hull"] = c["hull"]
        ship["shields"] = c["shields"]

with open("ships.json", "w") as f:
    json.dump(ships, f, indent=2)

print("Done. Transposed armor, toughness, hull, shields to ships.json")
