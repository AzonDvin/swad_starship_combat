# Scenario: Three TIE Fighters vs YT-1300 Freighter

## Setup

**Location:** Asteroid belt near Ord Mantell. A YT-1300 freighter evades Imperial patrol and is intercepted by three TIE fighters.

**Ships** (see ships.json: `yt_1300`, `tie_fighter`):

| Ship | Size | Handling | Speed | Toughness | Armor | Hull | Shields | Crew |
|------|------|----------|-------|-----------|-------|------|---------|------|
| **YT-1300** | 8 | +0 | 600 | 18 | 4 | 4 | 35 | Pilot, Co-pilot, Gunner |
| **TIE Fighter 1** | 6 | +2 | 800 | 11 | 1 | 3 | — | Pilot, Gunner |
| **TIE Fighter 2** | 6 | +2 | 800 | 11 | 1 | 3 | — | Pilot, Gunner |
| **TIE Fighter 3** | 6 | +2 | 800 | 11 | 1 | 3 | — | Pilot, Gunner |

**Key modifiers:**
- TIEs’ **handling advantage** vs YT-1300: **+1** momentum each round (YT-1300 vs three TIEs: **+0**). See guide: strict majority on Handling; +2 if also ≥ highest enemy Handling + 3.
- YT-1300 has turret; TIEs have fixed forward cannons.
- YT-1300 has shields (35 max); regen 5% + 5%/raise. TIEs have none.
- **One weapon system = one target per round** (quad turret fires at one ship only).
- **Momentum** persists round to round. Lose all: Distraction, becoming Shaken. **Stay on Target** (opposed Piloting): target -1 momentum per success (cumulative; 2 successes = -2, 3 = -3).
- **Joker:** Acts first, +2 to all crew rolls that round, short range.
- **Complications:** Each time a ship **takes hull damage** from an attack (see guide §4), roll **2d6** on the Complications table for **that ship** (usually resolved during or right after Gunnery).
- **Raise:** To-hit roll ≥ 8 (TN+4) adds +1d6 to damage.
- **Crew skills:** YT-1300 Pilot, Co-pilot, Gunner, Engineer = d10 + wild d6 (aces/Wild Cards; take best). TIE Pilot/Gunner = d6.

---

## Round 1

### Initiative (start of round)
- YT-1300 shields: **35**.

### Initiative draw
- **YT-1300:** 8♦
- **TIE 1:** 4♣
- **TIE 2:** 4♠
- **TIE 3:** Queen♣

*Initial initiative draw (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add extra card(s) in Maneuvers; the Pilot chooses which applies—see guide.*

**Order:** T3 (12) → YT (8) → T1 (4) → T2 (4)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 5 - 3 = 2 — fail. No effect.
- TIE 1: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 1: 3+3 vs YT: 14 — fail. No effect.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 3+3 vs YT: 14 — fail. No effect.
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 2+3 vs YT: 14 — fail. No effect.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 9, T1 5, T2 5, T3 2; Damage [5, 10, 19, 11])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 2 = 2 — miss. Damage 2d10+2 = 11.
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 9 - 2 (range) = 7 — **hit.** Damage 2d10+2 = 5. vs Toughness 11: no effect (glancing hit).
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 2 — fail. +0 shields.

### Complications (damage)
- **TIE 3** took hull damage — Complication **2d6 = 5**. Distraction (ship loses all momentum)

---

## Round 2

### Initiative (start of round)
- YT-1300 shields: **35**.

### Initiative draw
- **YT-1300:** 6♠
- **TIE 1:** Ace♣
- **TIE 2:** 4♦
- **TIE 3:** 2♠

*Initial initiative draw (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add extra card(s) in Maneuvers; the Pilot chooses which applies—see guide.*

**Order:** T1 (14) → YT (6) → T2 (4) → T3 (2)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 6 - 3 = 3 — fail. No effect.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 3+3 = 6 — success. +2 momentum.
- TIE 2: **I Can Hold It**
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 1+3 vs YT: 8 — fail. No effect.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 5, T1 5, T2 5, T3 3; Damage [10, 14, 14, 7])*
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 5 = 5 — **hit.** Damage 2d10+2 = 14. Strips 14 from shields. **YT-1300 shields: 21.**
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 5 - 2 (range) = 3 — miss. Damage 2d10+2 = 10.
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 8 — raise. +4 shields.

### Complications (damage)
- **YT-1300** took hull damage — Complication **2d6 = 2**. Disaster (major system failure; roll 1d6 Ship Systems — major column)

---

## Round 3

### Initiative (start of round)
- YT-1300 shields: **25**.

### Initiative draw
- **YT-1300:** 2♣
- **TIE 1:** 4♦
- **TIE 2:** 5♦
- **TIE 3:** Queen♥

*Initial initiative draw (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add extra card(s) in Maneuvers; the Pilot chooses which applies—see guide.*

**Order:** T3 (12) → T2 (5) → T1 (4) → YT (2)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 4 - 3 = 1 — fail. No effect.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 1+3 = 4 — success. +2 momentum.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 2+3 vs YT: 6 — fail. No effect.
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 8, T1 1, T2 2, T3 3; Damage [9, 9, 13, 13])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 13.
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 2 = 2 — miss. Damage 2d10+2 = 13.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 = 1 — miss. Damage 2d10+2 = 9.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 8 - 2 (range) = 6 — **hit.** Damage 2d10+2 = 9. vs Toughness 11: no effect (glancing hit).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 11 — raise. +4 shields.

### Complications (damage)
- **TIE 2** took hull damage — Complication **2d6 = 9**. Complication (subsystem offline; roll 1d6 Ship Systems — subsystem column)

---

## Round 4

### Initiative (start of round)
- YT-1300 shields: **29**.

### Initiative draw
- **YT-1300:** 10♣
- **TIE 1:** Jack♣
- **TIE 2:** Ace♣
- **TIE 3:** 3♥

*Initial initiative draw (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add extra card(s) in Maneuvers; the Pilot chooses which applies—see guide.*

**Order:** T2 (14) → T1 (11) → YT (10) → T3 (3)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 9 - 3 = 6 — success. -2 to opponents targeting this ship.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 5+3 = 8 — success. +2 momentum.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 5+3 vs YT: 15 — fail. No effect.
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 16+3 vs YT: 15 — success. YT-1300 -1 momentum.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 11, T1 5, T2 8, T3 1; Damage [24, 15, 13, 15])*
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 8 - 2 (target Evading) = 6 — **hit.** Damage 2d10+2 = 13. Strips 13 from shields. **YT-1300 shields: 16.**
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 5 - 2 (target Evading) = 3 — miss. Damage 2d10+2 = 15.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 11 - 2 (range) = 9 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 24. vs Toughness 11: **Shaken.** +3 hull damage → **Destroyed**.
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 9 — raise. +4 shields.

### Complications (damage)
- **YT-1300** took hull damage — Complication **2d6 = 2**. Disaster (major system failure; roll 1d6 Ship Systems — major column)
- **TIE 2** took hull damage — Complication **2d6 = 6**. Flight deck ionization (10 stun damage to a random crew member)

---

## Round 5

### Initiative (start of round)
- YT-1300 shields: **20**.

### Initiative draw
- **YT-1300:** 5♠
- **TIE 1:** 8♠
- **TIE 2:** Ace♠
- **TIE 3:** Queen♥

*Initial initiative draw (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add extra card(s) in Maneuvers; the Pilot chooses which applies—see guide.*

**Order:** T2 (14) → T3 (12) → T1 (8) → YT (5)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 4 - 3 = 1 — fail. No effect.
- TIE 1: **I Can Hold It**
- TIE 2: **I Can Hold It**
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 8, T1 15, T2 1, T3 3; Damage [9, 22, 5, 8])*
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 = 1 — miss. Damage 2d10+2 = 5.
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 8.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 15 = 15 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 22. Depletes shields (20). Overflow 2 vs Toughness 18: no hull effect. **Shields: 0.**
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 8 - 2 (range) = 6 — **hit.** Damage 2d10+2 = 9. vs Toughness 11: no effect (glancing hit).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 8 — raise. +4 shields.

### Complications (damage)
- **YT-1300** took hull damage — Complication **2d6 = 7**. Flight deck ionization (10 stun damage to a random crew member)
- **TIE 3** took hull damage — Complication **2d6 = 9**. Complication (subsystem offline; roll 1d6 Ship Systems — subsystem column)

---

## Summary

*(Scenario generated with pure random rolls. Run `python gen_scenario.py` to generate a new scenario with different rolls.)*
