# Scenario: Two TIE Fighters vs YT-1300 Freighter

## Setup

**Location:** Hyperspace lane near the Corellian Run. A Rebel-sympathizing YT-1300 freighter runs a blockade and is jumped by a pair of Imperial TIE fighters on patrol.

**Ships** (see ships.json: `millennium_falcon`, `tie_fighter`):

| Ship | Size | Handling | Top Speed | Toughness | Armor | Shields | Crew |
|------|------|----------|-----------|-----------|-------|---------|------|
| **YT-1300** "Starlight" | 8 | +1 | 650 | 25 (6) | 6 | 40 | Pilot, Co-pilot, Gunner, Engineer |
| **TIE Fighter 1** | 6 | +2 | 800 | 20 (5) | 5 | — | Pilot, Gunner |
| **TIE Fighter 2** | 6 | +2 | 800 | 20 (5) | 5 | — | Pilot, Gunner |

**Key modifiers:**
- TIEs have **handling advantage** vs YT-1300 (+1 momentum each; see guide: Handling vs strict majority of opponents).
- YT-1300 has turret; TIEs have fixed forward cannons.
- YT-1300 has shields (40 max); regen requires Electronics check in Systems phase (5% + 5%/raise). TIEs have none.
- Ship stats and weapons align with ships.json (TIE: 2d10+2 dual lasers; YT-1300 modified: quad turret 2d10+2).
- **Complications:** When a ship **takes hull damage** from a hit (see guide §4), roll **2d6** on the Complications table for **that ship** (not tied to initiative suit).

---

## Round 1

### Initiative
Each ship draws **one** initiative card (**no Piloting roll**). Results:
- YT-1300: **9♥**
- TIE 1: **Queen♣**
- TIE 2: **7♦**

**Order:** TIE 1 (Queen) → YT-1300 (9) → TIE 2 (7)

**Advantage:** TIE 1 has advantage over both. YT-1300 has advantage over TIE 2. TIE 2 has advantage over no one.

**Range (from cards):** Queen = short (0). 9 = medium (-2). 7 = long (-4).

### Support
- YT-1300 Co-pilot Supports Pilot (Notice): success → +1 to Pilot's Piloting (maneuver checks this round).

### Maneuver
- TIE 1: **I Can Hold It** — maintains position on YT-1300's tail.
- YT-1300: **Evade** — Piloting check (TN 4), -2 (2 opponents). Roll 9 - 2 = 7 — success. Their incoming targeting -2, their outgoing targeting -2.
- TIE 2: **Stay on Target** vs YT-1300. Opposed Piloting: TIE 2 wins. YT-1300 suffers -1 momentum.

### Gunnery
- **TIE 1** (advantage, short range): Fires dual lasers at YT-1300. TN 4. Roll 9 - 2 (target Evading) = 7 vs TN 4. **Hit.** Damage 2d10+2 = 14. Strips 14 from YT-1300 shields. **YT-1300 shields: 26.**
- **YT-1300** (advantage over TIE 2, medium range): Gunner fires quad turret at TIE 2. TN 4. Roll 3 - 2 (range) - 2 (Evade outgoing targeting) = -1 vs TN 4. **Miss.**
- **TIE 2** (no advantage): Return fire with turrets only — TIEs have no turrets. **Cannot fire** (fixed forward cannons only; no turret to return fire).

### Systems
- YT-1300 Systems Operator: **Electronics** check to activate shield regen. Rolls 7 — success. Recover 5% of 40 = **2**. **YT-1300 shields: 28.**

### Complications (damage)
- **YT-1300** took hull damage (shield hit from TIE 1). Complication **2d6 = 9**. **Complication:** Pilot roll -2; fail = subsystem offline. YT-1300 Pilot makes Piloting check (TN 4, -2): rolls 3, fail. **Sensor glitch** on freighter — -1 to next Gunnery (GM fiat).

---

## Round 2

### Initiative (start of round)
- YT-1300 shields: **28** (after R1 Systems regen).

### Initiative draw
- YT-1300: **Jack♦** (medium, -2)
- TIE 1: **10♠** (medium, -2)
- TIE 2: **8♣** (medium, -2)

**Order:** YT-1300 (Jack) → TIE 1 (10) → TIE 2 (8)

**Advantage:** YT-1300 has advantage over both TIEs this round.

### Maneuver
- YT-1300: **I Can Hold It** — steady flight.
- TIE 1: **I Can Hold It** — maintains pursuit (not Shaken yet; becomes Shaken in Gunnery).
- TIE 2: **Evade** — Piloting check (TN 4), -1 (1 opponent). Roll 6 - 1 = 5 — success. Their incoming targeting -2, their outgoing targeting -2.

### Gunnery
- **YT-1300** (advantage): Quad turret at TIE 1, medium range (-2). TN 4. Roll 9 - 2 = 7 vs TN 4. **Hit.** Damage 2d10+2 = 20. TIE 1 has no shields. vs Toughness 20: **TIE 1 Shaken.**
- **TIE 1** (Shaken): Fires at YT-1300. TN 4. YT-1300 used I Can Hold It (no Evade). Roll 4 - 1 (sensor glitch) = 3 vs TN 4. **Miss.**
- **TIE 2** (no advantage): Cannot fire (no turret).

### Systems
- YT-1300 Systems Operator: Electronics check for shield regen. Rolls 6 — success. +2. **YT-1300 shields: 30.**

### Complications (damage)
- **TIE 1** took hull damage (hit from YT-1300; Shaken). Complication **2d6 = 6**. **Flight deck ionization:** 10 stun damage to a random crew member (see Complications table).

---

## Round 3

### Initiative (start of round)
- YT-1300 shields: **30.**

### Initiative draw
- YT-1300: **Ace♠** (short, 0)
- TIE 1: **9♥** (medium, -2)
- TIE 2: **Queen♦** (short, 0)

**Order:** YT-1300 (Ace) → TIE 2 (Queen) → TIE 1 (9)

**Advantage:** YT-1300 has advantage over both. TIE 2 has advantage over TIE 1.

### Maneuver
- YT-1300: **Evade** — Piloting check (TN 4), -2 (2 opponents). Roll 8 - 2 = 6 — success. Their incoming targeting -2, their outgoing targeting -2.
- TIE 2: **Stay on Target** vs YT-1300 — success. YT-1300 -1 momentum next round.
- TIE 1: **I Can Hold It** — clears Shaken (required; cannot take other maneuver).

### Gunnery
- **YT-1300** (advantage over TIE 1, medium range): Quad turret at TIE 1. TN 4. Roll 8 - 2 (range) - 2 (Evade outgoing targeting) = 4 vs TN 4. **Hit.** Damage 2d10+2 = 24. 24 exceeds Toughness 20 by 4 = **1 hull damage** (and Shaken). TIE 1 hull-damaged, -1 to all rolls.
- **TIE 2** (advantage over TIE 1, short range): Dual lasers at YT-1300. TN 4. Roll 10 - 2 (target Evading) = 8 vs TN 4. **Hit.** Damage 2d10+2 = 16. **YT-1300 shields: 14.**
- **TIE 1** (no advantage, hull-damaged): Cannot fire.

### Systems
- YT-1300 Systems Operator: Electronics for regen. Rolls 11 — **raise!** 10% of 40 = 4. **YT-1300 shields: 18.**

### Complications (damage)
- **TIE 1** took hull damage (hull from quad turret). Complication **2d6 = 5**. **Distraction** — TIE 1 loses all momentum.
- **YT-1300** took hull damage (shield hit from TIE 2). Complication **2d6 = 8**. **Flight deck ionization:** 10 stun damage to a random crew member.

---

## Round 4

### Initiative (start of round)
- YT-1300 shields: **18.**

### Initiative draw
- YT-1300: **10♥** (medium, -2)
- TIE 1: **3♦** (long, -4)
- TIE 2: **Joker** — acts first, **short range**, **+2 to all crew rolls** this round

**Order:** TIE 2 (Joker) → YT-1300 (10) → TIE 1 (3)

**Advantage:** TIE 2 (Joker) has advantage over all.

### Maneuver
- TIE 2: **I Can Hold It** — keeps position.
- YT-1300: **Evade** — Piloting check (TN 4), -2 (2 opponents). Roll 7 - 2 = 5 — success. Their incoming targeting -2, their outgoing targeting -2 (effect carries into Gunnery).
- TIE 1: **I Can Hold It** — clears Shaken (required; cannot take other maneuver).

### Gunnery
- **TIE 2** (Joker, +2, short, target Evading -2): TN 4. Roll 9 + 2 (Joker) - 2 (target Evading) = 9 vs TN 4. **Hit with raise** (+1d6 damage). Damage 2d10+2+1d6 = 18+4 = 22. Strips 18 shields. **YT-1300 shields: 0** (depleted). Overflow 4 vs Toughness 25 — no effect (4 < 25).
- **YT-1300** (advantage over TIE 1): Fires at TIE 1. TIE 1 at range 3 — long (-4). TN 4. Roll 10 - 4 (range) - 2 (Evade outgoing targeting) = 4 vs TN 4. **Hit.** Damage 2d10+2 = 24. TIE 1: 1 hull damage already; 24 exceeds Toughness 20 by 4 = **2nd hull damage.** Crippled; -2 all rolls.
- **TIE 1** (no advantage, 2 hull damage): Card is 3 — long range. Cannot fire effectively; no turret anyway.

### Systems
- YT-1300 Systems Operator: Electronics for regen. Rolls 5 — success. +2. **YT-1300 shields: 2** (narrowly restored from zero).

### Complications (damage)
- **YT-1300** took hull damage (shields depleted; overflow did not add hull damage). Complication **2d6 = 3**. **Distraction** — YT-1300 loses all momentum.
- **TIE 1** took hull damage (second hull hit; Crippled). Complication **2d6 = 11**. **Complication:** Pilot -2; fail = subsystem offline (GM resolves).

---

## Round 5

### Initiative (start of round)
- YT-1300 shields: **2.**

### Initiative draw
- YT-1300: **8♦** (medium, -2)
- TIE 1: **5♥** (long, -4)
- TIE 2: **9♣** (medium, -2)

**Order:** TIE 2 (9) → YT-1300 (8) → TIE 1 (5)

**Advantage:** TIE 2 over both. YT-1300 over TIE 1.

### Maneuver
- TIE 2: **I Can Hold It**
- YT-1300: **Loop** — Piloting check (See guide). Modifier -(Size − Handling) = -(8 − 1) = -7. Roll 11 - 7 = 4 — success (d8 aced: 8+3). Reverses advantage with TIE 2 (who had higher card) — now on TIE 2's tail. Turret can bear.
- TIE 1: **I Can Hold It** — too damaged to maneuver aggressively.

### Gunnery
- **TIE 2** (advantage): Cannot fire — after YT-1300's Loop, the freighter is on TIE 2's six; fixed forward cannons cannot bear on a target behind.
- **YT-1300** (Loop complete; has advantage over TIE 2 this round): Turret fires at TIE 2, short range. TN 4. Roll 11 vs TN 4. **Hit with raise** (+1d6 damage). Damage 2d10+2+1d6 = 22+4 = 26. TIE 2 has no shields. 26 exceeds Toughness 20 by 6 = **TIE 2 Shaken and 1 hull damage.**
- **TIE 1** (no advantage, 2 hull damage): Cannot fire (no turret).

### Systems
- YT-1300 Systems Operator: Electronics for regen. Rolls 6 — success. +2. **YT-1300 shields: 4.**

### Complications (damage)
- **TIE 2** took hull damage (hull from YT-1300 turret). Complication **2d6 = 4**. **Distraction** — TIE 2 loses all momentum (see Complications table).

### Combat End
GM rolls: **5 = odd.** Combat ends. YT-1300 breaks away; TIEs disengage. TIE 1 is badly damaged; TIE 2 is hull-damaged. The freighter escapes with shields at 4/40 and no hull damage (shields briefly dropped to zero in Round 4 but regen brought them back).

---

## Summary

| Round | Key events |
|-------|------------|
| 1 | TIE 1 scores first hit (14 shield damage); YT-1300 Complication (sensor glitch). Systems: Electronics success → +2 regen (28 total). |
| 2 | YT-1300 gains advantage, Shakes TIE 1; TIE 1 Complication (flight deck ionization). Systems: +2 regen (30). |
| 3 | TIE 2 inflicts 16 damage; TIE 1 & YT-1300 Complications. Systems: Electronics raise → +4 regen (18 total). YT-1300 damages TIE 1 hull. |
| 4 | TIE 2 draws Joker, depletes shields (18 → 0); YT-1300 & TIE 1 Complications. Systems: +2 regen (2). YT-1300 cripples TIE 1 (2 hull damage). |
| 5 | YT-1300 Loops, reverses the chase, damages TIE 2 hull. Systems: +2 regen (4). Odd roll ends combat — freighter escapes. |

**Result:** YT-1300 survives through shield absorption (regen via Electronics checks kept shields in the fight after a brief depletion), turret flexibility (return fire without advantage), Evade, and a timely Loop. TIEs' lack of shields and turrets left them vulnerable when the freighter turned the tables.
