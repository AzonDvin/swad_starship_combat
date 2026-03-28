"""Generate YT-1300 vs 3 TIEs scenario with pure random rolls. Writes Scenario_YT1300_vs_3TIEs.md"""
import random
import json

# Load ship stats from ships.json
with open("ships.json") as f:
    ships_data = json.load(f)
ships_by_id = {s["id"]: s for s in ships_data["ships"]}
YT = ships_by_id["yt_1300"]
TIE = ships_by_id["tie_fighter"]

YT_SHIELDS_MAX = YT["shields"]
YT_TOUGH = YT["toughness"]
YT_HANDLING = YT["handling"]
TIE_TOUGH = TIE["toughness"]
TIE_HULL_MAX = TIE["hull"]
TIE_HANDLING = TIE["handling"]


def handling_momentum_bonus(your_handling, opponent_handlings):
    """+0, +1, or +2 momentum: beat strict majority on Handling; +2 if also your Handling >= max(opponents) + 3."""
    if not opponent_handlings:
        return 0
    n = len(opponent_handlings)
    beat = sum(1 for h in opponent_handlings if your_handling > h)
    if beat <= n // 2:
        return 0
    mmax = max(opponent_handlings)
    if your_handling >= mmax + 3:
        return 2
    return 1


# 3 TIEs vs 1 YT: per-ship handling advantage vs opponents
YT_OPP_HANDLING = [TIE_HANDLING, TIE_HANDLING, TIE_HANDLING]
YT_HANDLING_MOM = handling_momentum_bonus(YT_HANDLING, YT_OPP_HANDLING)
TIE_HANDLING_MOM = handling_momentum_bonus(TIE_HANDLING, [YT_HANDLING])

def d(n):
    r = random.randint(1, n)
    if r == n and n in (6,8,10):
        return r + d(n)
    return r

JOKER_VAL = 15  # Joker beats all non-jokers for initiative order

def draw(n):
    """Draw n initiative cards. Returns [(value, suit), ...] sorted high to low. Suit: s=spade, h=heart, d=diamond, c=club, j=joker."""
    cards = []
    for _ in range(n):
        if random.random() < 2/54:  # 2 Jokers in 54-card deck
            cards.append((JOKER_VAL, 'j'))
        else:
            cards.append((random.randint(2, 14), random.choice(['s', 'h', 'd', 'c'])))
    return sorted(cards, key=lambda c: -c[0])

def card_str(val, suit):
    if val == JOKER_VAL: return 'Joker'
    if val == 11: return 'Jack' + _suit_char(suit)
    if val == 12: return 'Queen' + _suit_char(suit)
    if val == 13: return 'King' + _suit_char(suit)
    if val == 14: return 'Ace' + _suit_char(suit)
    return str(val) + _suit_char(suit)
def _suit_char(s):
    return '♠' if s=='s' else '♥' if s=='h' else '♦' if s=='d' else '♣' if s=='c' else '' if s=='j' else s

def has_joker(drawn_cards):
    """Joker = value 15."""
    return any(v == JOKER_VAL for v, _ in drawn_cards)


def complication_roll():
    return random.randint(1, 6) + random.randint(1, 6)


def complication_text(cr):
    if cr == 2:
        return "Disaster (major system failure; roll 1d6 Ship Systems — major column)"
    if 3 <= cr <= 5:
        return "Distraction (ship loses all momentum)"
    if 6 <= cr <= 8:
        return "Flight deck ionization (10 stun damage to a random crew member)"
    if 9 <= cr <= 11:
        return "Complication (subsystem offline; roll 1d6 Ship Systems — subsystem column)"
    return "Major (subsystem offline; roll 1d6 Ship Systems — subsystem column; -1 to Repair to fix that subsystem until repaired)"


# Simulate 5 rounds with full state
yt_shields = YT_SHIELDS_MAX
tie_hull = [0,0,0]
tie_shaken = [False,False,False]
yt_shaken = False
yt_sot = 0  # Stay on Target modifier (momentum; reset when YT becomes Shaken)
yt_boost = 0  # +2 momentum from successful Boost; reset when YT becomes Shaken
rounds_data = []
TIE_MANEUVERS = ['I Can Hold It', 'Stay on Target', 'Boost']  # random choice when not Shaken

def has_advantage(attacker_card, target_card, attacker='TIE'):
    """TIE needs higher card than YT. YT turret always has advantage."""
    if attacker == 'YT': return True
    return attacker_card > target_card

for rd in range(1, 6):
    # Initiative: one card each (no Piloting roll). Boost raise can add a card same round during Maneuvers.
    yt_draw = list(draw(1))
    t1_draw = list(draw(1))
    t2_draw = list(draw(1))
    t3_draw = list(draw(1))

    yt_card = yt_draw[0][0]
    t1_card = t1_draw[0][0]
    t2_card = t2_draw[0][0]
    t3_card = t3_draw[0][0]

    yt_mod = YT_HANDLING + yt_boost - yt_sot + YT_HANDLING_MOM
    tie_mod = TIE_HANDLING + TIE_HANDLING_MOM
    # Opposed Piloting defense for Stay on Target (maneuver phase; Wild Card vs d6)
    yt_sot_def = max(d(10), d(6))
    
    # Build order (initial; Boost raise may update YT card and order before Gunnery)
    order = sorted([('YT',yt_card),('T1',t1_card),('T2',t2_card),('T3',t3_card)], key=lambda x:-x[1])
    
    # TIE maneuvers (I Can Hold It if Shaken, else random)
    t1_man = 'I Can Hold It' if tie_shaken[0] else random.choice(TIE_MANEUVERS)
    t2_man = 'I Can Hold It' if tie_shaken[1] else random.choice(TIE_MANEUVERS)
    t3_man = 'I Can Hold It' if tie_shaken[2] else random.choice(TIE_MANEUVERS)
    sot_rolls = [d(6), d(6), d(6)]  # Stay on Target/Boost: TIE Piloting d6
    # YT maneuver: I Can Hold It when Shaken (only option), else Boost if top initiative, else Evade
    yt_top = order[0][0] == 'YT'
    yt_man = 'I Can Hold It' if yt_shaken else ('Boost' if yt_top else 'Evade')
    # Evade/Boost, Gunnery, Systems rolls
    # YT-1300 has ONE quad turret = ONE weapon system = ONE target per round (guide: each weapon system can target a different enemy)
    yt_evade = max(d(10), d(6))   # Wild Card (Evade Piloting check)
    yt_boost_roll = max(d(10), d(6)) if yt_man == 'Boost' else None  # Boost Piloting check
    yt_boost_raise = False
    yt_boost_chosen = None  # (value, suit) Pilot chose for initiative after Boost raise
    if yt_man == 'Boost' and yt_boost_roll is not None and (yt_boost_roll + yt_mod) >= 8:
        yt_boost_raise = True
        extra = draw(1)[0]
        opts = yt_draw + [extra]
        chosen = max(opts, key=lambda c: c[0])
        yt_boost_chosen = chosen
        yt_card = chosen[0]
        yt_draw = sorted(opts, key=lambda c: -c[0])
        order = sorted([('YT', yt_card), ('T1', t1_card), ('T2', t2_card), ('T3', t3_card)], key=lambda x: -x[1])
    yt_target_tie = random.randint(1, 3)  # which TIE (1-3) the turret targets this round
    yt_shoot = max(d(10), d(6))  # Wild Card
    t1_shoot, t2_shoot, t3_shoot = d(6), d(6), d(6)  # TIE Gunners d6
    # damage[0] = YT->target TIE; damage[1,2,3] = T1,T2,T3 -> YT
    if yt_man == 'I Can Hold It':
        ev_succ_rd, ev_raise_rd, ev_out_rd, ev_in_rd = False, False, 0, 0
    elif yt_man == 'Boost':
        ev_succ_rd, ev_raise_rd, ev_out_rd, ev_in_rd = False, False, 0, 0  # No Evade when Boost
    else:
        ev_succ_rd = yt_evade - 3 >= 4
        ev_raise_rd = yt_evade - 3 >= 8  # Raise: negates Stay on Target maneuvers this round
        ev_out_rd = 0  # New Evade: no outgoing penalty; success = -2 incoming only
        ev_in_rd = -2 if ev_succ_rd else 0  # -2 to opponents targeting this ship
    damages = [d(10)+d(10)+2 for _ in range(4)]
    raise_bonus = [0, 0, 0, 0]  # +1d6 when to-hit >= 8 (raise)
    yt_tot = yt_shoot - 2 + ev_out_rd
    if yt_tot >= 8: damages[0] += d(6); raise_bonus[0] = 1
    for i, sh in enumerate([t1_shoot, t2_shoot, t3_shoot]):
        tot = sh + ev_in_rd
        if tot >= 8: damages[1+i] += d(6); raise_bonus[1+i] = 1
    elec = max(d(10), d(6))  # Engineer Wild Card
    
    # Advantage: TIE beats YT card to fire
    t1_adv = has_advantage(t1_card, yt_card)
    t2_adv = has_advantage(t2_card, yt_card)
    t3_adv = has_advantage(t3_card, yt_card)

    yt_shields_round_start = yt_shields
    comp_events = []

    # Apply damage in initiative order; hull damage triggers a Complication roll (2d6) for the ship that was hit
    ev_succ = yt_evade - 3 >= 4
    ev_in = -2 if ev_succ else 0
    for ship, _ in order:
        if ship == 'YT':
            # One turret = one target only
            tid = yt_target_tie - 1
            hit = (yt_shoot - 2) >= 4  # no outgoing penalty (matches Gunnery write-up)
            if hit:
                comp_events.append({'ship': f'TIE {tid + 1}', 'roll': complication_roll()})
            if hit and damages[0] > TIE_TOUGH:
                    tie_shaken[tid] = True
                    if damages[0] >= TIE_TOUGH + 4: tie_hull[tid] += 1 + max(0, (damages[0]-TIE_TOUGH-4)//4)
        else:
            tid = int(ship[1]) - 1
            adv = t1_adv if ship=='T1' else t2_adv if ship=='T2' else t3_adv
            if adv:
                shoot = t1_shoot if ship=='T1' else t2_shoot if ship=='T2' else t3_shoot
                hit = (shoot + ev_in) >= 4
                dmg = damages[1 + tid]
                if hit and dmg > 0:
                    comp_events.append({'ship': 'YT-1300', 'roll': complication_roll()})
                    sh_before = yt_shields
                    yt_shields = max(0, yt_shields - dmg)
                    overflow = dmg - sh_before if dmg > sh_before else 0
                    if overflow > YT_TOUGH:
                        yt_shaken = True

    rounds_data.append({
        'rd': rd, 'yt_shields': yt_shields_round_start, 'yt_sot': yt_sot, 'yt_boost': yt_boost,
        'yt_joker': has_joker(yt_draw), 't1_joker': has_joker(t1_draw), 't2_joker': has_joker(t2_draw), 't3_joker': has_joker(t3_draw),
        'yt_draw': yt_draw, 't1_draw': t1_draw, 't2_draw': t2_draw, 't3_draw': t3_draw,
        'yt_sot_def': yt_sot_def,
        'yt_boost_raise': yt_boost_raise,
        'yt_boost_chosen': yt_boost_chosen,
        'yt_card': yt_card, 't1_card': t1_card, 't2_card': t2_card, 't3_card': t3_card,
        'order': order, 'yt_shoot': yt_shoot, 'yt_target_tie': yt_target_tie,
        't1_shoot': t1_shoot, 't2_shoot': t2_shoot, 't3_shoot': t3_shoot,
        'damages': damages, 'raise_bonus': raise_bonus, 'elec': elec, 'yt_evade': yt_evade, 'ev_raise': ev_raise_rd,
        'comp_events': comp_events,
        't1_man': t1_man, 't2_man': t2_man, 't3_man': t3_man, 'yt_man': yt_man, 'sot_rolls': sot_rolls,
        'yt_boost_roll': yt_boost_roll, 'yt_top': yt_top,
        't1_adv': t1_adv, 't2_adv': t2_adv, 't3_adv': t3_adv,
        'tie_hull': tie_hull.copy(), 'tie_shaken': tie_shaken.copy()
    })

    # Stay on Target: success = YT -1 momentum next round (cumulative: 2 successes = -2, 3 = -3). Negated if YT Evaded with raise. YT Shaken = lose all momentum.
    prev_yt_sot = yt_sot
    yt_sot = 0
    if yt_shaken:
        yt_sot = 0  # Shaken loses all momentum
    elif not ev_raise_rd:
        for m, r in zip([t1_man, t2_man, t3_man], sot_rolls):
            if m == 'Stay on Target' and r + tie_mod >= yt_sot_def + (YT_HANDLING + yt_boost - prev_yt_sot):
                yt_sot += 1  # cumulative per success
    if yt_man == 'I Can Hold It':
        yt_shaken = False  # I Can Hold It clears Shaken
    
    # Boost: success = +2 momentum (persists until Shaken)
    if yt_shaken:
        yt_boost = 0  # Shaken loses all momentum
    elif yt_man == 'Boost' and yt_boost_roll is not None:
        brtot = yt_boost_roll + yt_mod
        if brtot >= 4:
            yt_boost += 2
    
    # Regen
    regen = 2 if elec >= 4 else 0
    if elec >= 8: regen = 4
    yt_shields = min(YT_SHIELDS_MAX, yt_shields + regen)

# Write scenario
with open('Scenario_YT1300_vs_3TIEs.md', 'w', encoding='utf-8') as f:
    f.write(f"""# Scenario: Three TIE Fighters vs YT-1300 Freighter

## Setup

**Location:** Asteroid belt near Ord Mantell. A YT-1300 freighter evades Imperial patrol and is intercepted by three TIE fighters.

**Ships** (see ships.json: `yt_1300`, `tie_fighter`):

| Ship | Size | Handling | Speed | Toughness | Armor | Hull | Shields | Crew |
|------|------|----------|-------|-----------|-------|------|---------|------|
| **YT-1300** | {YT["size"]} | {YT["handling"]:+d} | {YT["speed"]} | {YT["toughness"]} | {YT["armor"]} | {YT["hull"]} | {YT["shields"]} | {", ".join(YT["crew"])} |
| **TIE Fighter 1** | {TIE["size"]} | {TIE["handling"]:+d} | {TIE["speed"]} | {TIE["toughness"]} | {TIE["armor"]} | {TIE["hull"]} | — | {", ".join(TIE["crew"])} |
| **TIE Fighter 2** | {TIE["size"]} | {TIE["handling"]:+d} | {TIE["speed"]} | {TIE["toughness"]} | {TIE["armor"]} | {TIE["hull"]} | — | {", ".join(TIE["crew"])} |
| **TIE Fighter 3** | {TIE["size"]} | {TIE["handling"]:+d} | {TIE["speed"]} | {TIE["toughness"]} | {TIE["armor"]} | {TIE["hull"]} | — | {", ".join(TIE["crew"])} |

**Key modifiers:**
- TIEs’ **handling advantage** vs YT-1300: **+{TIE_HANDLING_MOM}** momentum each round (YT-1300 vs three TIEs: **+{YT_HANDLING_MOM}**). See guide: strict majority on Handling; +2 if also ≥ highest enemy Handling + 3.
- YT-1300 has turret; TIEs have fixed forward cannons.
- YT-1300 has shields ({YT_SHIELDS_MAX} max); regen 5% + 5%/raise. TIEs have none.
- **One weapon system = one target per round** (quad turret fires at one ship only).
- **Momentum** persists round to round. Lose all: Distraction, becoming Shaken. **Stay on Target** (opposed Piloting): target -1 momentum per success (cumulative; 2 successes = -2, 3 = -3).
- **Joker:** Acts first, +2 to all crew rolls that round, short range.
- **Complications:** Each time a ship **takes hull damage** from an attack (see guide §4), roll **2d6** on the Complications table for **that ship** (usually resolved during or right after Gunnery).
- **Raise:** To-hit roll ≥ 8 (TN+4) adds +1d6 to damage.
- **Crew skills:** YT-1300 Pilot, Co-pilot, Gunner, Engineer = d10 + wild d6 (aces/Wild Cards; take best). TIE Pilot/Gunner = d6.

---

""")
    
    for r in rounds_data:
        f.write(f"## Round {r['rd']}\n\n")
        f.write(f"### Initiative (start of round)\n")
        f.write(f"- YT-1300 shields: **{r['yt_shields']}**.\n\n")
        f.write(f"### Initiative draw\n")
        yj = ' — **Joker**' if r['yt_joker'] else ''
        c1j = ' — **Joker**' if r['t1_joker'] else ''
        c2j = ' — **Joker**' if r['t2_joker'] else ''
        c3j = ' — **Joker**' if r['t3_joker'] else ''

        def draw_line(label, draw, joker_note):
            cards_txt = ", ".join(card_str(a, b) for a, b in draw)
            f.write(f"- **{label}:** {cards_txt}{joker_note}\n")

        draw_line("YT-1300", r['yt_draw'], yj)
        draw_line("TIE 1", r['t1_draw'], c1j)
        draw_line("TIE 2", r['t2_draw'], c2j)
        draw_line("TIE 3", r['t3_draw'], c3j)
        f.write("\n")
        f.write("*Initial initiative draw (no Piloting roll). **Boost** raise or **I Know a Few Maneuvers** (success/raises) can add extra card(s) in Maneuvers; the Pilot chooses which applies—see guide.*\n\n")
        ord_str = ' → '.join([f"{s[0]} ({s[1]})" for s in r['order']])
        f.write(f"**Order:** {ord_str}\n\n")
        f.write(f"### Maneuver\n")
        ev_succ = (r['yt_evade'] - 3 >= 4) if r.get('yt_man') == 'Evade' else False  # Evade: -3 for 3 opponents
        ev_raise = (r['yt_evade'] - 3 >= 8) if r.get('yt_man') == 'Evade' else False
        ev_desc = 'No effect.'
        if ev_succ:
            ev_desc = '-2 to opponents targeting this ship. '
            if ev_raise: ev_desc += 'Raise: negates Stay on Target maneuvers this round.'
            else: ev_desc = ev_desc.rstrip()
        if r.get('yt_man') == 'I Can Hold It':
            f.write(f"- YT-1300: **I Can Hold It** (Shaken — clears Shaken).\n")
        elif r.get('yt_man') == 'Boost':
            br = r.get('yt_boost_roll')
            bmod = YT_HANDLING + r.get('yt_boost', 0) - r['yt_sot']
            brtot = (br + bmod) if br is not None else 0
            bsucc = br is not None and brtot >= 4
            raise_note = ""
            ch = r.get('yt_boost_chosen')
            if r.get('yt_boost_raise') and ch is not None:
                raise_note = f" **Raise:** extra initiative card; chose **{card_str(ch[0], ch[1])}** for order/advantage/range (simulation: highest rank). "
            f.write(f"- YT-1300: **Boost** (top initiative) — Piloting check (TN 4). Roll {br} + {bmod} = {brtot if br is not None else '?'} — {'success' if bsucc else 'fail'}. {'+2 momentum.' if bsucc else 'No effect.'}{raise_note}\n")
        else:
            f.write(f"- YT-1300: **Evade** (Pilot d10+wild d6) — Piloting check (TN 4), -3 (3 opponents). Roll {r['yt_evade']} - 3 = {r['yt_evade']-3} — {'success' if ev_succ else 'fail'}{' (raise)' if ev_raise else ''}. {ev_desc}\n")
        def man_line(tie_id, man, sot_r):
            if man == 'I Can Hold It': return f"- TIE {tie_id}: **I Can Hold It**\n"
            if man == 'Stay on Target':
                immune = r.get('ev_raise', False)  # YT Evade raise = immune to Stay on Target
                if immune: return f"- TIE {tie_id}: **Stay on Target** vs YT-1300 — negated (YT Evaded with raise).\n"
                yt_sot_tn = r['yt_sot_def'] + (YT_HANDLING + r.get('yt_boost', 0) - r['yt_sot'])
                succ = sot_r + tie_mod >= yt_sot_tn
                return f"- TIE {tie_id}: **Stay on Target** (Pilot d6) vs YT-1300 — opposed Piloting. TIE {tie_id}: {sot_r}+{tie_mod} vs YT: {yt_sot_tn} — {'success' if succ else 'fail'}. {'YT-1300 -1 momentum.' if succ else 'No effect.'}\n"
            return f"- TIE {tie_id}: **Boost** (Pilot d6) — Piloting TN 4. Roll {sot_r}+{tie_mod} = {sot_r+tie_mod} — success. +2 momentum.\n"
        f.write(man_line(1, r['t1_man'], r['sot_rolls'][0]))
        f.write(man_line(2, r['t2_man'], r['sot_rolls'][1]))
        f.write(man_line(3, r['t3_man'], r['sot_rolls'][2]))
        f.write("\n")
        f.write(f"### Gunnery\n")
        f.write(f"*(One weapon system = one target per round. Rolls: YT {r['yt_shoot']}, T1 {r['t1_shoot']}, T2 {r['t2_shoot']}, T3 {r['t3_shoot']}; Damage {r['damages']})*\n")
        ev_out = 0  # No outgoing penalty (new Evade rules)
        ev_in = -2 if ev_succ else 0
        shields = r['yt_shields']  # track as we apply damage in initiative order

        def tie_damage_desc(dmg, tid):
            if dmg <= TIE_TOUGH: return f" vs Toughness {TIE_TOUGH}: no effect (glancing hit)."
            shaken = " **Shaken.**" if dmg > TIE_TOUGH else ""
            hull_thresh = TIE_TOUGH + 4
            if dmg < hull_thresh: return f" vs Toughness {TIE_TOUGH}:{shaken} Pilot must I Can Hold It next round."
            hull = 1 + max(0, (dmg - hull_thresh) // 4)
            hull = min(hull, TIE_HULL_MAX)
            if hull == 1: status = "**Damaged** (−1 all checks)"
            elif hull == 2: status = "**Crippled** (−2 all checks)"
            else: status = "**Destroyed**"
            return f" vs Toughness {TIE_TOUGH}:{shaken} +{hull} hull damage → {status}."

        def yt_damage_desc(dmg, sh_before):
            new_sh = max(0, sh_before - dmg)
            if dmg <= sh_before:
                return new_sh, f" Strips {dmg} from shields. **YT-1300 shields: {new_sh}.**"
            overflow = dmg - sh_before
            if overflow < YT_TOUGH: return 0, f" Depletes shields ({sh_before}). Overflow {overflow} vs Toughness {YT_TOUGH}: no hull effect. **Shields: 0.**"
            if overflow < YT_TOUGH + 4: return 0, f" Depletes shields. Overflow {overflow} vs Toughness {YT_TOUGH}: **Shaken.** **Shields: 0.**"
            hull = 1 + (overflow - YT_TOUGH - 4) // 4  # 24+ = 1 hull, 28+ = 2, etc.
            if hull == 1: status = "**Damaged** (−1 all checks)"
            elif hull >= 2: status = "**Crippled** (−2 all checks)"
            return 0, f" Depletes shields. Overflow {overflow} vs Toughness {YT_TOUGH}: **Shaken** +{hull} hull → {status}. **Shields: 0.**"

        # Resolve in initiative order
        for ship, _ in r['order']:
            if ship == 'YT':
                tt = r['yt_target_tie']
                ys = r['yt_shoot']
                tot = ys - 2 + ev_out
                hit = tot >= 4
                ev_str = ""  # No outgoing penalty (Evade only affects incoming)
                dmg = r['damages'][0]
                raise_str = " **with raise** (+1d6)" if r['raise_bonus'][0] else ""
                f.write(f"- **YT-1300** vs TIE {tt}: Quad turret (Gunner d10+wild d6, one target). TN 4. Roll {ys} - 2 (range){ev_str} = {tot} — ")
                if hit:
                    dmg_str = f"2d10+2" + (f"+1d6 = {dmg}" if r['raise_bonus'][0] else f" = {dmg}")
                    f.write(f"**hit{raise_str}.** Damage {dmg_str}.{tie_damage_desc(dmg, tt-1)}\n")
                else:
                    f.write(f"miss. Damage 2d10+2 = {dmg}.\n")
            else:
                tid = int(ship[1]) - 1
                adv = r['t1_adv'] if ship=='T1' else r['t2_adv'] if ship=='T2' else r['t3_adv']
                shoot = r['t1_shoot'] if ship=='T1' else r['t2_shoot'] if ship=='T2' else r['t3_shoot']
                dmg = r['damages'][1+tid]
                if adv:
                    tot = shoot + ev_in
                    hit = tot >= 4
                    ev_str = " - 2 (target Evading)" if ev_succ else ""
                    raise_str = " **with raise** (+1d6)" if r['raise_bonus'][1+tid] else ""
                    f.write(f"- **TIE {tid+1}** vs YT-1300: Dual lasers (Gunner d6, advantage). TN 4. Roll {shoot}{ev_str} = {tot} — ")
                    if hit:
                        dmg_str = f"2d10+2" + (f"+1d6 = {dmg}" if r['raise_bonus'][1+tid] else f" = {dmg}")
                        shields, desc = yt_damage_desc(dmg, shields)
                        f.write(f"**hit{raise_str}.** Damage {dmg_str}.{desc}\n")
                    else:
                        f.write(f"miss. Damage 2d10+2 = {dmg}.\n")
                else:
                    f.write(f"- **TIE {tid+1}**: No advantage — cannot fire (fixed forward cannons).\n")
        f.write("\n")
        f.write(f"### Systems\n")
        regen = 2 if r['elec'] >= 4 else 0
        if r['elec'] >= 8: regen = 4
        f.write(f"- YT-1300 Electronics (Engineer d10+wild d6): Rolls {r['elec']} — {'raise' if r['elec']>=8 else 'success' if r['elec']>=4 else 'fail'}. +{regen} shields.\n\n")
        if r.get('comp_events'):
            f.write(f"### Complications (damage)\n")
            for ev in r['comp_events']:
                cr = ev['roll']
                f.write(f"- **{ev['ship']}** took hull damage — Complication **2d6 = {cr}**. {complication_text(cr)}\n")
            f.write("\n")
        f.write("---\n\n")

    f.write("## Summary\n\n")
    f.write("*(Scenario generated with pure random rolls. Run `python gen_scenario.py` to generate a new scenario with different rolls.)*\n")

print("Wrote Scenario_YT1300_vs_3TIEs.md")
