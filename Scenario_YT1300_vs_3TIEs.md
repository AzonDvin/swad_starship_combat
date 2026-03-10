# Scenario: Three TIE Fighters vs YT-1300 Freighter

## Setup

**Location:** Asteroid belt near Ord Mantell. A YT-1300 freighter evades Imperial patrol and is intercepted by three TIE fighters.

**Ships** (see ships.json: `millennium_falcon`, `tie_fighter`):

| Ship | Size | Handling | Top Speed | Toughness | Armor | Shields | Crew |
|------|------|----------|-----------|-----------|-------|---------|------|
| **YT-1300** | 8 | +1 | 650 | 20 (6) | 6 | 40 | Pilot, Co-pilot, Gunner, Engineer |
| **TIE Fighter 1** | 6 | +2 | 800 | 15 (5) | 5 | — | Pilot, Gunner |
| **TIE Fighter 2** | 6 | +2 | 800 | 15 (5) | 5 | — | Pilot, Gunner |
| **TIE Fighter 3** | 6 | +2 | 800 | 15 (5) | 5 | — | Pilot, Gunner |

**Key modifiers:**
- TIEs have speed advantage (+1 momentum vs YT-1300).
- YT-1300 has turret; TIEs have fixed forward cannons.
- YT-1300 has shields (40 max); regen 5% + 5%/raise. TIEs have none.
- **One weapon system = one target per round** (quad turret fires at one ship only).
- **Momentum** persists round to round. Lose all: Distraction, becoming Shaken. **Stay on Target** (opposed Piloting): target -2 momentum per success (cumulative; 2 successes = -4, 3 = -6); each side adds its momentum to its roll.
- **Joker:** Acts first, Pilot auto-passes initiative test, +2 to all crew rolls that round, short range.
- **Club drawn** = suit ♣; triggers Complications (Phase 7, roll 2d6 on table).
- **Raise:** To-hit roll ≥ 8 (TN+4) adds +1d6 to damage.
- **Crew skills:** YT-1300 Pilot, Co-pilot, Gunner, Engineer = d10 + wild d6 (aces/Wild Cards; take best). TIE Pilot/Gunner = d6.

---

## Round 1

### Initiative (start of round)
- YT-1300 shields: **40**.

### Initiative draw
- YT-1300: 8♥, 6♣ — **Club drawn**
- TIE 1: 4♣, 4♦ — **Club drawn**
- TIE 2: 10♦, 3♣ — **Club drawn**
- TIE 3: King♦, Queen♦

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling = 1. TN 4. Rolls 5 + 1 = 6 — success. Keeps 8.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 4.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 2 + 3 = 5 — success. Keeps 10.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 7 + 3 = 10 — success. Keeps 13.

**Order:** T3 (13) → T2 (10) → YT (8) → T1 (4)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 4 - 3 = 1 — fail. No effect.
- TIE 1: **I Can Hold It**
- TIE 2: **I Can Hold It**
- TIE 3: **Boost** (Pilot d6) — Piloting TN 4. Roll 2+3 = 5 — success. +2 momentum.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 6, T1 9, T2 10, T3 1; Damage [13, 16, 17, 15])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 = 1 — miss. Damage 2d10+2 = 15.
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 10 = 10 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 17. Strips 17 from shields. **YT-1300 shields: 23.**
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 6 - 2 (range) = 4 — **hit.** Damage 2d10+2 = 13. vs Toughness 15: no effect (glancing hit).
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 14 — raise. +4 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 7. Flight deck ionization (Pilot takes 2 Strain)
- **TIE 1** drew Club: 2d6 = 10. Complication (Pilot -2; fail = subsystem offline)
- **TIE 2** drew Club: 2d6 = 8. Flight deck ionization (Pilot takes 2 Strain)

---

## Round 2

### Initiative (start of round)
- YT-1300 shields: **27**.

### Initiative draw
- YT-1300: Jack♥, 7♣ — **Club drawn**
- TIE 1: 7♠, 7♦
- TIE 2: Ace♦, 10♥
- TIE 3: 9♣, 5♦ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling = 1. TN 4. Rolls 9 + 1 = 10 — success. Keeps 11.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 7.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 2 + 3 = 5 — success. Keeps 14.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 2 + 3 = 5 — success. Keeps 9.

**Order:** T2 (14) → YT (11) → T3 (9) → T1 (7)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 8 - 3 = 5 — success. -2 to opponents targeting this ship.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 3+3 = 6 — success. +2 momentum.
- TIE 2: **I Can Hold It**
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 7, T1 1, T2 5, T3 5; Damage [9, 19, 5, 11])*
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 5 - 2 (target Evading) = 3 — miss. Damage 2d10+2 = 5.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 7 - 2 (range) = 5 — **hit.** Damage 2d10+2 = 9. vs Toughness 15: no effect (glancing hit).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 5 — success. +2 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 8. Flight deck ionization (Pilot takes 2 Strain)
- **TIE 3** drew Club: 2d6 = 8. Flight deck ionization (Pilot takes 2 Strain)

---

## Round 3

### Initiative (start of round)
- YT-1300 shields: **29**.

### Initiative draw
- YT-1300: 6♣, 4♣ — **Club drawn**
- TIE 1: 6♥, 3♦
- TIE 2: 7♠, 3♦
- TIE 3: Jack♠, 6♦

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling = 1. TN 4. Rolls 4 + 1 = 5 — success. Keeps 6.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 2 + 3 = 5 — success. Keeps 6.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 7.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 10 + 3 = 13 — success. Keeps 11.

**Order:** T3 (11) → T2 (7) → YT (6) → T1 (6)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 5 - 3 = 2 — fail. No effect.
- TIE 1: **I Can Hold It**
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 5+3 vs YT: 5 — success. YT-1300 -2 momentum.
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 3+3 vs YT: 5 — success. YT-1300 -2 momentum.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 14, T1 5, T2 8, T3 4; Damage [17, 13, 21, 10])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 = 4 — **hit.** Damage 2d10+2 = 10. Strips 10 from shields. **YT-1300 shields: 19.**
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 8 = 8 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 21. Depletes shields (19). Overflow 2 vs Toughness 20: no hull effect. **Shields: 0.**
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 14 - 2 (range) = 12 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 17. vs Toughness 15: **Shaken.** Pilot must I Can Hold It next round.
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 9 — raise. +4 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 7. Flight deck ionization (Pilot takes 2 Strain)

---

## Round 4

### Initiative (start of round)
- YT-1300 shields: **4**.

### Initiative draw
- YT-1300: Queen♥, Jack♥
- TIE 1: Jack♠, 8♣ — **Club drawn**
- TIE 2: Joker, Queen♠ — **Joker**
- TIE 3: 9♥, 2♣ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling -4 Stay on Target = -3. TN 4. Rolls 9 + -3 = 6 — success. Keeps 12.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 10 + 3 = 13 — success. Keeps 11.
- **TIE 2** Joker — auto-passes (initiative test). Keeps Joker.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 11 + 3 = 14 — success. Keeps 9.

**Order:** T2 (15) → YT (12) → T1 (11) → T3 (9)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 5 - 3 = 2 — fail. No effect.
- TIE 1: **I Can Hold It**
- TIE 2: **Boost** (Pilot d6) — Piloting TN 4. Roll 5+3 = 8 — success. +2 momentum.
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 5, T1 9, T2 3, T3 3; Damage [10, 17, 15, 12])*
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 15.
- **YT-1300** vs TIE 1: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 5 - 2 (range) = 3 — miss. Damage 2d10+2 = 10.
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 5 — success. +2 shields.

### Complications (Phase 7)
- **TIE 1** drew Club: 2d6 = 7. Flight deck ionization (Pilot takes 2 Strain)
- **TIE 3** drew Club: 2d6 = 9. Complication (Pilot -2; fail = subsystem offline)

---

## Round 5

### Initiative (start of round)
- YT-1300 shields: **6**.

### Initiative draw
- YT-1300: Jack♥, 6♥
- TIE 1: Ace♠, 4♣ — **Club drawn**
- TIE 2: 9♥, 2♥
- TIE 3: 10♥, 9♦

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling = 1. TN 4. Rolls 14 + 1 = 15 — success. Keeps 11.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 3 + 3 = 6 — success. Keeps 14.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 9.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 1 + 3 = 4 — success. Keeps 10.

**Order:** T1 (14) → YT (11) → T3 (10) → T2 (9)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 5 - 3 = 2 — fail. No effect.
- TIE 1: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 1: 1+3 vs YT: 15 — fail. No effect.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 1+3 vs YT: 15 — fail. No effect.
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 10, T1 3, T2 4, T3 5; Damage [17, 25, 8, 16])*
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 25.
- **YT-1300** vs TIE 1: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 10 - 2 (range) = 8 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 17. vs Toughness 15: **Shaken.** Pilot must I Can Hold It next round.
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 3 — fail. +0 shields.

### Complications (Phase 7)
- **TIE 1** drew Club: 2d6 = 3. Distraction (ship loses all momentum)

---

## Summary

*(Scenario generated with pure random rolls. Run `python gen_scenario.py` to generate a new scenario with different rolls.)*
