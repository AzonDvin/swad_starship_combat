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
- TIEs have speed advantage (+2 to Piloting vs YT-1300).
- YT-1300 has turret; TIEs have fixed forward cannons.
- YT-1300 has shields (40 max); regen 5% + 5%/raise. TIEs have none.
- **One weapon system = one target per round** (quad turret fires at one ship only).
- **Stay on Target** applies to the target's Piloting **next round only**.
- **Club drawn** = suit ♣; triggers Complications (Phase 7, roll 2d6 on table).
- **Raise:** To-hit roll ≥ 8 (TN+4) adds +1d6 to damage.
- **Crew skills:** YT-1300 Pilot, Co-pilot, Gunner, Engineer = d10 + wild d6 (aces/Wild Cards; take best). TIE Pilot/Gunner = d6.

---

## Round 1

### Initiative (start of round)
- YT-1300 shields: **40**.

### Initiative draw
- YT-1300: 7s, 3h
- TIE 1: Kingc, Jackc — **Club drawn**
- TIE 2: 3d, 2s
- TIE 3: 9s, 2h

### Piloting
- **YT-1300** Pilot (d10+wild d6): d10 + 1 Handling - 2 (speed) - 0 (Stay on Target) = -1. TN 4. Rolls 8 + -1 = 7 — success. Keeps 7.
- **TIE 1** Pilot: d6 + 2 + 2. Rolls 2 + 4 = 6 — success. Keeps 13.
- **TIE 2** Pilot: d6 + 2 + 2. Rolls 2 + 4 = 6 — success. Keeps 3.
- **TIE 3** Pilot: d6 + 2 + 2. Rolls 4 + 4 = 8 — success. Keeps 9.

**Order:** T1 (13) → T3 (9) → YT (7) → T2 (3)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 11 - 3 = 8 — success. Incoming targeting -2, outgoing targeting -2.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 3+4 = 7 — success. +2 Piloting next round.
- TIE 2: **Hold Steady**
- TIE 3: **Boost** (Pilot d6) — Piloting TN 4. Roll 8+4 = 12 — success. +2 Piloting next round.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 5, T1 10, T2 4, T3 3; Damage [14, 17, 11, 16])*
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 10 - 2 (target Evading) = 8 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 17. Strips 17 from shields. **YT-1300 shields: 23.**
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 - 2 (target Evading) = 1 — miss. Damage 2d10+2 = 16.
- **YT-1300** vs TIE 2: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 5 - 2 (range) - 2 (Evade outgoing) = 1 — miss. Damage 2d10+2 = 14.
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 9 — raise. +4 shields.

### Complications (Phase 7)
- **TIE 1** drew Club: 2d6 = 9. Complication (Pilot -2; fail = subsystem offline)

---

## Round 2

### Initiative (start of round)
- YT-1300 shields: **27**.

### Initiative draw
- YT-1300: 7s, 2h
- TIE 1: Kingh, 5h
- TIE 2: 7s, 4d
- TIE 3: Aced, Queenh

### Piloting
- **YT-1300** Pilot (d10+wild d6): d10 + 1 Handling - 2 (speed) - 0 (Stay on Target) = -1. TN 4. Rolls 5 + -1 = 4 — success. Keeps 7.
- **TIE 1** Pilot: d6 + 2 + 2. Rolls 9 + 4 = 13 — success. Keeps 13.
- **TIE 2** Pilot: d6 + 2 + 2. Rolls 8 + 4 = 12 — success. Keeps 7.
- **TIE 3** Pilot: d6 + 2 + 2. Rolls 7 + 4 = 11 — success. Keeps 14.

**Order:** T3 (14) → T1 (13) → YT (7) → T2 (7)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 9 - 3 = 6 — success. Incoming targeting -2, outgoing targeting -2.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 5+4 = 9 — success. +2 Piloting next round.
- TIE 2: **Boost** (Pilot d6) — Piloting TN 4. Roll 11+4 = 15 — success. +2 Piloting next round.
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 5+4 vs YT: 4 — success. YT-1300 -2 Piloting next round.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 6, T1 4, T2 8, T3 2; Damage [14, 17, 6, 21])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 2 - 2 (target Evading) = 0 — miss. Damage 2d10+2 = 21.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 17.
- **YT-1300** vs TIE 1: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 6 - 2 (range) - 2 (Evade outgoing) = 2 — miss. Damage 2d10+2 = 14.
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 3 — fail. +0 shields.

---

## Round 3

### Initiative (start of round)
- YT-1300 shields: **27**.

### Initiative draw
- YT-1300: 9s, 3s
- TIE 1: Queend, 10h
- TIE 2: Kingc, Queens — **Club drawn**
- TIE 3: Queenh, 4c — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): d10 + 1 Handling - 2 (speed) - 2 (Stay on Target) = -3. TN 4. Rolls 7 + -3 = 4 — success. Keeps 9.
- **TIE 1** Pilot: d6 + 2 + 2. Rolls 3 + 4 = 7 — success. Keeps 12.
- **TIE 2** Pilot: d6 + 2 + 2. Rolls 4 + 4 = 8 — success. Keeps 13.
- **TIE 3** Pilot: d6 + 2 + 2. Rolls 3 + 4 = 7 — success. Keeps 12.

**Order:** T2 (13) → T1 (12) → T3 (12) → YT (9)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 8 - 3 = 5 — success. Incoming targeting -2, outgoing targeting -2.
- TIE 1: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 1: 2+4 vs YT: 4 — success. YT-1300 -2 Piloting next round.
- TIE 2: **Hold Steady**
- TIE 3: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 3: 4+4 vs YT: 4 — success. YT-1300 -2 Piloting next round.

### Gunnery
*(One weapon system = one target per round. Rolls: YT 7, T1 1, T2 4, T3 4; Damage [19, 15, 15, 12])*
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 15.
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 - 2 (target Evading) = -1 — miss. Damage 2d10+2 = 15.
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 4 - 2 (target Evading) = 2 — miss. Damage 2d10+2 = 12.
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 7 - 2 (range) - 2 (Evade outgoing) = 3 — miss. Damage 2d10+2 = 19.

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 3 — fail. +0 shields.

### Complications (Phase 7)
- **TIE 2** drew Club: 2d6 = 10. Complication (Pilot -2; fail = subsystem offline)
- **TIE 3** drew Club: 2d6 = 11. Complication (Pilot -2; fail = subsystem offline)

---

## Round 4

### Initiative (start of round)
- YT-1300 shields: **27**.

### Initiative draw
- YT-1300: 9d, 8h
- TIE 1: 7d, 2h
- TIE 2: 6s, 2h
- TIE 3: Kingc, 8c — **Club drawn**

### Piloting
- **YT-1300** Pilot (d10+wild d6): d10 + 1 Handling - 2 (speed) - 2 (Stay on Target) = -3. TN 4. Rolls 4 + -3 = 1 — fail. Keeps 9.
- **TIE 1** Pilot: d6 + 2 + 2. Rolls 4 + 4 = 8 — success. Keeps 7.
- **TIE 2** Pilot: d6 + 2 + 2. Rolls 4 + 4 = 8 — success. Keeps 6.
- **TIE 3** Pilot: d6 + 2 + 2. Rolls 9 + 4 = 13 — success. Keeps 13.

**Order:** T3 (13) → YT (9) → T1 (7) → T2 (6)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 3 - 3 = 0 — fail. No effect.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 4+4 = 8 — success. +2 Piloting next round.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 4+4 vs YT: 1 — success. YT-1300 -2 Piloting next round.
- TIE 3: **Hold Steady**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 5, T1 5, T2 1, T3 1; Damage [13, 8, 5, 26])*
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 = 1 — miss. Damage 2d10+2 = 26.
- **YT-1300** vs TIE 3: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 5 - 2 (range) = 3 — miss. Damage 2d10+2 = 13.
- **TIE 1**: No advantage — cannot fire (fixed forward cannons).
- **TIE 2**: No advantage — cannot fire (fixed forward cannons).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 3 — fail. +0 shields.

### Complications (Phase 7)
- **TIE 3** drew Club: 2d6 = 8. Complication (Pilot -2; fail = subsystem offline)

---

## Round 5

### Initiative (start of round)
- YT-1300 shields: **27**.

### Initiative draw
- YT-1300: 7s, 6d
- TIE 1: Aceh, Kingd
- TIE 2: Kingc, 6h — **Club drawn**
- TIE 3: 8d, 7h

### Piloting
- **YT-1300** Pilot (d10+wild d6): d10 + 1 Handling - 2 (speed) - 2 (Stay on Target) = -3. TN 4. Rolls 4 + -3 = 1 — fail. Keeps 7.
- **TIE 1** Pilot: d6 + 2 + 2. Rolls 2 + 4 = 6 — success. Keeps 14.
- **TIE 2** Pilot: d6 + 2 + 2. Rolls 5 + 4 = 9 — success. Keeps 13.
- **TIE 3** Pilot: d6 + 2 + 2. Rolls 5 + 4 = 9 — success. Keeps 8.

**Order:** T1 (14) → T2 (13) → T3 (8) → YT (7)

### Maneuver
- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll 5 - 3 = 2 — fail. No effect.
- TIE 1: **Boost** (Pilot d6) — Piloting TN 4. Roll 1+4 = 5 — success. +2 Piloting next round.
- TIE 2: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE 2: 8+4 vs YT: 1 — success. YT-1300 -2 Piloting next round.
- TIE 3: **Hold Steady**

### Gunnery
*(One weapon system = one target per round. Rolls: YT 13, T1 3, T2 5, T3 1; Damage [12, 10, 11, 11])*
- **TIE 1** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 3 = 3 — miss. Damage 2d10+2 = 10.
- **TIE 2** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 5 = 5 — **hit.** Damage 2d10+2 = 11. Strips 11 from shields. **YT-1300 shields: 16.**
- **TIE 3** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll 1 = 1 — miss. Damage 2d10+2 = 11.
- **YT-1300** vs TIE 1: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll 13 - 2 (range) = 11 — **hit **with raise** (+1d6).** Damage 2d10+2+1d6 = 12. vs Toughness 15: no effect (glancing hit).

### Systems
- YT-1300 Electronics (Engineer d10+wild d6): Rolls 9 — raise. +4 shields.

### Complications (Phase 7)
- **TIE 2** drew Club: 2d6 = 9. Complication (Pilot -2; fail = subsystem offline)

---

## Summary

*(Scenario generated with pure random rolls. Run `python gen_scenario.py` to generate a new scenario with different rolls.)*
