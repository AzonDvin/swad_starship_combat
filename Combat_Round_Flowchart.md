# Star Wars Ship Combat: Round-by-Round Flowchart

A quick reference for players showing what to do in each phase. See the full combat guide for details.

### Phase Details

**1. Initiative** — *Who: All ships*

- Each ship draws 2 cards (GM deals)
- Note Clubs — they trigger complications in Phase 7
- Higher card = acts first and has advantage over lower cards
- Range from card: 2 = none; 3–7 = long (-4); 8–Jack = medium (-2); Queen–Joker = short (0)
- **Joker:** Acts first, +2 to all crew rolls that round, counts as short range

**2. Support** — *Who: Co-pilot, Commander, Engineer, Systems Operator*

- One Support action per crewmember per round
- Support Pilot: Common Knowledge, Notice, or Piloting → +1/+2 to Pilot's Piloting check
- Spot for Gunner: Notice → +1/+2 to one Gunner's Shooting
- Engineer: Repair or Knowledge (Eng) → +1/+2 to Pilot
- Systems: Electronics or Notice → Sensor lock (+1/+2 to one Gunner)
- Co-pilot may call primary target → first Gunner to hit gets +1 (1/round)

**3. Piloting** — *Who: Pilot only*

- Piloting check TN 4 (mods: Handling, speed advantage, hull, Support bonuses)
- Success = keep highest of 2 cards. Raise = draw another, pick best. Fail = must take lowest
- Modifiers: +2 if faster than opponent; +4 if 2× faster

**4. Maneuver** — *Who: Pilot only*

- Choose one: Evade | Stay on Target | Hold Steady | Boost | Loop
- Evade: Piloting TN 4, -1 per opposing ship; success = -2 incoming targeting, -2 outgoing targeting; raise = -1 outgoing targeting
- Stay on Target: Opposed Piloting vs target; success = target -2 Piloting next round
- Hold Steady: Cancels Evade (incoming and outgoing penalties); +1 Piloting next round. Shaken ship: must declare Hold Steady (clears Shaken); may still fire.
- Boost: Piloting TN 4; success = +2 Piloting next round; raise = +2 and draw extra card
- Loop: Piloting (See note); success = reverse advantage with one ship this round + +1 Piloting next round

**5. Gunnery** — *Who: Gunners (act in initiative order)*

- Systems Operator declares shield facing (if directional) — before firing
- With advantage: Fire all weapons that bear on target(s); each weapon system may target a different enemy
- Without advantage: Turret weapons only, -2 to Shooting
- To hit: TN 4. Modifiers stack (e.g., target Evading -2 + medium -2 = -4; or your Evade outgoing targeting -2 or -1 when Evading)
- Snapfire (torpedoes): -2 unless target at short range
- Damage to shields first; excess to hull (Damaged = -1, Crippled = -2, max = destroyed)

**6. Systems** — *Who: Engineer, Systems Operator*

- Engineer: Repair subsystem (bring offline system back)
- Systems Operator: Electronics check for shield regen — success = 5% of max, +5% per raise
- Systems Operator: Jamming (Electronics opposed) → -2 to enemy attacks

**7. Complications** — *Who: GM (players may react)*

- Resolve each Club drawn in Phase 1: roll 2d6 on Complications table
- If result is **major system failure** or **subsystem offline**: roll 1d6 on Ship Systems Chart to determine which system
- Engineer may attempt Reinforce (when Club drawn)
- Systems Operator may Diagnose (Electronics/Repair) → +1 to Engineer

---

## Role Quick Reference: "What Can I Do?"

### Pilot


| Phase           | Action                                                                                |
| --------------- | ------------------------------------------------------------------------------------- |
| 1 Initiative    | — (observe cards; declare speed for modifiers)                                        |
| 2 Support       | —                                                                                     |
| 3 Piloting      | **Piloting check** — keep high/low card based on result                               |
| 4 Maneuver      | **Choose maneuver** — Evade, Stay on Target, Hold Steady, Boost, or Loop (modifiers apply next round) |
| 5 Gunnery       | — (unless also Gunner)                                                                |
| 6 Systems       | —                                                                                     |
| 7 Complications | —                                                                                     |


### Gunner


| Phase           | Action                                                                  |
| --------------- | ----------------------------------------------------------------------- |
| 1 Initiative    | —                                                                       |
| 2 Support       | — (unless Co-pilot spots for you)                                       |
| 3 Piloting      | —                                                                       |
| 4 Maneuver      | —                                                                       |
| 5 Gunnery       | **Fire weapons** — all if advantage, turrets only at -2 if no advantage |
| 6 Systems       | —                                                                       |
| 7 Complications | —                                                                       |


### Engineer


| Phase           | Action                                                           |
| --------------- | ---------------------------------------------------------------- |
| 1 Initiative    | —                                                                |
| 2 Support       | **Support Pilot** (Repair or Knowledge: Eng) — +1/+2 to Piloting |
| 3 Piloting      | —                                                                |
| 4 Maneuver      | —                                                                |
| 5 Gunnery       | —                                                                |
| 6 Systems       | **Repair** subsystem (bring offline system back)                |
| 7 Complications | **Reinforce** (when Club drawn; same modifier as Pilot; success = avoid failure) |


### Co-pilot / Commander


| Phase           | Action                                                             |
| --------------- | ------------------------------------------------------------------ |
| 1 Initiative    | Tactical assessment (Smarts/Battle) — reroll for one crewmember    |
| 2 Support       | **Support Pilot** or **Spot for Gunner**                           |
| 3 Piloting      | —                                                                  |
| 4 Maneuver      | —                                                                  |
| 5 Gunnery       | **Call primary target** — first Gunner to hit gets +1 (once/round) |
| 6 Systems       | —                                                                  |
| 7 Complications | —                                                                  |


### Systems Operator


| Phase           | Action                                                       |
| --------------- | ------------------------------------------------------------ |
| 1 Initiative    | —                                                            |
| 2 Support       | **Sensor lock** (Electronics/Notice) — +1/+2 to one Gunner   |
| 3 Piloting      | —                                                            |
| 4 Maneuver      | —                                                            |
| 5 Gunnery       | **Declare shield facing** (before firing, if directional)    |
| 6 Systems       | **Activate shield regen** (Electronics) or **Jamming**       |
| 7 Complications | **Diagnose** (Electronics/Repair) when Club — +1 to Engineer |


---

## Key Tables

**Range (from initiative card)**


| Card        | Range   | Modifier |
| ----------- | ------- | -------- |
| 2           | No shot | —        |
| 3–7         | Long    | -4       |
| 8–Jack      | Medium  | -2       |
| Queen–Joker | Short   | 0        |


**Complications (2d6 when Club drawn)** — If major system failure or subsystem offline, also roll 1d6 on Ship Systems Chart.


| Roll | Effect                                                               |
| ---- | -------------------------------------------------------------------- |
| 2    | Disaster: Piloting -4; fail = **major system failure** (roll 1d6)    |
| 3–7  | Major: Pilot roll -4; fail = **subsystem offline** (roll 1d6)        |
| 8–Q  | Complication: Pilot roll -2; fail = **subsystem offline** (roll 1d6) |
| A    | Distraction: -2 Shooting this round                                  |


**Ship Systems Chart (1d6)** — See full combat guide for details.


| d6  | System            | Major Failure                             | Subsystem Offline                         |
| --- | ----------------- | ----------------------------------------- | ----------------------------------------- |
| 1   | Sublight Engines  | Speed = 0 until repaired                  | Handling -1 until repaired                |
| 2   | Nav Computer      | Hyperdrive offline; cannot jump           | Astrogation checks delayed until repaired |
| 3   | Deflector Shields | All shields down; no absorption           | Shield flickering; no regen until repair  |
| 4   | Weapons           | All weapons offline                       | One weapon bank or turret offline         |
| 5   | Life Support      | Hull breach; -2 all checks until repaired | -1 to one crew check this round           |
| 6   | Sensors / Comms   | -4 Shooting; no comms                     | -2 Shooting until repaired                |


**Combat end:** Voluntary hyperjump (Astrogation if Nav Computer ok); GM may narratively call off pursuit; or after round 5, GM rolls each round — **odd** = combat ends; **even** = continues.