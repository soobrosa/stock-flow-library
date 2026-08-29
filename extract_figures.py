#!/usr/bin/env python3
"""Extract original figures from the source PDFs into figures/ (PNG).

For born-digital PDFs: locate the caption page and caption line via
`pdftotext -bbox`; the figure zone is cropped from the top boundary (found by
scanning upward from the caption and stopping at the first large vertical gap
between text rows) down to the caption bottom. Pure-scan PDFs are shipped as
auto-trimmed full pages.

    python3 extract_figures.py
"""
import re, subprocess, pathlib
from PIL import Image, ImageOps

LIB = pathlib.Path(__file__).parent
OUT = LIB / "figures"; OUT.mkdir(exist_ok=True)
TMP = pathlib.Path("/tmp/figs"); TMP.mkdir(exist_ok=True)
DPI = 150; S = DPI / 72.0
GAP_PT = 28          # vertical gap (points) that ends a figure block

# (name, pdf stem, caption regex, mode, page hint)
FIGURES = [
    # --- books ---
    ("sterman_sfd",              "Sterman_2000_Business-Dynamics",       r"Figure 2-6 shows",                         "above", 83),
    ("gl_sim_balance",           "Godley-Lavoie_2007_Monetary-Economics", r"Balance sheet of Model SIM",              "above", 104),
    ("gl_sim_tfm",               "Godley-Lavoie_2007_Monetary-Economics", r"Accounting \(transactions\) matrix for Model SIM", "above", 105),
    ("forrester61_fig1",         "Forrester_1961_Industrial-Dynamics",   r"Figure 1-1\.? The art",                    "above", 16),
    ("world3_feedback_loops",    "Meadows_1972_Limits-to-Growth",        r"Figure 24 FEEDBACK LOOPS",                 "above", 108),
    ("urban_dynamics_scan",      "Forrester_1969_Urban-Dynamics",        r"",                                         "page",  30),
    # --- papers (existing) ---
    ("rework_cycle",     "Lyneis-Ford_2007_PM-survey",           r"Fig\.?\s*1\.?\s*The rework",                 "above", None),
    ("pm_control_loops", "Lyneis-Ford_2007_PM-survey",           r"Fig\.?\s*2\.?\s*Controlling feedback",       "above", None),
    ("pm_ripple",        "Lyneis-Ford_2007_PM-survey",           r"Fig\.?\s*3\.?\s*Policy resistance",          "above", None),
    ("croads_overview",  "Sterman_2013_C-ROADS",                 r"Fig\.?\s*1\.?\s*C-ROADS Overview",           "above", None),
    ("zhang_sfd",        "Zhang_2021_building-stock-Jinan",      r"Figure 2\. Stock and flow",                  "above", None),
    ("weee_sfd",         "WEEE_2018_kobe-WP",                    r"Fig 2\. WEEE management",                    "above", None),
    ("muller_ironcycle", "Muller_2006_iron-cycles_PNAS",         r"Fig\.?\s*5\.?\s*The U\.S\. iron cycle",      "above", None),
    ("lotka_fig13",      "Lotka_1925_Elements-Physical-Biology", r"FIG\.\s*13",                                 "page", 118),
    ("lotka_fig14",      "Lotka_1925_Elements-Physical-Biology", r"FIG\.\s*14",                                 "page", 119),
    ("gordon_fig4",      "Gordon_1954_fishery",                  r"FIG\.\s*4",                                  "above", None),
    ("gordon_fig6",      "Gordon_1954_fishery",                  r"FIG\.\s*6",                                  "above", None),
    ("fiddaman_carbon",  "Fiddaman_1997_thesis",                 r"Figure 68",                                  "below", 115),
]

def page_words(pdf, page):
    html = subprocess.run(["pdftotext", "-bbox", "-f", str(page), "-l", str(page), str(pdf), "-"],
                          capture_output=True, text=True).stdout
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', html):
        x0, y0, x1, y1, w = float(m[1]), float(m[2]), float(m[3]), float(m[4]), m[5]
        out.append((x0, y0, x1, y1, w))
    return out

def find_page(pdf, regex, hint, max_pages=400):
    n = int(subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
            .stdout.split("Pages:")[1].split()[0])
    if hint:
        return hint if re.search(regex, subprocess.run(
            ["pdftotext", "-f", str(hint), "-l", str(hint), str(pdf), "-"],
            capture_output=True, text=True).stdout, re.I) else None
    for i in range(1, min(n, max_pages) + 1):
        if re.search(regex, subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), str(pdf), "-"],
                                           capture_output=True, text=True).stdout, re.I):
            return i
    return None

def trim(im, pad=12, thresh=245):
    g = ImageOps.grayscale(im)
    bbox = g.point(lambda p: 0 if p > thresh else 255).getbbox()
    if not bbox: return im
    x0, y0, x1, y1 = bbox
    return im.crop((max(0, x0-pad), max(0, y0-pad), min(im.width, x1+pad), min(im.height, y1+pad)))

for name, stem, regex, mode, hint in FIGURES:
    pdf = LIB / f"{stem}.pdf"
    if not pdf.exists(): print(f"SKIP {name}: no pdf"); continue
    page = find_page(pdf, regex, hint) if regex else hint
    if not page: print(f"SKIP {name}: no caption page"); continue
    words = page_words(pdf, page)
    # group words into rows (merge rows within 4pt), then match caption against row text
    raw = {}
    for w in words: raw.setdefault(round(w[1], 0), []).append(w)
    ys = sorted(raw)
    merged, cur = [], []
    for y in ys:
        if cur and y - cur[-1] <= 4: cur.append(y)
        else:
            if cur: merged.append(cur)
            cur = [y]
    if cur: merged.append(cur)
    rows = {}
    for grp in merged:
        ws = [w for y in grp for w in raw[y]]
        rows[min(w[1] for w in ws)] = sorted(ws, key=lambda w: w[0])
    cap_line = None; cap_key = None
    for y in sorted(rows):
        if re.search(regex, " ".join(w[4] for w in rows[y]), re.I):
            cap_line = rows[y]; cap_key = y; break
    if not cap_line: print(f"SKIP {name}: caption line not matched on p{page}"); continue
    cap_top = min(w[1] for w in cap_line); cap_bot = max(w[3] for w in cap_line)
    cap_x0, cap_x1 = min(w[0] for w in cap_line), max(w[2] for w in cap_line)
    # all rows dict for walking (skip the caption row itself)
    body_rows = {y: ws for y, ws in rows.items() if y != cap_key}
    # column bounds: narrow caption -> crop its column only
    png = TMP / f"{name}_p{page}"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(DPI), "-png", str(pdf), str(png)], check=True)
    im = Image.open(sorted(TMP.glob(f"{name}_p{page}-*.png"))[0])
    if mode in ("above", "below"):
        def row_stats(ws):
            return sum(w[2]-w[0] for w in ws), len(ws)
        cap_mid = (cap_x0 + cap_x1) / 2 * S
        left = cap_mid < im.width / 2
        colrows = {y: [w for w in ws if ((w[0]+w[2])/2*S < im.width/2) == left]
                   for y, ws in body_rows.items()}
        colrows = {y: ws for y, ws in colrows.items() if ws}
        col_width_pt = max((max(w[2] for w in ws) - min(w[0] for w in ws)) for ws in colrows.values())
        if mode == "above":
            boundary_pt, prev_top = 0.0, cap_top
            for y in sorted(colrows, reverse=True):
                if y >= cap_top - 2: continue
                ws = colrows[y]
                width_pt, n = row_stats(ws)
                dense = n >= 6 or width_pt >= 0.55 * col_width_pt
                if dense and prev_top - max(w[3] for w in ws) > GAP_PT:
                    boundary_pt = max(w[3] for w in ws) + 2; break
                if not dense: prev_top = min(w[1] for w in ws)
            top_px = int(max(0, boundary_pt*S - 6)); bot_px = int(cap_bot*S + 10*S)
        else:  # below: figure follows the caption
            boundary_pt, prev_bot = im.width and 10000.0, cap_bot
            for y in sorted(colrows):
                if y <= cap_bot + 2: continue
                ws = colrows[y]
                width_pt, n = row_stats(ws)
                dense = n >= 6 or width_pt >= 0.55 * col_width_pt
                if dense and min(w[1] for w in ws) - prev_bot > GAP_PT:
                    boundary_pt = min(w[1] for w in ws) - 2; break
                if not dense: prev_bot = max(w[3] for w in ws)
            top_px = int(cap_top*S - 6); bot_px = int(min(im.height, boundary_pt*S + 4)) if boundary_pt < 9999 else im.height
        band = ImageOps.grayscale(im.crop((0, top_px, im.width, bot_px)))
        inkbb = band.point(lambda p: 0 if p > 245 else 255).getbbox()
        if inkbb:
            ix0, iy0, ix1, iy1 = inkbb
            crop = im.crop((max(0, ix0-10), top_px + max(0, iy0-8), min(im.width, ix1+10), bot_px))
        else:
            crop = im.crop((0, top_px, im.width, bot_px))
    else:
        crop = im
    crop = trim(crop)
    dest = OUT / f"{name}.png"
    crop.save(dest)
    ink = sum(1 for p in ImageOps.grayscale(crop).get_flattened_data() if p < 128) / (crop.width*crop.height)
    print(f"{'OK ' if ink > 0.004 else 'EMPTY?'} {name}: p{page} {crop.size} ink={ink:.1%}")
