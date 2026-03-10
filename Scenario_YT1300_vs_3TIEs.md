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
- TIEs have speed advantage (+1 momentum vs YT-1300).
- YT-1300 has turret; TIEs have fixed forward cannons.
- YT-1300 has shields (35 max); regen 5% + 5%/raise. TIEs have none.
- **One weapon system = one target per round** (quad turret fires at one ship only).
- **Momentum** persists round to round. Lose all: Distraction, becoming Shaken. **Stay on Target** (opposed Piloting): target -2 momentum per success (cumulative; 2 successes = -4, 3 = -6); each side adds its momentum to its roll.
- **Joker:** Acts first, Pilot auto-passes initiative test, +2 to all crew rolls that round, short range.
- **Club drawn** = suit ♣; triggers Complications (Phase 7, roll 2d6 on table).
- **Raise:** To-hit roll ≥ 8 (TN+4) adds +1d6 to damage.
- **Crew skills:** YT-1300 Pilot, Co-pilot, Gunner, Engineer = d10 + wild d6 (aces/Wild Cards; take best). TIE Pilot/Gunner = d6.

---

## Round 1

### Initiative (start of round)
- YT-1300 shields: **35**.

### Initiative draw
- YT-1300: 8♦, 7♣ — **Club drawn**
- TIE 1: 9♣, 2♦ — **Club drawn**
- TIE 2: 7♠, 6♦
- TIE 3: 7♥, 6♥

### Piloting
- **YT-1300** Pilot (d10+wild d6): 0 Handling = 0. TN 4. Rolls 10 + 0 = 10 — success. Keeps 8.
- **TIE 1** Pilot: d6 + 3. Rolls 1 + 3 = 4 — success. Keeps 9.
- **TIE 2** Pilot: d6 + 3. Rolls 14 + 3 = 17 — success. Keeps 7.
- **TIE 3** Pilot: d6 + 3. Rolls 11 + 3 = 14 — success. Keeps 7.

**Order:** T1 (9) → YT (8) → T2 (7) → T3 (7)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 8 - 3 = 5 — success. -2 to opponents targeting this ship.
- TIE 1: **I Can Hold It**
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 3+3 vs YT: 10 — fail. No effect.
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 17, T1 4, T2 2, T3 3; Damage [19, 13, 12, 12])*
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 13.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 17 - 2 (range) = 15 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 19. vs Toughness 11: **Shaken.** +2 hull damage → **Crippled** (−2 all checks).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 6 — success. +2 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 11. Complication (Pilot -2; fail = subsystem offline)
- **TIE 1** drew Club: 2d6 = 8. Flight deck ionization (10 stun damage to a random crew member)

---

## Round 2

### Initiative (start of round)
- YT-1300 shields: **35**.

### Initiative draw
- YT-1300: Queen♣, 10♠ — **Club drawn**
- TIE 1: Jack♣, 5♥ — **Club drawn**
- TIE 2: Jack♥, 9♠
- TIE 3: Ace♦, 4♣ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 0 Handling = 0. TN 4. Rolls 14 + 0 = 14 — success. Keeps 12.
- **TIE 1** Pilot: d6 + 3. Rolls 15 + 3 = 18 — success. Keeps 11.
- **TIE 2** Pilot: d6 + 3. Rolls 2 + 3 = 5 — success. Keeps 11.
- **TIE 3** Pilot: d6 + 3. Rolls 2 + 3 = 5 — success. Keeps 14.

**Order:** T3 (14) → YT (12) → T1 (11) → T2 (11)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 11 - 3 = 8 — success (raise). -2 to opponents targeting this ship. Raise: negates Stay on Target maneuvers this round.
- TIE 1: **Stay on Target** vs YT-1300 — negated (YT Evaded with raise).
- TIE 2: **I Can Hold It**
- TIE 3: **Stay on Target** vs YT-1300 — negated (YT Evaded with raise).

### Gunnery
*(One weapon system = one target per round. Rolls: YT 7, T1 2, T2 16, T3 1; Damage [10, 29, 14, 24])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 - 2 (target Evading) = -1 — miss. Damage 2d10+2 = 24.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 7 - 2 (range) = 5 — **hit.** Damage 2d10+2 = 10. vs Toughness 11: no effect (glancing hit).
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 8 — raise. +4 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 3. Distraction (ship loses all momentum)
- **TIE 1** drew Club: 2d6 = 4. Distraction (ship loses all momentum)
- **TIE 3** drew Club: 2d6 = 11. Complication (Pilot -2; fail = subsystem offline)

---

## Round 3

### Initiative (start of round)
- YT-1300 shields: **35**.

### Initiative draw
- YT-1300: 5♦, 5♣ — **Club drawn**
- TIE 1: 6♥, 2♦
- TIE 2: 8♠, 6♦
- TIE 3: King♣, 3♠ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 0 Handling = 0. TN 4. Rolls 19 + 0 = 19 — success. Keeps 5.
- **TIE 1** Pilot: d6 + 3. Rolls 5 + 3 = 8 — success. Keeps 6.
- **TIE 2** Pilot: d6 + 3. Rolls 3 + 3 = 6 — success. Keeps 8.
- **TIE 3** Pilot: d6 + 3. Rolls 5 + 3 = 8 — success. Keeps 13.

**Order:** T3 (13) → T2 (8) → T1 (6) → YT (5)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 8 - 3 = 5 — success. -2 to opponents targeting this ship.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 3+3 = 6 — success. +2 momentum.
- TIE 2: **I Can Hold It**
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 8, T1 10, T2 5, T3 7; Damage [8, 11, 17, 9])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 7 - 2 (target Evading) = 5 — **hit.** Damage 2d10+2 = 9. Strips 9 from shields. **YT-1300 shields: 26.**
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 5 - 2 (target Evading) = 3 — miss. Damage 2d10+2 = 17.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 10 - 2 (target Evading) = 8 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 11. Strips 11 from shields. **YT-1300 shields: 15.**
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 8 - 2 (range) = 6 — **hit.** Damage 2d10+2 = 8. vs Toughness 11: no effect (glancing hit).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 5 — success. +2 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 5. Distraction (ship loses all momentum)
- **TIE 3** drew Club: 2d6 = 3. Distraction (ship loses all momentum)

---

## Round 4

### Initiative (start of round)
- YT-1300 shields: **17**.

### Initiative draw
- YT-1300: Ace♣, 7♠ — **Club drawn**
- TIE 1: 10♣, 4♦ — **Club drawn**
- TIE 2: Jack♥, 10♠
- TIE 3: 10♠, 3♠

### Piloting
- **YT-1300** Pilot (d10+wild d6): 0 Handling = 0. TN 4. Rolls 8 + 0 = 8 — success. Keeps 14.
- **TIE 1** Pilot: d6 + 3. Rolls 1 + 3 = 4 — success. Keeps 10.
- **TIE 2** Pilot: d6 + 3. Rolls 2 + 3 = 5 — success. Keeps 11.
- **TIE 3** Pilot: d6 + 3. Rolls 4 + 3 = 7 — success. Keeps 10.

**Order:** YT (14) → T2 (11) → T1 (10) → T3 (10)

### Maneuver
- YT-1300: **Boost** (top initiative) — Piloting check (TN 4). Roll 2 + 0 = 2 — fail. No effect.
- TIE 1: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 1: 5+3 vs YT: 8 — success. YT-1300 -2 momentum.
- TIE 2: **I Can Hold It**
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 4+3 vs YT: 8 — fail. No effect.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 4, T1 5, T2 2, T3 11; Damage [7, 29, 13, 26])*
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 4 - 2 (range) = 2 — miss. Damage 2d10+2 = 7.
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 9 — raise. +4 shields.

### Complications (Phase 7)
- **YT-1300** drew Club: 2d6 = 7. Flight deck ionization (10 stun damage to a random crew member)
- **TIE 1** drew Club: 2d6 = 9. Complication (Pilot -2; fail = subsystem offline)

---

## Round 5

### Initiative (start of round)
- YT-1300 shields: **21**.

### Initiative draw
- YT-1300: Jack♦, 9♦
- TIE 1: Ace♥, 5♥
- TIE 2: Ace♥, 10♠
- TIE 3: 7♣, 7♥ — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): 0 Handling -2 Stay on Target = -2. TN 4. Rolls 6 + -2 = 4 — success. Keeps 11.
- **TIE 1** Pilot: d6 + 3. Rolls 3 + 3 = 6 — success. Keeps 14.
- **TIE 2** Pilot: d6 + 3. Rolls 3 + 3 = 6 — success. Keeps 14.
- **TIE 3** Pilot: d6 + 3. Rolls 13 + 3 = 16 — success. Keeps 7.

**Order:** T1 (14) → T2 (14) → YT (11) → T3 (7)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 9 - 3 = 6 — success. -2 to opponents targeting this ship.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 4+3 = 7 — success. +2 momentum.
- TIE 2: **I Can Hold It**
- TIE 3: **I Can Hold It**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 8, T1 4, T2 4, T3 5; Damage [13, 9, 27, 28])*
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 9.
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 27.
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 8 - 2 (range) = 6 — **hit.** Damage 2d10+2 = 13. vs Toughness 11: **Shaken.** Pilot must I Can Hold It next round.
- **TIE 3**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 3 — fail. +0 shields.

### Complications (Phase 7)
- **TIE 3** drew Club: 2d6 = 6. Flight deck ionization (10 stun damage to a random crew member)

---

## Summary

*(Scenario generated with pure random rolls. Run `python gen_scenario.py` to generate a new scenario with different rolls.)*
