"""Compute Shaken probabilities for Star Destroyer turbolasers."""
from collections import Counter

def prob_exceeds(n, d, mod, toughness):
    """P(ndN+mod > toughness) using exact distribution."""
    # Build distribution for ndN
    dist = Counter({0: 1})
    for _ in range(n):
        new_dist = Counter()
        for val, count in dist.items():
            for r in range(1, d + 1):
                new_dist[val + r] += count
        dist = new_dist
    total = sum(dist.values())
    exceeds = sum(c for v, c in dist.items() if v + mod > toughness)
    return exceeds / total

# Star Destroyer: 5d10+6, Toughness 75
print("=== Star Destroyer: Turbolasers 5d10+6, Toughness 75 ===\n")
print("Current 5d10+6 vs various targets (P(Shaken) = P(damage > Toughness)):")
targets = [("TIE Fighter", 14), ("X-wing", 16), ("YT-1300", 19), ("CR90", 39), 
           ("Nebulon-B", 48), ("Mon Cal", 60), ("Star Destroyer", 75)]
for name, t in targets:
    p = prob_exceeds(5, 10, 6, t)
    print(f"  vs {name} (T{t}): {p*100:.1f}%")

print("\n=== Damage formula for ~30% Shaken chance ===\n")
for target_name, target_t in targets:
    best = None
    for n in range(1, 20):
        for m in range(0, 40):
            p = prob_exceeds(n, 10, m, target_t)
            if 0.25 <= p <= 0.35:
                if best is None or abs(p - 0.30) < abs(best[2] - 0.30):
                    best = (n, m, p)
    if best:
        n, m, p = best
        print(f"  vs {target_name} (T{target_t}): {n}d10+{m} -> {p*100:.1f}%")
