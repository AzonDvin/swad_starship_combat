# Ship Combat Quick Reference

One-page style cheat sheet. **Full rules:** `SWADE_Star_Wars_Ship_Combat_Guide.md` · **Round flow:** `Combat_Round_Flowchart.md`

---

## Round order

1. **Initiative** — Each ship **one** card → order, **advantage**, **range**. Pilot: **no** Piloting roll. **Boost** raise / **I Know a Few Maneuvers** add card(s) in step 3.
2. **Support** (optional) — Crew trait rolls **before** maneuvers (aid Pilot / Gunners).
3. **Maneuver** — Pilot picks **one**: Evade, Stay on Target, I Have You Now, I Can Hold It, Boost, I Know a Few Maneuvers, Loop.
4. **Gunnery** — Shooting in initiative order; **hull damage** → **2d6 Complications** for ship hit (now or note for step 6).
5. **Systems** — Repair; shield regen (Electronics); jamming; etc.
6. **Complications** — Reinforce, Diagnose, follow-up from **2d6** results.
7. **End of round** — **Break away** if eligible (after step 6).

---

## Initiative card → range (when you shoot)

| Card        | Range   | Modifier |
| ----------- | ------- | -------- |
| 2           | No shot | —        |
| 3–7         | Long    | −4       |
| 8–Jack      | Medium  | −2       |
| Queen–Joker | Short   | 0        |

**Joker:** Acts first; **+2** all crew rolls that round; **short** range for attacks.

---

## Handling advantage & momentum

- **+1 momentum** / round: your **Handling** higher than **strict majority** of enemies (strictly lower count).
- **+2** instead: same, **and** your Handling ≥ **highest enemy Handling + 3**.
- Applies to **maneuver-phase** Piloting and **opposed** Piloting.

**Momentum:** Starts **0**; persists. All **Piloting** rolls add/subtract **current momentum**. **Lose all:** Distraction (complication), **Shaken**.

---

## Maneuvers (Pilot — one per round)

| Maneuver | Summary |
| -------- | ------- |
| **Evade** | Piloting TN 4, −1 per opposing ship. Success: −2 to foes **targeting you**. Raise: negates **Stay on Target** vs you. |
| **Stay on Target** | Opposed Piloting vs one ship. Success: target −1 mom; Raise: you +1 mom. |
| **I Have You Now** | Need **+2+** momentum. Opposed vs target. Success: **+2 Gunnery** vs target, −2 mom; Raise: +2 Gunnery, no mom loss; Fail: −4 mom. |
| **I Can Hold It** | Steady. **Shaken:** must (clears Shaken). **Optional:** momentum → **0**. No roll. |
| **Boost** | Piloting TN 4. Success: **+2** mom. Raise: **+1** card, **choose** for order/advantage/range. |
| **I Know a Few Maneuvers** | Piloting TN 4. Success: **+1** card + choose. Raise: **+1 card per raise**, then choose. **No** mom change. |
| **Loop** | Opposed vs higher **card**; both **−(Size − Handling)**. Success: reverse advantage vs them, +1 mom. Raise: **−1** to attacks vs you **until your next Maneuver**. Crit fail: −2 mom. |

---

## Gunnery

- **TN 4**; stack modifiers on Shooting.
- **Advantage** (higher card): all weapons that bear; each **weapon system** may pick a target.
- **No advantage:** **turrets only**, **−2** Shooting.
- **Snapfire** (torpedoes/missiles): **−2** unless target at **short** range.
- **Unstable platform:** **−2** (Edges may negate) — full guide.

---

## Shields & hull

- Damage **shields first**; overflow vs **Toughness** → **Shaken** / **hull damage** on track.
- **Taking hull damage** (for **Complications**): **any** damage from a hit — **shields and/or** hull track. **Misses:** no 2d6 (GM discretion).

**vs Toughness (no / depleted shields):** Damage > Toughness → **Shaken**; already Shaken → **1 hull damage**. **+1 hull damage** per **4** over Toughness beyond first bracket (see guide).

| Hull damage | Effect |
| ----------- | ------ |
| 1 | **Damaged** −1 all ship checks |
| 2+ | **Crippled** −2 all ship checks |
| = Hull stat | **Destroyed** (or disabled) |

**Shaken:** Lose **all** momentum; may fire; **must** **I Can Hold It** next maneuver (clears Shaken).

**Shield regen (Systems):** Electronics — **5%** max shields, **+5%** per raise (round down base).

---

## Complications (2d6 when ship takes hull damage)

**Pilot roll −X:** Piloting TN 4 at that mod; fail → offline / major per result. **Engineer Reinforce:** Repair TN 4, same mod — success may avoid failure before **1d6** system. **Major failure** or **subsystem offline** → **1d6** system chart.

| 2d6 | Effect |
| --- | ------ |
| 2 | **Disaster** — Pilot −4; fail = **major system failure** (d6) |
| 3–5 | **Distraction** — lose all momentum |
| 6–8 | **Ionization** — 10 stun random crew |
| 9–11 | **Complication** — Pilot −2; fail = **subsystem offline** (d6) |
| 12 | **Major** — Pilot −4; fail = **subsystem offline** (d6) |

### Ship Systems (d6)

| d6 | System | Major failure (short) | Subsystem offline (short) |
| -- | ------ | ---------------------- | ------------------------- |
| 1 | Sublight | Engines off; speed 0 | Handling −1 |
| 2 | Nav | No hyperspace | Astrogation delayed |
| 3 | Shields | All down | No regen until repair |
| 4 | Weapons | All offline | One bank/turret offline |
| 5 | Life support | Breach; −2 all | −1 one crew check |
| 6 | Sensors/Comms | −4 Shooting; no comms | −2 Shooting |

*(Full text: full guide.)*

---

## Common modifiers (at-a-glance)

| Situation | Modifier |
| --------- | -------- |
| Base TN ship attacks | **4** |
| Handling adv. (strict majority) | **+1** momentum |
| Handling adv. + ≥ highest enemy +3 | **+2** momentum |
| Climb (atmosphere) | **+2** |
| Debris / asteroids | **−2** Piloting |
| Hull Damaged / Crippled / Shaken | **−1** / **−2** ship checks |
| No advantage (return fire) | **−2** Shooting |
| Long / medium range | **−4** / **−2** |
| Target **Evade** success | **−2** to hit that ship |
| **Loop** raise vs you | **−1** to hit you |
| **I Have You Now** — you succeeded vs declared target | **+2** Gunnery vs that target |
| Unstable platform | **−2** Shooting |

---

## Combat end

- **Hyperjump** — Nav Computer up; Astrogation.
- **Break away (sublight)** — **End of round** after Complications: your **card** beats **every** enemy’s **this round** **and** your **Top Speed** > **each** enemy’s (Joker high; ties block unless GM says otherwise).
- **GM** ends scene; optional: after R5+, d6 odd = end.

---

## Crew hooks (Support = optional, before maneuver)

| Role | Typical action |
| ---- | ---------------- |
| Co-pilot | Support Pilot / Spot / **Tactical assessment** (Smarts or Battle) — **one** Support action |
| Engineer | Support Pilot (Repair or Know.: Eng) |
| Systems Op | Sensor lock (Support) |
| Co-pilot | **Call out targets** (Battle or Smarts) — any phase; first hit on call +1 (1/round) |

---

## Edges (see SWADE + Star Wars Companion)

**Pilot:** Ace, Steady Hands, Quick, Level-Headed · **Gunner:** Ace Gunner, Steady Hands, Marksman · **Engineer:** McGyver, Mr. Fix It · **Command:** Command, Tactician

---

*Derived from `SWADE_Star_Wars_Ship_Combat_Guide.md`. Ion weapons, directional shields, and setting details — Companion + full guide.*
