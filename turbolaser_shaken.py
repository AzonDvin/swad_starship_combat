"""Compute P(Shaken) for a turbolaser (5d10+6) hit vs each ship in ships_canon.json.
   Assumes shields = 0 (all damage goes to hull)."""
import json
from collections import Counter

def get_damage_dist(n, d, mod):
    """Exact distribution of ndN+mod."""
    dist = Counter({0: 1})
    for _ in range(n):
        new_dist = Counter()
        for val, count in dist.items():
            for r in range(1, d + 1):
                new_dist[val + r] += count
        dist = new_dist
    return {v + mod: c for v, c in dist.items()}

def prob_exceeds(dist, threshold):
    """P(damage > threshold)."""
    total = sum(dist.values())
    exceeds = sum(c for v, c in dist.items() if v > threshold)
    return exceeds / total

# Turbolaser: 5d10+6 (Star Destroyer)
TURBOLASER = (5, 10, 6)
damage_dist = get_damage_dist(*TURBOLASER)

with open("ships_canon.json") as f:
    data = json.load(f)

print("Turbolaser: 5d10+6 (Star Destroyer)")
print("Shields = 0 (all damage to hull). Shaken when damage > Toughness.")
print()
print(f"{'Ship':<35} {'Tough':>6} {'P(Shaken)':>10}")
print("-" * 54)

for ship in data["ships"]:
    name = ship["name"]
    toughness = ship["toughness"]
    p = prob_exceeds(damage_dist, toughness)
    print(f"{name:<35} {toughness:>6} {p*100:>9.1f}%")
