# Savage Worlds + Star Wars Ship Combat Guide

A combined reference for running starship combat using Savage Worlds Adventure Edition (SWADE) with Star Wars flavor. It consolidates SWADE core ideas, community variants, and the Star Wars Companion into one practical guide.

---

## 1. Savage Worlds Ship Combat Overview

SWADE does **not** include dedicated naval or starship combat rules in the core book. This guide uses an **initiative-card-based system** (not SWADE's chase track):

- **Initiative cards** for turn order, advantage, and range
- **Maneuvers** that add or subtract momentum (persists round to round)
- **Ship stats** (Handling, Speed, Toughness, Crew)

### Official Resources


| Resource                       | What It Covers                                                 |
| ------------------------------ | -------------------------------------------------------------- |
| SWADE Core Rules               | Maneuver names; damage, Traits, Bennies                        |
| Ship stats source              | Size, Handling, Top Speed, Toughness, Crew, era-based examples |
| Chase Examples PDF             | Illustrated chase examples                                     |
| Combat & Chase Quick Reference | Two-page summary of all maneuvers                              |


---

## 2. Initiative-Card Combat System

Combat uses **initiative cards** for turn order, advantage, and range. Each round, each ship draws **one** initiative card. The higher card acts first and has **advantage** over lower cards. Card rank sets **range** when firing: 2 = no shot; 3–7 = long (−4); 8–Jack = medium (−2); Queen–Joker = short (0).

Maneuvers grant **momentum** (see below).

### Handling advantage (momentum)

Compare each ship’s **Handling** (the ship stat modifier from ship stats) to **opposing ships** at the start of combat. Count how many opponents have **strictly lower** Handling than yours.

- **+1 momentum** each round if your Handling is **higher than a strict majority** of opposing ships (e.g., higher than more than half of them).
- **+2 momentum** each round instead if you also meet the **+1** condition **and** your Handling is **at least 3 points higher** than the **highest** opposing ship’s Handling.

This bonus is **handling advantage** (agility in the fight), not raw speed. It applies to **maneuver-phase** Piloting checks (e.g., Evade, Boost, I Know a Few Maneuvers) and all **opposed** Piloting rolls. Ships that do not beat a strict majority on Handling get **no** bonus from this rule.

**Momentum (brief):** Starts at 0, persists round to round; **handling advantage** and maneuvers change it. Full rules: **Momentum** under Hull (§4).

### Maneuvers

Each round during the Maneuver phase, the Pilot chooses one maneuver. **Momentum** gained or lost persists.


| Maneuver           | Effect                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Evade**          | Piloting check (TN 4), -1 per opposing ship. Success: -2 to opponents targeting this ship. Raise: negates Stay on Target vs this ship this round.                                                                        |
| **Stay on Target** | Opposed Piloting vs one target. Success = target -1 momentum. Raise = +1 momentum.                                                                                                                                       |
| **I Have You Now** | Requires 2 or more momentum. Opposed Piloting vs one target. Success = +2 Gunnery vs target, -2 momentum. Raise = +2 Gunnery, no momentum loss. Failure = -4 momentum.                                                   |
| **I Can Hold It**  | Steady flight. Shaken ships: must declare it (clears Shaken). **Optional:** reset **momentum** to **0**.                                                                                                                  |
| **Boost**          | Piloting check (TN 4). Success = +2 momentum. Raise = draw another initiative card and choose which card applies (order, advantage, range).                                                                              |
| **I Know a Few Maneuvers** | Piloting check (TN 4). Success = draw **another** initiative card and **choose** which card applies (order, advantage, range). **Raise:** draw **one additional card per raise**, then **choose** which card applies (same as success, with a larger pool). |
| **Loop**           | Opposed Piloting vs one target (higher card). Both add -(Size - Handling). Success = reverse advantage, +1 momentum. Raise = −1 to ships targeting you (until your next Maneuver). Crit fail = -2 momentum. |


### Maneuver Effects (Detailed)

**Evade**

- **Effect:** Defensive posture. **Piloting** check (TN 4). Modifier: **-1 per opposing ship** to the roll.
- **Success:** Until your next Maneuver phase: **-2 to opponents targeting this ship** (incoming targeting).
- **Raise:** **This ship negates Stay on Target maneuvers this round** (any Stay on Target vs this ship has no effect).
- **Failure:** No effect.
- **Next round:** No modifier.

**Stay on Target**

- **Effect:** Apply pressure to one target. Make an **opposed Piloting** roll vs that ship's Pilot.
- **Success:** Target **-1 momentum** (you're staying on their tail).
- **Raise:** **You** get **+1 momentum**.
- **Failure:** No effect.

**I Have You Now**

- **Prerequisite:** You must have **+2 or more momentum** (you're on their tail).
- **Effect:** Line up the kill shot. Make an **opposed Piloting** roll vs one declared target.
- **Success:** **+2 to your Gunnery** vs that target this round. **-2 momentum** (you committed to the shot).
- **Raise:** **+2 to your Gunnery** vs that target this round. **No momentum loss** (perfect setup).
- **Failure:** No bonus. **-4 momentum** (you overcommitted and lost position).
- **Next round:** Momentum changes persist.

**I Can Hold It**

- **Effect:** Steady flight.
- **Shaken ships:** A Shaken ship clears Shaken by declaring **I Can Hold It** as its maneuver; it may take no other maneuver that round.
- **Optional:** When you declare **I Can Hold It**, you may **reset momentum to 0** (stable line—give up accumulated position energy).
- **Roll:** None.
- **Next round:** No modifier.

**Boost**

- **Effect:** Push engines for advantage. **Piloting** check (TN 4).
- **Success:** **+2 momentum**.
- **Raise:** Draw **another** initiative card, then **choose** which of your initiative cards applies for **turn order, advantage, and range** for the rest of the round (including Gunnery). Re-sort acting order among ships if needed.
- **Failure:** No bonus.

**I Know a Few Maneuvers**

- **Effect:** Veteran flying—re-sequence off the initial draw. **Piloting** check (TN 4).
- **Success:** Draw **one** additional initiative card, then **choose** which of **your** initiative cards applies for **turn order, advantage, and range** for the rest of the round (including Gunnery). Re-sort acting order among ships if needed.
- **Raise:** Draw **one additional initiative card per raise** (each raise adds another card to your pool). When finished drawing, **choose** which **one** card applies for the round (same as success—order, advantage, range). **No momentum** gain or loss.
- **Failure:** No effect.

**Loop**

- **Effect:** Reverse onto a pursuer's tail. **Opposed Piloting** vs one ship that had a **higher card than you** this round. **Both combatants** add **-(Size - Handling)** to their roll (each uses their own ship's Size and Handling; e.g., Size 8 Handling +1 = -7).
- **Success (you win):** For **Gunnery this round**, you have **advantage over them** (you reversed onto their six). Also **+1 momentum**.
- **Raise:** Until your next Maneuver phase, **−1** to attack rolls from **any ship targeting you** (Gunnery, etc.).
- **Failure:** No effect. Critical Failure: **-2 momentum** (disoriented).

### Range (from Initiative Card)


| Card        | Range   | Modifier |
| ----------- | ------- | -------- |
| 2           | No shot | —        |
| 3-7         | Long    | -4       |
| 8-Jack      | Medium  | -2       |
| Queen-Joker | Short   | 0        |


**Complications:** Trigger when a ship **takes hull damage** from a hit (see **Hull and destruction** in §4)—**not** on initiative suits. Roll **2d6** for the **ship that was hit** when the damage lands; use **Phase 6** for Reinforce, Diagnose, and other follow-up, then **end-of-round** steps (e.g. break away). **Misses** (and narratively “no impact” hits, at GM discretion) do not trigger a roll. Full table and effects: **Complications (2d6 on hull damage)** in §5.

**Joker (initiative):** Acts first regardless of rank; **+2 to all crew rolls** that round; counts as **short range** (0) for attacks.

---

## 3. Ship Stats

Typical ship stat block:


| Stat          | Purpose                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| **Size**      | Affects Toughness, Crew; large ships are harder to maneuver                        |
| **Handling**  | Modifier on Piloting rolls; handling advantage vs opponents (+1 or +2 momentum each round); with Size, each ship’s Loop modifier is −(Size − Handling) |
| **Top Speed** | Movement rate; in space often scaled up                                            |
| **Toughness** | Damage soak; often Size + Armor                                                    |
| **Shields**   | Maximum shield value (e.g., 60, 80, 120); omit if ship has no deflectors           |
| **Hull**      | Maximum hull damage before destruction; typically 3 for fighters, 4 for freighters |
| **Crew**      | Minimum crew; gunners, pilots, engineers                                           |
| **Climb**     | Used for atmospheric flight                                                        |


---

## 4. Star Wars Savage Worlds Combat

### Shields

Ships with deflector shields absorb damage before it reaches the hull. Shield strength and regeneration are managed during the Systems phase.

**Shield pool**

- Each ship with shields has a maximum shield value (e.g., 60, 80, 120). This is listed in the ship stat block (see Ship Stats).
- Damage is applied to shields first. Only damage that exceeds the current shield total reaches the hull and is rolled against Toughness for Shaken and hull damage.
- Track current shields separately from **hull damage** marked on the hull track. When shields reach 0, further damage goes directly to the hull.

**Regeneration**

- During the **Systems phase**, the Systems Operator (or crewmember managing shields) may attempt an **Electronics** check to activate shield regeneration.
- **Success:** Recover 5% of the ship's maximum shields (rounded down). E.g., 80 max = 4 recovered.
- **Raise:** +5% per raise (10% for one raise, 15% for two raises, etc.). E.g., 80 max with one raise = 8 recovered.
- Regeneration applies only if the shield generators are online and the ship has not suffered a shield-related complication.
- Regeneration cannot exceed the ship's maximum shield value.

**Weapon interaction**

- **Lasers and cannons:** Full damage to shields. Common tactics use laser fire to strip shields before committing torpedoes.
- **Torpedoes and missiles:** Half damage to shields. These weapons are powerful against hull but less efficient for burning down shields.

**Directional shields (optional)**

- Some ships (freighters, capital vessels) have directional shields with separate arcs: forward, aft, port, starboard.
- The Systems Operator declares shield facing at the start of the Gunnery phase.
- Damage from an attack applies to the arc that faces the attacker. If that arc is depleted, excess damage may spill to adjacent arcs or the hull (GM's discretion).
- During the Systems phase, the Systems Operator may **rebalance** shields: shift points from one arc to another. Rebalancing does not create new shield points; it only moves existing points between arcs.

**Ships without shields**

- Fighters such as the TIE/LN have no deflector shields. All damage goes directly to hull Toughness.

### Hull and Destruction

Each ship has a **Hull** value (see ships.json: typically 3 for fighters, 4 for freighters, more for capital ships). Hull is how much **hull damage** the ship can take before destruction.

**Taking hull damage (from hits):** A ship **takes hull damage** from an attack whenever that attack **deals damage** to the ship—whether the damage is **absorbed by shields**, applied as **hull damage** on the track (below), or both. **Complications** (§5): each time a ship **takes hull damage** this way, roll **2d6** on the Complications table for **that ship**. Shield-only hits count; **misses** do not (unless the GM rules otherwise).

**Resolving hull damage**

When damage exceeds shields (or the ship has no shields), compare the damage to the ship's Toughness:

- **Damage > Toughness:** Ship is Shaken. If the ship was already Shaken, it instead takes **1 hull damage**.
- **For every 4 over Toughness, add 1 hull damage** (ship is also Shaken): 4+ over = 1 hull, 8+ over = 2 hull, 12+ over = 3 hull, and so on.

**Shaken (effects)**

- **Momentum:** A ship that becomes Shaken loses all momentum.
- **Weapons:** A Shaken ship may still fire (Gunnery phase); gunners act normally.
- **Maneuver:** A Shaken ship must declare **I Can Hold It** as its maneuver; it may take no other maneuver that round. Declaring I Can Hold It clears Shaken. **I Can Hold It** may **optionally** reset **momentum** to **0** (see maneuver table).

**Hull damage penalties**


| Hull damage | Effect                                     |
| ----------- | ------------------------------------------ |
| 1           | **Damaged** = -1 to all ship checks        |
| 2+          | **Crippled** = -2 to all ship checks       |
| Hull max    | **Destroyed** = ship disabled or destroyed |


When hull damage equals the ship's Hull value, the ship is **destroyed** (or disabled; GM's choice). Crew may eject or attempt emergency repairs between combats.

### Momentum

**Momentum** tracks how well a ship's combat is going. Each ship starts combat with **zero momentum**; momentum **persists from round to round**. **Handling advantage** and maneuvers add or subtract momentum (Stay on Target, Boost, Loop, I Have You Now). **Lose all momentum** when: Distraction complication, or **the ship becomes Shaken**.

All **Piloting** rolls **add** (or **subtract**) the ship’s **current momentum** to the roll.

---

## 5. Rules of Play

This chapter is the **playing the round** reference: turn order, crew jobs, complications, and combat end. It matches the **initiative-card** system above (not the SWADE chase track).

### Unified Round Sequence

Combat proceeds in rounds. Each round follows this order:


| Phase                     | Who Acts                                        | What Happens                                                                                                                                                                |
| ------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Initiative**         | All ships                                       | Each ship draws **one** initiative card. **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add cards during Maneuvers—see §2. Higher card acts first and has *advantage* vs lower cards.       |
| **2. Support (optional)** | Co-pilot, Commander, Engineer, Systems Operator | Optional **trait rolls** (Notice, Repair, Electronics, Smarts/Battle, etc.) to aid the Pilot’s **maneuver** checks or Gunners’ **Shooting**—**before** the Maneuver phase. See **Player Jobs**. |
| **3. Maneuver**           | Pilot                                           | Evade, Stay on Target, I Have You Now, I Can Hold It, Boost, I Know a Few Maneuvers, Loop — see maneuver table in §2                                                        |
| **4. Gunnery**            | Gunners                                         | Fire weapons (advantage, range). **Hull damage → Complication 2d6** for the ship that was hit (resolve now or note for Phase 6).                                             |
| **5. Systems**            | Engineer, Systems Operator                      | Repair, shield regen (Electronics check), sensor locks                                                                                                                      |
| **6. Complications**      | GM                                              | Resolve **complication follow-up** from damage this round (Reinforce, Diagnose, lingering effects). **End of round:** qualifying ships may **break away** (see Combat End). |


**Initiative vs Support vs Maneuver:** Phase **1** is **initiative cards** for each ship—order, advantage, and range (no **Pilot** Piloting roll for initiative; extra cards from **Boost** raise or **I Know a Few Maneuvers** happen in Phase **3**). Phase **2** is **Support**: optional **trait rolls** by crew who have that role—**before** the Pilot’s maneuver (aid Piloting, Shooting, or tactical rerolls). Phase **3** is the Pilot’s **maneuver** (Piloting rolls as required by the chosen maneuver).

---

### Player Jobs

Each crew role has specific responsibilities. A character may fill multiple roles on small ships (e.g., X-wing: pilot + gunner); larger ships (freighters, capital vessels) assign one role per character when possible.

---

#### Pilot

**Your job:** Fly the ship, gain advantage, and set up shots for the gunners.


| When               | Action                | Skill    | Effect                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | --------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Initiative**     | —                     | —        | Draw **one** initiative card (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises): extra card(s) and choice—see §2.                                                                                                                                                                                                                                                                                         |
| **Maneuver phase** | Choose maneuver       | Piloting | Evade (-1 per opponent; success = -2 incoming targeting; raise = negates Stay on Target), Stay on Target (target -1 momentum; raise = you +1 momentum), I Have You Now (req. +2 momentum; opposed; +2 Gunnery vs target; success -2 mom, raise no loss, fail -4 mom), I Can Hold It, Boost (+2 momentum; raise = extra card + choose), I Know a Few Maneuvers (Piloting TN 4; success/raises = extra card(s) + choose, no momentum), Loop (opposed vs target; both apply -(Size-Handling); raise = −1 to ships targeting you until your next Maneuver) |
| **All rounds**     | Handling advantage    | —        | Higher Handling than a strict majority of opponents = +1 momentum; if also ≥ highest enemy Handling + 3, +2 instead                                                                                                                                                                                                                                                                                                                      |
| **End of round**   | Break away (optional) | —        | After Complications: if your initiative **card** beat **all** enemies’ **this round** and your **Top Speed** exceeds **each** enemy’s, you may declare sublight disengagement (see **Combat End**).                                                                                                                                                                                                                                      |


**Key modifiers to your Piloting check:** Ship Handling (stat on the sheet), ship hull/Shaken, terrain/asteroids (−2).

**Edges that help:** Ace, Steady Hands, Quick, Level-Headed.

---

#### Gunner

**Your job:** Fire the ship's weapons when you have a shot. Your effectiveness depends on the Pilot earning advantage.


| When                  | Action              | Skill    | Effect                                                                                                 |
| --------------------- | ------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| **Gunnery phase**     | Fire weapons        | Shooting | TN 4. Modifiers stack (range, target Evading -2, etc.); apply to roll.                                 |
| **With advantage**    | Fire all weapons    | Shooting | May use fixed and turret weapons that bear on target. Each weapon system can target a different enemy. |
| **Without advantage** | Return fire only    | Shooting | Turret weapons only; -2 to Shooting                                                                    |
| **Snapfire weapons**  | Torpedoes, missiles | Shooting | -2 unless target at short range                                                                        |


**Range (from initiative card):** 2 = no shot; 3–7 = long (-4); 8–Jack = medium (-2); Queen–Joker = short (0).

**To hit:** Base TN 4. Modifiers apply to your Shooting roll and stack (e.g., target Evading -2 + medium range -2 = -4). Roll + modifiers vs TN 4.

**Edges that help:** Ace Gunner, Steady Hands, Marksman.

---

#### Engineer

**Your job:** Keep systems online and repair damage during combat.


| When                                     | Action                   | Skill  | Effect                                                                                                                                                                                    |
| ---------------------------------------- | ------------------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Systems phase**                        | Repair subsystem         | Repair | Success = bring one offline system back online. Raise = back online + remove 1 hull damage/shaken                                                                                         |
| **When complication threatens a system** | Reinforce failing system | Repair | When a Complication result calls for it: Repair check (TN 4) with same modifier as Pilot (Disaster -4, Major -4, Complication -2). Success = avoid system failure before 1d6 system roll. |
| **Between rounds**                       | Emergency patch          | Repair | Restore limited function to heavily damaged system (GM discretion)                                                                                                                        |


**Engineer Support:** Before the Pilot's check, an Engineer can use **Support** (Repair or Knowledge: Engineering): success = +1 to Pilot's Piloting check; raise = +2.

**Edges that help:** McGyver, Ace (if piloting backup), Mr. Fix It.

---

#### Co-pilot / Commander

**Your job:** Coordinate the crew, spot threats, and support the Pilot.


| When                 | Action              | Skill                                 | Effect                                                                                                  |
| -------------------- | ------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Support phase**    | Support Pilot       | Common Knowledge, Notice, or Piloting | Success = +1 to Pilot's Piloting check. Raise = +2                                                      |
| **Support phase**    | Spot for Gunner     | Notice                                | Success = +1 to one Gunner's Shooting. Raise = +2                                                       |
| **Support phase**    | Tactical assessment | Smarts or Battle                      | Success = one crewmember may reroll one failed check this round. Raise = reroll + ignore one -2 penalty |
| **Any phase**        | Call out targets    | Battle or Smarts                      | Designate primary target; first Gunner to hit that target gets +1 (once per round)                      |


**Small ships:** The co-pilot often doubles as a Gunner or Systems Operator. One Support action per round.

**Edges that help:** Command, Tactician, Level-Headed.

---

#### Systems Operator

**Your job:** Manage shields, sensors, and communications. Optional on small craft; essential on larger ships.


| When                                     | Action                    | Skill                 | Effect                                                                                  |
| ---------------------------------------- | ------------------------- | --------------------- | --------------------------------------------------------------------------------------- |
| **Systems phase**                        | Activate shield regen     | Electronics           | Success = 5% of max shields. +5% per raise. See Shields section.                        |
| **Support phase**                        | Sensor lock               | Electronics or Notice | Success = +1 to one Gunner's Shooting vs designated target. Raise = +2                  |
| **Systems phase**                        | Jamming / countermeasures | Electronics           | Opposed vs enemy Electronics or Piloting; success = -2 to enemy attacks or sensor locks |
| **When complication threatens a system** | Diagnose                  | Electronics or Repair | Identify failing system; success = Engineer gets +1 to Repair that system               |


**Shields:** Declare shield facing at start of Gunnery phase. See Shields section for absorption, regeneration, and directional rules.

**Edges that help:** McGyver, Ace (Electronics).

---

### Crew Size Variants


| Ship Type                             | Crew | Role Mapping                                                                                            |
| ------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------- |
| **Fighter** (X-wing, TIE)             | 1    | Pilot = Gunner. No Engineer/Commander/Systems.                                                          |
| **Heavy fighter** (Y-wing)            | 2    | Pilot + Gunner, or Pilot + Systems (rear gun)                                                           |
| **Freighter** (YT-1300, Falcon-style) | 4    | Pilot, Co-pilot, Gunner, Engineer (typical). Engineer or Co-pilot often handles Systems (shield regen). |
| **Corvette / capital**                | 5+   | One per role; may have multiple Gunners, Engineers                                                      |


**Combining roles:** A character filling two roles gets one action per role per round, but may not use the same skill twice for Support (e.g., cannot Support Pilot twice with Notice). Multiple Support actions for the same beneficiary do stack from different crew (Pilot can receive +1 from Co-pilot and +1 from Engineer).

---

### Round Summary (Quick Reference)

1. **Initiative**: Each ship draws **one** card (no Piloting roll); compare for order, advantage, and range.
2. **Support** (optional): Trait rolls to aid Pilot (before maneuvers) or Gunners—see **Player Jobs**.
3. **Maneuver**: Pilot chooses Evade, Stay on Target, I Have You Now, I Can Hold It, Boost, I Know a Few Maneuvers, or Loop.
4. **Gunnery**: Gunners fire; each **ship that takes hull damage** (see §4) rolls **Complications (2d6)**.
5. **Systems**: Engineer repairs; Systems Operator activates shield regen (Electronics), sensor locks.
6. **Complications**: Resolve complication **follow-up** from damage taken this round (Reinforce, Diagnose, etc.).
7. **End of round:** Any ship that meets the **Break away (sublight)** conditions may declare it is leaving (see **Combat End**).

---

### Advantage and Firing (Reference)

- **With advantage** (higher initiative card): May fire all weapons that can bear on target(s). Each weapon system may engage a different target.
- **Without advantage**: Can return fire with **turret weapons only**, -2 to Shooting.
- **To hit:** TN 4. Modifiers stack (range, target Evading -2, etc.); apply total to your Shooting roll.
- **Range table:** 2 = no attack; 3-7 = long (-4); 8-Jack = medium (-2); Queen-Joker = short (0).
- **Snapfire** (torpedoes): -2 unless target at short range.
- **Complications:** Each time a ship **takes hull damage** from a successful attack, roll **2d6** on the Complications table **for the ship that was hit** (see below; **§4** defines *takes hull damage*).

### Complications (2d6 on hull damage)

Each time a ship **takes hull damage** from a hit, roll **2d6 once** for **that ship** (see §2 for misses / timing; **§4** for what counts as hull damage).

**Pilot roll -X:** Piloting (TN 4) at that modifier; fail = subsystem offline (or major system failure on Disaster). **Engineer Reinforce:** Repair (TN 4), same modifier; success = avoid that failure before the 1d6 system roll. **Major system failure** or **subsystem offline** → roll 1d6 on **Ship Systems Chart**.


| 2d6  | Effect                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------- |
| 2    | **Disaster:** Piloting -4; fail = **major system failure** (roll 1d6 on Ship Systems Chart)    |
| 3-5  | **Distraction:** Ship loses all momentum                                                       |
| 6-8  | **Flight deck ionization:** 10 stun damage to a random crew member                             |
| 9-11 | **Complication:** Pilot roll -2; fail = **subsystem offline** (roll 1d6 on Ship Systems Chart) |
| 12   | **Major:** Pilot roll -4; fail = **subsystem offline** (roll 1d6 on Ship Systems Chart)        |


#### Ship Systems Chart

Roll 1d6 to determine which system is affected. Apply the effect from the appropriate column based on whether the complication was a **major system failure** or **subsystem offline**.


| d6  | System                | Major System Failure (full failure)                                                                                     | Subsystem Offline (partial failure)                                       |
| --- | --------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1   | **Sublight Engines**  | Engines offline. No movement; speed = 0 until repaired.                                                                 | Maneuvering thrusters damaged. Handling -1 until repaired.                |
| 2   | **Nav Computer**      | Hyperdrive offline. Cannot jump to hyperspace until repaired. Any Astrogation calculations are lost.                    | Nav computer glitch. Astrogation checks are delayed until repaired.       |
| 3   | **Deflector Shields** | Shields fully down. All shield points lost; no absorption until repaired. Repaired shields come back at 0 strength.     | Shield flickering. No shield regen until Systems phase repair.            |
| 4   | **Weapons**           | All weapons offline. Cannot fire until repaired.                                                                        | One weapon bank or turret offline. Reduce available weapons.              |
| 5   | **Life Support**      | Life support failure. Hull breach, atmosphere leak, or critical failure. Crew at risk; -2 to all checks until repaired. | Environmental glitch. -1 to one crew role's check this round (GM choice). |
| 6   | **Sensors / Comms**   | Sensors blind, comms dead. -4 to Shooting; cannot communicate externally.                                               | Targeting computer or sensor array offline. -2 Shooting until repaired.   |


### Combat End

Combat may end in several ways:

- **Voluntary escape:** A ship may attempt to **hyperjump** away (requires Nav Computer online; Astrogation check as usual). Success = ship escapes; combat ends for that ship. Pursuers may give chase (GM's discretion) or break off.
- **Break away (sublight):** At the **end of the round**—after **Complications** (and any other end-of-round cleanup)—a ship may declare it is **flying away** and **ending the engagement** if **both** are true, judged using **this round’s** initiative cards (drawn at the start of the round) and ship stats: (1) its initiative **card rank** is **higher than every opposing ship’s** card (Joker counts highest; on a **tie** at the same rank with any enemy, this option does not apply unless the GM rules otherwise), and (2) its **Top Speed** (from ship stats) is **greater than each opposing ship’s Top Speed**. No roll is required unless the GM adds one. Remaining ships may keep fighting or the GM may close the scene.
- **GM call-off:** The GM may **narratively call off the pursuit** at any time—e.g., reinforcements arrive, terrain interferes, the chase is no longer dramatic.
- **Random roll (optional):** After round 5, GM may roll a die each round: **odd** = combat ends (break off or escape); **even** = continues.

---

## 6. How It Works in Play: Example Flow

**Setup:** A Rebel X-wing vs two TIE fighters.

1. **Round 1**
  - All draw for initiative. X-wing draws **10**; TIEs draw **7** and **3** (one card each).
  - X-wing has advantage over both TIEs. TIE 1 has advantage over TIE 2.
  - **Maneuver:** X-wing lines up shots; TIEs jockey for position (Boost, Stay on Target, etc. as chosen).
  - X-wing fires all forward lasers at TIE 1 (medium range, -2).
  - TIEs: Without advantage, may only use turret-like weapons (or rear weapons if applicable) at -2.
  - Resolve damage, apply hull damage/shaken as usual.
2. **Round 2**
  - Example: TIE 2 is **hit** and loses shields—roll **Complications** for TIE 2 (e.g. **Distraction**: lose all momentum).
  - Maneuvers from R1 still apply (e.g. TIE 1 **Boost** success → +2 momentum).
  - Repeat initiative, maneuvers, advantage, and firing.
3. **Round 5+**
  - GM rolls: 5 = odd—combat ends. X-wing escapes; TIEs break off.

---

## 7. Quick Reference: Modifiers


| Modifier                                                               | Value                        |
| ---------------------------------------------------------------------- | ---------------------------- |
| Base TN (ship attacks)                                                 | 4                            |
| Handling advantage (higher Handling than strict majority of opponents) | +1 momentum                  |
| Handling advantage (also ≥ highest enemy Handling + 3)                 | +2 momentum instead          |
| Climb advantage (atmosphere)                                           | +2                           |
| Harsh terrain (debris, asteroids)                                      | -2                           |
| Ship hull damaged / Shaken (see Hull)                                  | -1 or -2                     |
| Lose all momentum                                                      | Distraction, becoming Shaken |
| Without advantage (return fire)                                        | -2 Shooting                  |
| Long range                                                             | -4                           |
| Medium range                                                           | -2                           |
| Evade: target Evading (incoming targeting)                             | -2 to hit that target        |
| Loop raise: defender Looped with raise                                 | −1 to hit that ship          |
| I Have You Now: you succeeded (vs declared target)                     | +2 to hit that target        |
| Unstable platform (firing from moving ship)                            | -2 (often negated by Edges)  |


---

## 8. Star Wars Companion Integration

For full Star Wars flavor, use the **Star Wars: Savage Worlds Companion**:

1. **Ship stats**:  X-wings, TIEs, freighters, etc., with Handling, Speed, Armor, Weapons.
2. **Shields:** Ablative or directional; see Shields section for absorption and regeneration.
3. **Ion weapons**: Disable systems rather than destroy hull; follow Companion ion rules.
4. **Edges**: Ace, Ace Gunner, Steady Hands, etc., for pilots and gunners.

Apply these on top of the initiative-card and ship rules above for Star Wars starship battles.

---

## 9. Summary


| Layer             | Source                           | Use                                                           |
| ----------------- | -------------------------------- | ------------------------------------------------------------- |
| Initiative cards  | This guide                       | Turn order, advantage, range; maneuvers add/subtract momentum |
| Ship stats        | Ship sources / Star Wars content | Handling, Speed, Toughness, weapons                           |
| Combat flow       | This guide + SWADE               | Advantage, range, snapfire; complications on **hull damage**  |
| Star Wars content | Star Wars Companion              | Ships, weapons, shields, ion, Edges                           |


Result: abstract, fast ship combat that feels like Star Wars dogfights, driven by initiative cards, Piloting, advantage, and range—without needing a battle mat or detailed positioning.