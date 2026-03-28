"""
Generate printable PDF maneuver cards for SWADE Star Wars ship combat.
Run: python gen_maneuver_cards.py
Output: Maneuver_Cards.pdf (6 cards per page, cut along borders)
Requires: pip install reportlab
"""

try:
    from reportlab.lib.pagesizes import letter, landscape
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    from reportlab.pdfbase.pdfmetrics import stringWidth
except ImportError:
    print("Requires reportlab. Run: pip install reportlab")
    exit(1)

# Landscape page
PAGE_SIZE = landscape(letter)

# Card size: ~3.25" x 2.25" (landscape cards; 6 per page in 3x2 grid)
CARD_W = 3.25 * inch
CARD_H = 2.25 * inch
MARGIN = 0.35 * inch
GAP = 0.15 * inch

# Maneuver data: (name, effect_summary, details_list)
MANEUVERS = [
    ("Evade", "Piloting TN 4, -1 per opponent",
     ["Success: -2 to opponents targeting you", "Raise: negates Stay on Target"]),
    ("Stay on Target", "Opposed Piloting vs one target",
     ["Success: target -1 momentum", "Raise: you +1 momentum"]),
    ("I Have You Now", "Req: +2 momentum. Opposed vs target.",
     ["Success: +2 Gunnery, -2 momentum", "Raise: +2 Gunnery, no loss", "Fail: -4 momentum"]),
    ("I Can Hold It", "Steady flight",
     ["Shaken: must declare (clears Shaken)", "Optional: reset momentum to 0", "No roll"]),
    ("Boost", "Piloting TN 4",
     ["Success: +2 momentum", "Raise: extra initiative card, choose"]),
    ("I Know a Few Maneuvers", "Piloting TN 4",
     ["Success: extra initiative card, choose", "Raise: +1 card per raise, then choose", "No momentum change"]),
    ("Loop", "Opposed vs higher card. -(Size-Handling) + momentum",
     ["Success: advantage +1 momentum", "Raise: -1 to ships targeting you", "Crit fail: -2 momentum"]),
]


def wrap_text(text, font, size, max_width):
    """Split text into lines that fit within max_width."""
    words = text.split()
    lines = []
    current = []
    for w in words:
        test = " ".join(current + [w])
        if stringWidth(test, font, size) <= max_width:
            current.append(w)
        else:
            if current:
                lines.append(" ".join(current))
            current = [w]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_card(c, x, y, name, summary, details):
    """Draw a single maneuver card at (x,y)."""
    c.saveState()
    c.translate(x, y)

    pad = 0.12 * inch
    text_width = CARD_W - 2 * pad

    # Border
    c.setStrokeColor(HexColor("#333333"))
    c.setLineWidth(1)
    c.rect(0, 0, CARD_W, CARD_H, stroke=1, fill=0)

    # Header bar
    header_h = 0.38 * inch
    c.setFillColor(HexColor("#1a365d"))
    c.rect(0, CARD_H - header_h, CARD_W, header_h, stroke=0, fill=1)

    # Maneuver name
    c.setFillColor(HexColor("#ffffff"))
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(CARD_W / 2, CARD_H - 0.26 * inch, name)

    # Summary (with wrapping)
    c.setFillColor(HexColor("#000000"))
    c.setFont("Helvetica", 10)
    summary_lines = wrap_text(summary, "Helvetica", 10, text_width)
    for i, line in enumerate(summary_lines):
        c.drawString(pad, CARD_H - 0.55 * inch - i * 0.15 * inch, line)

    # Details (with wrapping)
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#374151"))
    detail_y = CARD_H - 0.78 * inch - len(summary_lines) * 0.15 * inch
    for line in details:
        wrapped = wrap_text("• " + line, "Helvetica", 9, text_width)
        for wline in wrapped:
            c.drawString(pad, detail_y, wline)
            detail_y -= 0.18 * inch

    c.restoreState()


def main():
    out = "Maneuver_Cards.pdf"
    c = canvas.Canvas(out, pagesize=PAGE_SIZE)
    w, h = PAGE_SIZE
    
    # Page layout: 3 cols x 2 rows (landscape)
    cards_per_page = 6
    cols, rows = 3, 2
    
    start_x = MARGIN
    start_y = h - MARGIN - CARD_H
    
    for idx, (name, summary, details) in enumerate(MANEUVERS):
        slot = idx % cards_per_page
        col = slot % cols
        row = slot // cols
        
        if idx > 0 and slot == 0:
            c.showPage()
            c.setPageSize(PAGE_SIZE)
        
        x = start_x + col * (CARD_W + GAP)
        y = start_y - row * (CARD_H + GAP)
        
        draw_card(c, x, y, name, summary, details)
    
    c.save()
    print(f"Wrote {out}")
    print("Print and cut along card borders. Recommended: print on cardstock.")


if __name__ == "__main__":
    main()
