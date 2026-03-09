# Savage Worlds + Star Wars Ship Combat Guide

A combined reference for running starship combat using Savage Worlds Adventure Edition (SWADE) with Star Wars flavor. The workspace `swad_shipcombat` was empty?this document consolidates the official Savage Worlds approach, community variants, and the Star Wars Companion into one practical guide.

---

## 1. Savage Worlds Ship Combat Overview

SWADE does **not** include dedicated naval or starship combat rules in the core book. This guide uses an **initiative-card-based system** (not SWADE's chase track):

- **Initiative cards** for turn order, advantage, and range
- **Maneuvers** that push modifiers to next round's Piloting
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

Combat uses **initiative cards** for both turn order and tactical position. Each round, ships draw cards; higher card = acts first and has **advantage** over lower cards. Your card rank also determines your **range band** when firing (2 = no shot; 3-7 = long; 8-Jack = medium; Queen-Joker = short).

There is no chase track. Maneuvers grant **modifiers that apply to next round's Piloting check** (or to an opponent's), affecting who keeps the better card.

### Maneuvers

Each round during the Maneuver phase, the Pilot chooses one maneuver. **Next-round modifiers** apply to the Piloting phase of the following round.


| Maneuver           | Effect                                                                           |
| ------------------ | -------------------------------------------------------------------------------- |
| **Evade**          | Piloting check (TN 4), -1 per opposing ship. Success: -2 incoming targeting, -2 outgoing targeting. Raise: -1 outgoing targeting. |
| **Stay on Target** | Opposed Piloting vs one target. Success = target -2 Piloting next round.         |
| **Hold Steady**    | Cancels Evade. +1 to your Piloting next round.                                   |
| **Boost**          | Piloting check (TN 4). Success = +2 Piloting next round.                         |
| **Loop**           | Piloting check (See note). Success = reverse advantage with one ship this round. |


### Maneuver Effects (Detailed)

**Evade**

- **Effect:** Defensive posture. **Piloting** check (TN 4). Modifier: **-1 per opposing ship** to the roll.
- **Success:** Until your next Maneuver phase: your incoming targeting suffers **-2** (ships targeting you); your outgoing targeting suffers **-2**.
- **Raise:** Same, but your outgoing targeting suffers **-1** only.
- **Failure:** No effect.
- **Next round:** No modifier.

**Stay on Target**

- **Effect:** Apply pressure to one target. Make an **opposed Piloting** roll vs that ship's Pilot.
- **Success:** Target suffers **-2 to Piloting** next round (you're staying on their tail).
- **Raise:** **You** get **+1 to Piloting** next round.
- **Failure:** No effect.

**Hold Steady**

- **Effect:** Steady flight. Cancels Evade (incoming targeting and outgoing targeting penalties).
- **Shaken ships:** A Shaken ship clears Shaken by declaring **Hold Steady** as its maneuver; it may take no other maneuver that round.
- **Roll:** None.
- **Next round:** **+1 to your Piloting** (stable, predictable).

**Boost**

- **Effect:** Push engines for advantage. **Piloting** check (TN 4).
- **Success:** **+2 to your Piloting** next round.
- **Raise:** +2 and **draw 1 extra card** next round (pick best of 3).
- **Failure:** No bonus. Critical Failure: **-2 Piloting** next round (overstressed engines).

**Loop**

- **Effect:** Reverse onto a pursuer's tail. **Piloting** check (See note). **Note:** Base TN 4; modifier **-(Size - Handling)** to the roll (e.g., Size 8, Handling +1 = -7).
- **Success:** Pick one ship that had a **higher card than you** this round. For **Gunnery this round**, you have **advantage over them** (you reversed onto their six). Also **+1 to your Piloting** next round.
- **Raise:** Same, plus **draw 1 extra card** next round.
- **Failure:** No effect. Critical Failure: **-2 Piloting** next round (disoriented).

### Tracking Modifiers

Pilots track modifiers between rounds: *"+2 Piloting next round"*, *"target -2"*, etc. These apply to the **Piloting phase** of the next round when choosing which initiative card to keep. Draw an extra card when a maneuver grants it; pick best of 3.

### Range (from Initiative Card)


| Card        | Range   | Modifier |
| ----------- | ------- | -------- |
| 2           | No shot | ?        |
| 3?7         | Long    | -4       |
| 8-Jack      | Medium  | -2       |
| Queen-Joker | Short   | 0        |


### Complications

- **Clubs** drawn for initiative trigger complications (Phase 7). Roll 2d6 on the Complications table.
- Suits on cards may provide terrain or situational modifiers at GM discretion.

**Joker (special)**

- When a ship draws the **Joker** for initiative: acts first regardless of card rank; **+2 to all crew rolls** that round (Piloting, Shooting, Repair, Electronics, etc.); counts as **short range** (0) when resolving attacks.

---

## 3. Ship Stats

Typical ship stat block:


| Stat          | Purpose                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| **Size**      | Affects Toughness, Crew; large ships are harder to maneuver                        |
| **Handling**  | Modifier to Piloting; nimble ships get +1 or +2                                    |
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
- Track current shields separately from hull damage. When shields reach 0, further damage goes directly to the hull.

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

Each ship has a **Hull** value (see ships.json: typically 3 for fighters, 4 for freighters, more for capital ships). Hull represents how many wounds the ship can absorb before destruction.

**Resolving hull damage**

When damage exceeds shields (or the ship has no shields), compare the damage to the ship's Toughness:

- **Damage ? Toughness:** Ship is Shaken. If the ship was already Shaken, it instead takes **1 hull damage**.
- **For every 4 over Toughness, add 1 hull damage** (ship is also Shaken): 4+ over = 1 hull, 8+ over = 2 hull, 12+ over = 3 hull, and so on.

**Shaken (effects)**

- **Weapons:** A Shaken ship may still fire (Gunnery phase); gunners act normally.
- **Maneuver:** A Shaken ship must declare **Hold Steady** as its maneuver; it may take no other maneuver that round. Declaring Hold Steady clears Shaken.

**Hull damage penalties**


| Hull damage | Effect                                     |
| ----------- | ------------------------------------------ |
| 1           | **Damaged** ? -1 to all ship checks        |
| 2+          | **Crippled** ? -2 to all ship checks       |
| Hull max    | **Destroyed** ? ship disabled or destroyed |


When hull damage equals the ship's Hull value, the ship is **destroyed** (or disabled; GM's choice). Crew may eject or attempt emergency repairs between combats.

---

## 5. Rules of Play

This chapter combines the SWADE chase rules, ship mechanics, and Star Wars elements into one unified starship combat system. It defines the round sequence and **each player's job** during combat.

### Unified Round Sequence

Combat proceeds in rounds. Each round follows this order:


| Phase                     | Who Acts                                        | What Happens                                                           |
| ------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------- |
| **1. Initiative**         | All ships                                       | Draw cards; higher card acts first and has *advantage* vs lower cards  |
| **2. Support (optional)** | Co-pilot, Commander, Engineer, Systems Operator | Aid other crew before their checks                                     |
| **3. Piloting**           | Pilot                                           | Piloting check (TN 4); determines which initiative card the ship keeps |
| **4. Maneuver**           | Pilot                                           | Evade, Stay on Target, Hold Steady, Boost, or Loop                     |
| **5. Gunnery**            | Gunners                                         | Fire weapons (based on advantage and range)                            |
| **6. Systems**            | Engineer, Systems Operator                      | Repair, shield regen (Electronics check), sensor locks                 |
| **7. Complications**      | GM                                              | Resolve Club cards and system failures                                 |


---

### Player Jobs

Each crew role has specific responsibilities. A character may fill multiple roles on small ships (e.g., X-wing: pilot + gunner); larger ships (freighters, capital vessels) assign one role per character when possible.

---

#### Pilot

**Your job:** Fly the ship, gain advantage, and set up shots for the gunners.


| When               | Action                | Skill    | Effect                                                                                                                                              |
| ------------------ | --------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Piloting phase** | Piloting check (TN 4) | Piloting | Success = keep highest of 2 initiative cards. Raise = draw another, pick best. Fail = must take lowest card.                                        |
| **Maneuver phase** | Choose maneuver       | ?        | Evade (Piloting -1 per opponent; success -2 incoming targeting/-2 outgoing targeting, raise -1 outgoing targeting), Stay on Target (target -2 next round), Hold Steady (+1), Boost (+2 Piloting next round), Loop (reverse advantage) |
| **All phases**     | Declare speed         | ?        | Higher speed than opponents = +2 to Piloting; 2? speed = +4                                                                                         |


**Key modifiers to your Piloting check:** Ship Handling, ship hull/shaken, ship agility test (ship trait roll: fail = -1, success = +1), speed advantage, terrain/asteroids (-2).

**Edges that help:** Ace, Steady Hands, Quick, Level-Headed.

---

#### Gunner

**Your job:** Fire the ship's weapons when you have a shot. Your effectiveness depends on the Pilot earning advantage.


| When                  | Action              | Skill    | Effect                                                                                                 |
| --------------------- | ------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| **Gunnery phase**     | Fire weapons        | Shooting | TN 4. Modifiers stack (range, target Evading -2, your Evade outgoing targeting -2 or -1 (raise), etc.); apply to roll.         |
| **With advantage**    | Fire all weapons    | Shooting | May use fixed and turret weapons that bear on target. Each weapon system can target a different enemy. |
| **Without advantage** | Return fire only    | Shooting | Turret weapons only; -2 to Shooting                                                                    |
| **Snapfire weapons**  | Torpedoes, missiles | Shooting | -2 unless target at short range                                                                        |


**Range (from initiative card):** 2 = no shot; 3?7 = long (-4); 8?Jack = medium (-2); Queen?Joker = short (0).

**To hit:** Base TN 4. Modifiers apply to your Shooting roll and stack (e.g., target Evading -2 + medium range -2 = -4; or your Evade outgoing targeting -2 or -1 when you are Evading (raise = -1)). Roll + modifiers vs TN 4.

**Edges that help:** Ace Gunner, Steady Hands, Marksman.

---

#### Engineer

**Your job:** Keep systems online and repair damage during combat.


| When                | Action                   | Skill  | Effect                                                                                                                                                                  |
| ------------------- | ------------------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Systems phase**   | Repair subsystem         | Repair | Success = bring one offline system back online. Raise = back online + remove 1 hull damage/shaken                                                                       |
| **When Club drawn** | Reinforce failing system | Repair | When resolving a Club: Repair check (TN 4) with same modifier as Pilot (Disaster -4, Major -4, Complication -2). Success = avoid system failure before 1d6 system roll. |
| **Between rounds**  | Emergency patch          | Repair | Restore limited function to heavily damaged system (GM discretion)                                                                                                      |


**Engineer Support:** Before the Pilot's check, an Engineer can use **Support** (Repair or Knowledge: Engineering): success = +1 to Pilot's Piloting check; raise = +2.

**Edges that help:** McGyver, Ace (if piloting backup), Mr. Fix It.

---

#### Co-pilot / Commander

**Your job:** Coordinate the crew, spot threats, and support the Pilot.


| When                 | Action              | Skill                                 | Effect                                                                                                  |
| -------------------- | ------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Support phase**    | Support Pilot       | Common Knowledge, Notice, or Piloting | Success = +1 to Pilot's Piloting check. Raise = +2                                                      |
| **Support phase**    | Spot for Gunner     | Notice                                | Success = +1 to one Gunner's Shooting. Raise = +2                                                       |
| **Initiative phase** | Tactical assessment | Smarts or Battle                      | Success = one crewmember may reroll one failed check this round. Raise = reroll + ignore one -2 penalty |
| **Any phase**        | Call out targets    | ?                                     | Designate primary target; first Gunner to hit that target gets +1 (once per round)                      |


**Small ships:** The co-pilot often doubles as a Gunner or Systems Operator. One Support action per round.

**Edges that help:** Command, Tactician, Level-Headed.

---

#### Systems Operator

**Your job:** Manage shields, sensors, and communications. Optional on small craft; essential on larger ships.


| When                | Action                    | Skill                 | Effect                                                                                  |
| ------------------- | ------------------------- | --------------------- | --------------------------------------------------------------------------------------- |
| **Systems phase**   | Activate shield regen     | Electronics           | Success = 5% of max shields. +5% per raise. See Shields section.                        |
| **Support phase**   | Sensor lock               | Electronics or Notice | Success = +1 to one Gunner's Shooting vs designated target. Raise = +2                  |
| **Systems phase**   | Jamming / countermeasures | Electronics           | Opposed vs enemy Electronics or Piloting; success = -2 to enemy attacks or sensor locks |
| **When Club drawn** | Diagnose                  | Electronics or Repair | Identify failing system; success = Engineer gets +1 to Repair that system               |


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

1. **Initiative**: Draw cards; compare for advantage.
2. **Support**: Co-pilot, Commander, Engineer, Systems Operator aid Pilot/Gunners.
3. **Piloting**: Pilot rolls; determine final initiative card.
4. **Maneuver**: Pilot chooses Evade, Stay on Target, Hold Steady, Boost, or Loop.
5. **Gunnery**: Gunners fire (advantage = all weapons; no advantage = turrets only, -2).
6. **Systems**: Engineer repairs; Systems Operator activates shield regen (Electronics), sensor locks.
7. **Complications**: Resolve Clubs; Engineer may attempt Reinforce when Club drawn.

---

### Advantage and Firing (Reference)

- **With advantage** (higher initiative card): May fire all weapons that can bear on target(s). Each weapon system may engage a different target.
- **Without advantage**: Can return fire with **turret weapons only**, -2 to Shooting.
- **To hit:** TN 4. Modifiers stack (range, target Evading, your Evade outgoing targeting, etc.); apply total to your Shooting roll.
- **Range table:** 2 = no attack; 3-7 = long (-4); 8-Jack = medium (-2); Queen-Joker = short (0).
- **Snapfire** (torpedoes): -2 unless target at short range.

### Complications (Clubs)

When a ship draws a Club for initiative, roll 2d6 on the table below. **Pilot roll -X** means the Pilot makes a Piloting check (TN 4) with that modifier applied to the roll; fail = subsystem offline (or major system failure on Disaster). The **Engineer** may attempt **Reinforce** (Repair check, TN 4, same modifier as the Pilot) to avoid the failure; success = subsystem stays online. If the result is a **major system failure** or **subsystem offline**, roll 1d6 on the **Ship Systems Chart** to determine which system is affected.


| 2d6 | Effect                                                                                         |
| --- | ---------------------------------------------------------------------------------------------- |
| 2   | **Disaster:** Piloting -4; fail = **major system failure** (roll 1d6 on Ship Systems Chart)    |
| 3-7 | **Major:** Pilot roll -4; fail = **subsystem offline** (roll 1d6 on Ship Systems Chart)        |
| 8-Q | **Complication:** Pilot roll -2; fail = **subsystem offline** (roll 1d6 on Ship Systems Chart) |
| A   | **Distraction:** -2 Shooting this round                                                        |


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
- **GM call-off:** The GM may **narratively call off the pursuit** at any time?e.g., reinforcements arrive, terrain interferes, the chase is no longer dramatic.
- **Random roll (optional):** After round 5, GM may roll a die each round: **odd** = combat ends (break off or escape); **even** = continues.

---

## 6. How It Works in Play: Example Flow

**Setup:** A Rebel X-wing vs two TIE fighters.

1. **Round 1**
  - All draw for initiative. X-wing draws a 10, TIEs draw a 7 and a 3.
  - X-wing has advantage over both TIEs. TIE 1 has advantage over TIE 2.
  - X-wing: Piloting check (+1 Handling, +2 speed advantage)?success = keeps 10.
  - X-wing fires all forward lasers at TIE 1 (medium range, -2).
  - TIEs: Without advantage, may only use turret-like weapons (or rear weapons if applicable) at -2.
  - Resolve damage, apply hull damage/shaken as usual.
2. **Round 2**
  - TIE 2 draws a Club?rolls Complication table; gets "Distraction," -2 Shooting.
  - Maneuvers from R1 may apply: e.g., TIE 1 did Boost (success)?+2 Piloting this round.
  - Repeat initiative, advantage, and firing.
3. **Round 5+**
  - GM rolls: 5 = odd?combat ends. X-wing escapes; TIEs break off.

---

## 7. Quick Reference: Modifiers


| Modifier                                    | Value                       |
| ------------------------------------------- | --------------------------- |
| Base TN (ship attacks)                      | 4                           |
| Speed advantage (faster than opponent)      | +2                          |
| Speed advantage (2? faster)                 | +4                          |
| Climb advantage (atmosphere)                | +2                          |
| Harsh terrain (debris, asteroids)           | -2                          |
| Ship hull damaged / Shaken (see Hull)       | -1 or -2                    |
| Without advantage (return fire)             | -2 Shooting                 |
| Long range                                  | -4                          |
| Medium range                                | -2                          |
| Evade: target Evading (incoming targeting) | -2 to hit that target       |
| Evade: you Evading (outgoing targeting)    | -2 or -1 to your attacks (raise = -1) |
| Unstable platform (firing from moving ship) | -2 (often negated by Edges) |


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


| Layer             | Source                           | Use                                                    |
| ----------------- | -------------------------------- | ------------------------------------------------------ |
| Initiative cards  | This guide                       | Turn order, advantage, range; maneuvers push modifiers |
| Ship stats        | Ship sources / Star Wars content | Handling, Speed, Toughness, weapons                    |
| Combat flow       | Geek Ken variant + SWADE         | Advantage, range, snapfire, complications              |
| Star Wars content | Star Wars Companion              | Ships, weapons, shields, ion, Edges                    |


Result: abstract, fast ship combat that feels like Star Wars dogfights, driven by initiative cards, Piloting, advantage, and range?without needing a battle mat or detailed positioning.