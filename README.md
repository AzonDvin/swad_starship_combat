# SWADE Star Wars Ship Combat

A Savage Worlds Adventure Edition (SWADE) ship combat system for Star Wars–style starship battles, using initiative cards, momentum, and Star Wars–themed maneuvers.

## Contents

- **SWADE_Star_Wars_Ship_Combat_Guide.md** — Full rules reference: initiative cards, maneuvers, momentum, shields, hull damage, and quick reference tables
- **Ship_Combat_Quick_Reference.md** — One-sheet cheat sheet (tables + round order) distilled from the combat guide
- **Combat_Round_Flowchart.md** — Combat round flow
- **gen_scenario.py** — Generates sample scenarios (YT-1300 vs 3 TIE fighters)
- **gen_maneuver_cards.py** — Generates printable maneuver cards (PDF)
- **Scenario_YT1300_vs_3TIEs.md** — Example scenario (run `gen_scenario.py` to regenerate)
- **Scenario_TIE_vs_YT1300.md** — Example scenario (1 TIE vs YT-1300)
- **ships.json** — Ship stats data

## Quick Start

1. Read **SWADE_Star_Wars_Ship_Combat_Guide.md** for the rules.
2. Use **Ship_Combat_Quick_Reference.md** at the table and **Combat_Round_Flowchart.md** for phase detail.
3. Generate a sample scenario:
   ```bash
   python gen_scenario.py
   ```
4. Create printable maneuver cards:
   ```bash
   pip install -r requirements.txt
   python gen_maneuver_cards.py
   ```
   Output: **Maneuver_Cards.pdf** — 6 landscape cards per page; print on cardstock and cut along borders.

## Maneuvers

| Maneuver        | Summary                                                        |
| --------------- | -------------------------------------------------------------- |
| Evade           | -2 to opponents targeting you; raise negates Stay on Target   |
| Stay on Target  | Opposed Piloting; success = target -1 momentum                |
| I Have You Now  | Req: +2 momentum; +2 Gunnery vs target on success             |
| I Can Hold It   | Steady flight; Shaken must use it to clear; optional momentum → 0 |
| Boost           | Piloting check; success = +2 momentum                         |
| I Know a Few Maneuvers | Piloting TN 4; success/raises = extra initiative card(s), choose; no momentum |
| Loop            | Opposed vs higher card; reverse advantage; raise = −1 incoming |

## Requirements

- Python 3
- **gen_scenario.py** — standard library only
- **gen_maneuver_cards.py** — requires `reportlab` (see `requirements.txt`)
