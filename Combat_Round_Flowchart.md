# Star Wars Ship Combat: Round-by-Round Flowchart

A quick reference for players. Full rules: **SWADE_Star_Wars_Ship_Combat_Guide.md** (§2 initiative/maneuvers, §4 shields/hull/momentum, §5 round sequence and jobs).

**Momentum:** Starts at 0; **persists round to round.** Maneuvers and handling advantage add/subtract. Lose all: **Distraction** complication, or **Shaken**. All **Piloting** rolls **add** (or **subtract**) **current momentum**.

### Round order (quick)

1. **Initiative** — one card each; order, advantage, range (no Pilot Piloting roll).  
2. **Support** (optional) — crew trait rolls **before** maneuvers.  
3. **Maneuver** — Pilot chooses one maneuver.  
4. **Gunnery** — Shooting; **hull damage** (see §4) → **Complications 2d6** for the ship hit.  
5. **Systems** — repairs, shield regen, jamming.  
6. **Complications** — Reinforce, Diagnose, follow-up; **end of round:** **break away** if eligible.

### Phase Details

**1. Initiative** — *Who: All ships*

- Each ship draws **one** card (GM deals); **Pilot** does not roll Piloting for initiative. **Boost** raise or **I Know a Few Maneuvers** (phase 3): extra initiative card(s), **choose** which applies—see guide §2.
- Suits are **not** a complications trigger (optional flavor only).
- Higher card = acts first, has **advantage** over lower cards.
- Range from card: 2 = no shot; 3–7 = long (−4); 8–Jack = medium (−2); Queen–Joker = short (0).
- **Joker:** Acts first regardless of rank; +2 to all crew rolls that round; short range (0) for attacks.
- **Handling advantage:** +1 momentum if your Handling beats a **strict majority** of opponents; +2 if you also have Handling ≥ **highest enemy Handling + 3**. Applies to maneuver-phase Piloting and opposed Piloting (guide §2).

**2. Support (optional)** — *Who: Co-pilot, Commander, Engineer, Systems Operator*

- **After** initiative cards, **before** Maneuvers. Optional **trait rolls** (Notice, Repair, Electronics, Smarts/Battle, etc.).
- One Support action per crewmember per round (co-pilot: pick one option below).
- Support Pilot: Common Knowledge, Notice, or Piloting → +1/+2 to Pilot’s upcoming maneuver check.
- Tactical assessment: Smarts or Battle → one crew reroll / ignore −2 (guide).
- Spot for Gunner: Notice → +1/+2 to one Gunner’s Shooting.
- Engineer: Repair or Knowledge (Eng) → +1/+2 to Pilot.
- Systems Op: Electronics or Notice → Sensor lock (+1/+2 to one Gunner).

**3. Maneuver** — *Who: Pilot only*

- Choose one: **Evade** | **Stay on Target** | **I Have You Now** | **I Can Hold It** | **Boost** | **I Know a Few Maneuvers** | **Loop**
- **Evade:** Piloting TN 4, −1 per opposing ship; success = −2 to opponents **targeting this ship**; raise = negates **Stay on Target** vs this ship this round.
- **Stay on Target:** Opposed Piloting vs one target; success = target −1 momentum; raise = you +1 momentum.
- **I Have You Now:** Requires **+2 momentum**. Opposed Piloting vs one target; success = +2 Gunnery vs that target, −2 momentum; raise = +2 Gunnery, no momentum loss; failure = −4 momentum.
- **I Can Hold It:** Steady flight. **Shaken:** must declare (clears Shaken). **Optional:** reset **momentum** to **0**.
- **Boost:** Piloting TN 4; success = +2 momentum; raise = **another** initiative card, **choose** (order, advantage, range); re-sort if needed.
- **I Know a Few Maneuvers:** Piloting TN 4; success = **another** card + **choose**; **raise** = **+1 card per raise**, then **choose**; **no momentum** change.
- **Loop:** Opposed Piloting vs one ship with **higher card**; both add **−(Size − Handling)**. Success = reverse advantage on them + +1 momentum; raise = **−1** to ships **targeting you** **until your next Maneuver**; crit fail = −2 momentum.

**4. Gunnery** — *Who: Gunners (initiative order)*

- Systems Op: declare shield facing (if directional) — start of Gunnery.
- **Advantage:** all weapons that bear; each weapon system may pick a different target.
- **No advantage:** **turret** weapons only, −2 Shooting.
- To hit: TN 4; modifiers stack (e.g. Evade −2 + medium −2 = −4).
- **Snapfire** (torpedoes/missiles): −2 unless target at short range.
- Damage: shields first; overflow vs **Toughness** → Shaken / **hull damage** on track (Damaged −1, Crippled −2, destroyed at Hull max)—guide §4.
- **Complications:** a ship **takes hull damage** when a hit **deals damage** (shields **and/or** hull track)—roll **2d6** for **that ship** (usually now; Phase 6 = follow-up). **Misses** don’t trigger. See guide **§4** and **§5**.

**5. Systems** — *Who: Engineer, Systems Operator*

- Engineer: Repair subsystem (offline → online); raise may remove 1 hull damage / Shaken (guide).
- Systems Op: **Electronics** — shield regen (5% max, +5% per raise).
- Systems Op: **Jamming** — Electronics opposed → −2 enemy attacks / sensor locks (guide).

**6. Complications** — *Who: GM (players react)*

- Resolve **follow-up** from **hull damage** complications this round (not from initiative suits).
- **Major system failure** or **subsystem offline** → roll **1d6** on Ship Systems Chart.
- Engineer **Reinforce** / Systems Op **Diagnose** when the result calls for it (guide §5).
- **End of round (after Complications):** **Break away (sublight)** if your card beat **all** enemies’ **this round** **and** your **Top Speed** > **each** enemy’s; or hyperjump / GM call-off / optional die after round 5 (guide **Combat End**).

---

## Role Quick Reference: "What Can I Do?"

### Pilot


| Phase           | Action                                                                                |
| --------------- | ------------------------------------------------------------------------------------- |
| 1 Initiative    | **Draw one card** — your initiative card (no Piloting roll)                             |
| 2 Support       | —                                                                                     |
| 3 Maneuver      | **Choose maneuver** — Evade, Stay on Target, I Have You Now, I Can Hold It, Boost, I Know a Few Maneuvers, Loop |
| 4 Gunnery       | — (unless also Gunner)                                                                |
| 5 Systems       | —                                                                                     |
| 6 Complications | **End of round:** may **break away** if eligible (see Combat End)                    |


### Gunner


| Phase           | Action                                                                  |
| --------------- | ----------------------------------------------------------------------- |
| 1 Initiative    | —                                                                       |
| 2 Support       | — (unless Co-pilot spots for you)                                       |
| 3 Maneuver      | —                                                                       |
| 4 Gunnery       | **Fire weapons** — all if advantage, turrets only at -2 if no advantage |
| 5 Systems       | —                                                                       |
| 6 Complications | —                                                                       |


### Engineer


| Phase           | Action                                                           |
| --------------- | ---------------------------------------------------------------- |
| 1 Initiative    | —                                                                |
| 2 Support       | **Support Pilot** (Repair or Knowledge: Eng) — +1/+2 to Piloting |
| 3 Maneuver      | —                                                                |
| 4 Gunnery       | —                                                                |
| 5 Systems       | **Repair** subsystem (bring offline system back)                |
| 6 Complications | **Reinforce** (when complication calls for it; same modifier as Pilot; success = avoid failure) |


### Co-pilot / Commander


| Phase           | Action                                                             |
| --------------- | ------------------------------------------------------------------ |
| 1 Initiative    | —                                                                  |
| 2 Support       | **Tactical assessment** (Smarts/Battle), **Support Pilot**, or **Spot for Gunner** (pick one Support action) |
| 3 Maneuver      | —                                                                  |
| 4 Gunnery       | **Call out targets** (Battle or Smarts) — first Gunner to hit designated target +1 (once/round) |
| 5 Systems       | —                                                                  |
| 6 Complications | —                                                                  |

*Co-pilot: **Call out targets** may be used in **any** phase (guide §5).*

### Systems Operator


| Phase           | Action                                                       |
| --------------- | ------------------------------------------------------------ |
| 1 Initiative    | —                                                            |
| 2 Support       | **Sensor lock** (Electronics/Notice) — +1/+2 to one Gunner   |
| 3 Maneuver      | —                                                            |
| 4 Gunnery       | **Declare shield facing** (before firing, if directional)    |
| 5 Systems       | **Activate shield regen** (Electronics) or **Jamming**       |
| 6 Complications | **Diagnose** (Electronics/Repair) when needed — +1 to Engineer |


---

## Key Tables

**Range (from initiative card)**


| Card        | Range   | Modifier |
| ----------- | ------- | -------- |
| 2           | No shot | —        |
| 3–7         | Long    | -4       |
| 8–Jack      | Medium  | -2       |
| Queen–Joker | Short   | 0        |


**Complications (2d6 on hull damage)** — Pilot roll −X = Piloting TN 4 at that modifier; Engineer **Reinforce** / Systems **Diagnose** per guide §5. Major failure or subsystem offline → also **1d6** Ship Systems Chart.


| 2d6  | Effect                                                                 |
| ---- | ---------------------------------------------------------------------- |
| 2    | **Disaster:** Piloting −4; fail = **major system failure** (roll 1d6)   |
| 3–5  | **Distraction:** lose all momentum                                     |
| 6–8  | **Flight deck ionization:** 10 stun to random crew                     |
| 9–11 | **Complication:** Pilot −2; fail = **subsystem offline** (roll 1d6)    |
| 12   | **Major:** Pilot −4; fail = **subsystem offline** (roll 1d6)          |


**Ship Systems Chart (1d6)** — Match columns to **major system failure** vs **subsystem offline** (guide §5).


| d6  | System              | Major system failure (summary)              | Subsystem offline (summary)                |
| --- | ------------------- | ------------------------------------------- | ----------------------------------------- |
| 1   | Sublight Engines    | Engines offline; speed 0 until repaired     | Thrusters damaged; Handling −1            |
| 2   | Nav Computer        | Hyperdrive offline; cannot jump             | Nav glitch; Astrogation delayed           |
| 3   | Deflector Shields   | Shields fully down; 0 until repaired        | Flickering; no shield regen until repair  |
| 4   | Weapons             | All weapons offline                         | One bank/turret offline                   |
| 5   | Life Support        | Breach / critical; −2 all checks            | Environmental glitch; −1 one crew check   |
| 6   | Sensors / Comms     | Blind / dead comms; −4 Shooting             | Targeting/sensors; −2 Shooting            |


**Combat end (guide §5):** **Break away (sublight)** — end of round after Complications; card higher than **every** enemy **this round** **and** **Top Speed** > **each** enemy’s. **Hyperjump** (Nav Computer, Astrogation). GM call-off. Optional: after round 5, GM rolls each round — **odd** = end, **even** = continue.