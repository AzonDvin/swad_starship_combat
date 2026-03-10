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
- YT-1300: 10♥, 4♣ — **Club drawn**
- TIE 1: Ace♥, Queen♣ — **Club drawn**
- TIE 2: King♦, 5♣ — **Club drawn**
- TIE 3: Joker, Jack♥ — **Joker**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling = 1. TN 4. Rolls 9 + 1 = 10 — success. Keeps 10.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 7 + 3 = 10 — success. Keeps 14.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 1 + 3 = 4 — success. Keeps 13.
- **TIE 3** Joker — auto-passes (initiative test). Keeps Joker.

**Order:** T3 (15) → T1 (14) → T2 (13) → YT (10)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 3 - 3 = 0 — fail. No effect.
- TIE 1: **I Can Hold It**
- TIE 2: **I Can Hold It**
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 4, T1 3, T2 2, T3 3; Damage [15, 6, 4, 38])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 38.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 6.
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 2 = 2 — miss. Damage 2d10+2 = 4.
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 4 - 2 (range) = 2 — miss. Damage 2d10+2 = 15.

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 5 — success. +2 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 10. Complication (Pilot -2; fail = subsystem offline)
- **TIE 1** drew Club: 2d6 = 9. Complication (Pilot -2; fail = subsystem offline)
- **TIE 2** drew Club: 2d6 = 6. Flight deck ionization (10 stun damage to a random crew member)

---

## Round 2

### Initiative (start of round)
- YT-1300 shields: **40**.

### Initiative draw
- YT-1300: Ace♠, 10♦
- TIE 1: 10♥, 8♥
- TIE 2: 10♠, 4♦
- TIE 3: King♥, 6♦

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling = 1. TN 4. Rolls 6 + 1 = 7 — success. Keeps 14.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 10.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 10.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 3 + 3 = 6 — success. Keeps 13.

**Order:** YT (14) → T3 (13) → T1 (10) → T2 (10)

### Maneuver
- YT-1300: **Boost** (top initiative) — Piloting check (TN 4). Roll 4 + 1 = 5 — success. +2 momentum.
- TIE 1: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 1: 2+3 vs YT: 7 — fail. No effect.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 3+3 vs YT: 7 — fail. No effect.
- TIE 3: **Boost** (Pilot d6) — Piloting TN 4. Roll 2+3 = 5 — success. +2 momentum.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 15, T1 10, T2 1, T3 11; Damage [9, 16, 16, 16])*
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 15 - 2 (range) = 13 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 9. vs Toughness 15: no effect (glancing hit).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 4 — success. +2 shields.

---

## Round 3

### Initiative (start of round)
- YT-1300 shields: **40**.

### Initiative draw
- YT-1300: 10♣, 10♣ — **Club drawn**
- TIE 1: 10♥, 9♣ — **Club drawn**
- TIE 2: Joker, 3♦ — **Joker**
- TIE 3: 10♣, 8♦ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling +2 Boost = 3. TN 4. Rolls 16 + 3 = 19 — success. Keeps 10.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 2 + 3 = 5 — success. Keeps 10.
- **TIE 2** Joker — auto-passes (initiative test). Keeps Joker.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 1 + 3 = 4 — success. Keeps 10.

**Order:** T2 (15) → YT (10) → T1 (10) → T3 (10)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 13 - 3 = 10 — success (raise). -2 to opponents targeting this ship. Raise: negates Stay on Target maneuvers this round.
- TIE 1: **I Can Hold It**
- TIE 2: **I Can Hold It**
- TIE 3: **Stay on Target** vs YT-1300 — negated (YT Evaded with raise).

### Gunnery
*(One weapon system = one target per round. Rolls: YT 5, T1 5, T2 4, T3 11; Damage [13, 9, 22, 19])*
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 22.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 5 - 2 (range) = 3 — miss. Damage 2d10+2 = 13.
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 12 — raise. +4 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 5. Distraction (ship loses all momentum)
- **TIE 1** drew Club: 2d6 = 7. Flight deck ionization (10 stun damage to a random crew member)
- **TIE 3** drew Club: 2d6 = 2. Disaster (Pilot -4; fail = major system failure)

---

## Round 4

### Initiative (start of round)
- YT-1300 shields: **40**.

### Initiative draw
- YT-1300: King♥, Queen♠
- TIE 1: Jack♥, 6♦
- TIE 2: 10♥, 3♠
- TIE 3: 7♦, 4♦

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling +2 Boost = 3. TN 4. Rolls 10 + 3 = 13 — success. Keeps 13.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 3 + 3 = 6 — success. Keeps 11.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 3 + 3 = 6 — success. Keeps 10.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 9 + 3 = 12 — success. Keeps 7.

**Order:** YT (13) → T1 (11) → T2 (10) → T3 (7)

### Maneuver
- YT-1300: **Boost** (top initiative) — Piloting check (TN 4). Roll 9 + 3 = 12 — success. +2 momentum.
- TIE 1: **I Can Hold It**
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 4+3 vs YT: 13 — fail. No effect.
- TIE 3: **Boost** (Pilot d6) — Piloting TN 4. Roll 3+3 = 6 — success. +2 momentum.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 7, T1 5, T2 10, T3 1; Damage [17, 14, 33, 13])*
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 7 - 2 (range) = 5 — **hit.** Damage 2d10+2 = 17. vs Toughness 15: **Shaken.** Pilot must I Can Hold It next round.
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 11 — raise. +4 shields.

---

## Round 5

### Initiative (start of round)
- YT-1300 shields: **40**.

### Initiative draw
- YT-1300: 3♥, 2♣ — **Club drawn**
- TIE 1: 9♦, 9♣ — **Club drawn**
- TIE 2: 6♠, 2♣ — **Club drawn**
- TIE 3: King♣, 8♠ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 1 Handling +4 Boost = 5. TN 4. Rolls 5 + 5 = 10 — success. Keeps 3.
- **TIE 1** Pilot: d6 + 2 + 1. Rolls 3 + 3 = 6 — success. Keeps 9.
- **TIE 2** Pilot: d6 + 2 + 1. Rolls 5 + 3 = 8 — success. Keeps 6.
- **TIE 3** Pilot: d6 + 2 + 1. Rolls 1 + 3 = 4 — success. Keeps 13.

**Order:** T3 (13) → T1 (9) → T2 (6) → YT (3)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 6 - 3 = 3 — fail. No effect.
- TIE 1: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 1: 17+3 vs YT: 10 — success. YT-1300 -2 momentum.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 4+3 vs YT: 10 — fail. No effect.
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 3, T1 5, T2 4, T3 2; Damage [5, 8, 21, 37])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 2 = 2 — miss. Damage 2d10+2 = 37.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 5 = 5 — **hit.** Damage 2d10+2 = 8. Strips 8 from shields. **YT-1300 shields: 32.**
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 = 4 — **hit.** Damage 2d10+2 = 21. Strips 21 from shields. **YT-1300 shields: 11.**
- **YT-1300** vs TIE 1: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 3 - 2 (range) = 1 — miss. Damage 2d10+2 = 5.

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 3 — fail. +0 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 8. Flight deck ionization (10 stun damage to a random crew member)
- **TIE 1** drew Club: 2d6 = 11. Complication (Pilot -2; fail = subsystem offline)
- **TIE 2** drew Club: 2d6 = 11. Complication (Pilot -2; fail = subsystem offline)
- **TIE 3** drew Club: 2d6 = 7. Flight deck ionization (10 stun damage to a random crew member)

---

## Summary

*(Scenario generated with pure random rolls. Run `python gen_scenario.py` to generate a new scenario with different rolls.)*
