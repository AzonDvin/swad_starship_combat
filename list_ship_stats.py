import json
with open("ships_canon.json") as f:
    data = json.load(f)
print(f"{'Ship':<40} {'Armor':>6} {'Toughness':>10} {'Hull':>6}")
print("-" * 66)
for s in data["ships"]:
    print(f"{s['name']:<40} {s['armor']:>6} {s['toughness']:>10} {s['hull']:>6}")
