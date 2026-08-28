#!/usr/bin/env python3
"""Generate SVG stock-and-flow diagrams for the flagship cases in poietic-mcp-cases.md.

Dependency-free: emits SVG directly. Every diagram is defined as a small layout
dict (stocks, flows, auxiliaries with grid positions). Regenerate with:

    python3 gen_diagrams.py

Diagrams are original renderings of the documented model structures (not scans
of published figures) and are committed to the repo.
"""
import html, pathlib

W, H = 760, 300
BW, BH = 118, 40          # stock box size

def svg_header():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">\n'
            f'<rect width="{W}" height="{H}" fill="white"/>\n'
            '<defs><marker id="arr" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">'
            '<path d="M0,0 L9,3.5 L0,7 z" fill="#111"/></marker></defs>\n')

def stock(x, y, label):
    cx, cy = x + BW/2, y + BH/2
    return (f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="4" fill="#fff" stroke="#111" stroke-width="1.6"/>\n'
            f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12.5" fill="#111">{html.escape(label)}</text>\n')

def flow(x1, y1, x2, y2, label="", valve_at=None, dashed=False):
    da = ' stroke-dasharray="5,4"' if dashed else ''
    s = (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#111" stroke-width="1.5" '
         f'marker-end="url(#arr)"{da}/>\n')
    if valve_at:
        vx, vy = valve_at
        s += (f'<rect x="{vx-9}" y="{vy-9}" width="18" height="18" fill="#fff" stroke="#111" stroke-width="1.5" '
              f'transform="rotate(45 {vx} {vy})"/>\n')
        if label:
            s += f'<text x="{vx}" y="{vy-15}" text-anchor="middle" font-size="12" fill="#111">{html.escape(label)}</text>\n'
    return s

def aux(x, y, label):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="12" fill="#333">{html.escape(label)}</text>\n')

def arrow_pts(points, label="", dashed=False):
    da = ' stroke-dasharray="5,4"' if dashed else ''
    p = points
    s = f'<polyline points="{" ".join(f"{x},{y}" for x,y in p)}" fill="none" stroke="#555" stroke-width="1.3"{da}/>\n'
    if label:
        mx, my = p[len(p)//2]
        s += f'<text x="{mx+6}" y="{my-6}" font-size="11" fill="#555">{html.escape(label)}</text>\n'
    return s

def wrap(title, body):
    return svg_header() + f'<text x="{W/2}" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#111">{html.escape(title)}</text>\n' + body + '</svg>\n'

DIAGRAMS = {}

# 9. Bathtub
b = stock(320, 150, "Water volume")
body = flow(150, 170, 320, 170, "inflow", valve_at=(215, 170))
body += flow(438, 170, 640, 170, "outflow", valve_at=(540, 170))
body += aux(215, 210, "faucet") + aux(540, 210, "drain")
DIAGRAMS["bathtub"] = wrap("9. Bathtub (Thinking in Systems ch.1)", body + b)

# 10. Capital
b = stock(320, 140, "Capital")
body = flow(150, 160, 320, 160, "investment = depr + desired growth", valve_at=(215, 160))
body += flow(438, 160, 620, 160, "depreciation = fraction * Capital", valve_at=(540, 160))
body += arrow_pts([(500, 200), (215, 200)], "net-rate trap: gross, not net")
DIAGRAMS["capital"] = wrap("10. Capital plant (Meadows ch.2)", body + b)

# 33. Bass
b = stock(180, 140, "Potential adopters")
b2 = stock(470, 140, "Adopters")
body = flow(298, 160, 470, 160, "adoption = p*P + q*A/N*P", valve_at=(380, 160))
body += arrow_pts([(560, 140), (560, 80), (380, 80), (240, 80), (240, 140)], "word of mouth (q)")
DIAGRAMS["bass"] = wrap("33. Bass diffusion (1969)", body + b + b2)

# 36. SIR
b = stock(120, 150, "Susceptible")
b2 = stock(340, 150, "Infectious")
b3 = stock(560, 150, "Removed")
body = flow(238, 170, 340, 170, "infection = kappa*S*I", valve_at=(289, 170))
body += flow(458, 170, 560, 170, "removal = ell*I", valve_at=(509, 170))
body += aux(380, 120, "threshold N0 = ell / kappa")
DIAGRAMS["sir"] = wrap("36. SIR, constant-rate case (Kermack & McKendrick 1927 §10)", body + b + b2 + b3)

# 21. Rework cycle
b = stock(70, 90, "Work to Do")
b2 = stock(300, 90, "Work Done")
b3 = stock(300, 210, "Undiscovered Rework")
b4 = stock(60, 210, "Rework to Do")
body = flow(188, 110, 300, 110, "accomplish (error fraction)", valve_at=(240, 110))
body += flow(359, 130, 359, 210, "error split", valve_at=(359, 170))
body += flow(359, 230, 178, 230, "discovery (delayed)", valve_at=(268, 230))
body += arrow_pts([(129, 210), (129, 130)], "rework doing")
body += aux(240, 70, "productivity, error fraction (GF: overtime, dilution)")
DIAGRAMS["rework_cycle"] = wrap("21. Rework cycle (Cooper 1980; Lyneis & Ford 2007 Fig.1)", body + b + b2 + b3 + b4)

# 43. PK one-compartment
b = stock(200, 150, "Drug in gut")
b2 = stock(470, 150, "Drug in plasma")
body = flow(318, 170, 470, 170, "absorption = ka*Gut", valve_at=(390, 170))
body += flow(588, 170, 690, 170, "elimination = (Cl/V)*Plasma", valve_at=(640, 170))
DIAGRAMS["pk_one_cmt"] = wrap("43. One-compartment PK (Teorell 1937; Gibaldi & Perrier)", body + b + b2)

# 39. Fishery
b = stock(300, 140, "Fish biomass")
b2 = stock(300, 40, "Fishing effort")
body = flow(150, 160, 300, 160, "growth = r*P*(1-P/a)", valve_at=(215, 160))
body += flow(418, 160, 570, 160, "harvest = c*E*P", valve_at=(490, 160))
body += flow(360, 80, 360, 140, "effort entry/exit = k*(L-C)", valve_at=(360, 110))
body += arrow_pts([(490, 180), (240, 40)], "revenue per effort")
DIAGRAMS["fishery"] = wrap("39. Gordon-Schaefer fishery (Gordon 1954 + Schaefer growth)", body + b + b2)

# 42. Leslie cohorts (compressed)
b = stock(80, 140, "Age 0-1")
b2 = stock(250, 140, "Age 1..")
b3 = stock(420, 140, "Age ..m")
b4 = stock(590, 140, "Post-repr")
body = flow(198, 160, 250, 160, "", valve_at=(224, 160))
body += flow(368, 160, 420, 160, "", valve_at=(394, 160))
body += flow(538, 160, 590, 160, "", valve_at=(564, 160))
body += flow(360, 120, 139, 120, "births = sum(Fx*nx)", valve_at=(250, 120))
body += aux(470, 90, "deaths = -ln(Px)*nx per class")
DIAGRAMS["leslie_chain"] = wrap("42. Leslie cohorts as aging chain (Leslie 1945 Table 5)", body + b + b2 + b3 + b4)

# 48. Iron cycle
b = stock(280, 120, "Iron in use (Tg)")
b2 = stock(80, 40, "Lithosphere ore")
b3 = stock(560, 120, "Scrap / EOL")
body = flow(200, 60, 310, 120, "fabrication inflow", valve_at=(255, 90))
body += flow(398, 140, 560, 140, "end-of-life = lifetime convolution", valve_at=(480, 140))
body += arrow_pts([(600, 120), (620, 220), (120, 220), (120, 80)], "scrap recycling loop (yield GF)")
body += arrow_pts([(340, 200), (340, 250), (660, 250), (660, 150)], "demand: replacement + growth")
DIAGRAMS["iron_cycle"] = wrap("48. Anthropogenic iron cycle (Muller et al. 2006 PNAS)", body + b + b2 + b3)

# 25. Dwelling stock
b = stock(300, 140, "Dwellings by cohort (chain)")
body = flow(150, 160, 300, 160, "construction = f(desired - actual, replacement)", valve_at=(215, 160))
body += flow(418, 160, 600, 160, "demolition = survival GF of age", valve_at=(500, 160))
body += aux(380, 100, "desired stock = population * dwellings per capita (GF of income)")
DIAGRAMS["dwelling_stock"] = wrap("25. Dwelling stock cohorts (Muller 2006; Bergsdal 2007)", body + b)

# 13. Beer game echelon
b = stock(120, 150, "Retailer inventory")
b2 = stock(380, 150, "Wholesaler inventory")
b3 = stock(620, 150, "Factory inventory")
body = flow(238, 170, 380, 170, "orders (anchor-and-adjust)", valve_at=(309, 170), dashed=True)
body += flow(498, 170, 620, 170, "orders", valve_at=(559, 170), dashed=True)
body += arrow_pts([(180, 130), (180, 70), (680, 70), (680, 130)], "shipments downstream")
body += aux(370, 240, "policy: demand + inventory gap + supply-line correction")
DIAGRAMS["beer_chain"] = wrap("13. Beer Game supply chain (Sterman 1989/2000)", body + b + b2 + b3)

# 40b. C-ROADS carbon
b = stock(120, 60, "Atmosphere")
b2 = stock(120, 210, "Biomass")
b3 = stock(340, 210, "Soils")
b4 = stock(340, 60, "Mixed layer")
b5 = stock(560, 60, "Deep ocean (4 layers)")
body = flow(238, 230, 340, 230, "NPP / respiration", valve_at=(289, 230))
body += flow(238, 80, 340, 80, "uptake / release (Revelle)", valve_at=(289, 80))
body += flow(458, 80, 560, 80, "eddy diffusion", valve_at=(509, 80))
body += aux(560, 150, "emissions (scenario) into atmosphere")
DIAGRAMS["croads_carbon"] = wrap("40b. C-ROADS carbon cycle (Sterman et al. 2013 Eqs.1-5)", body + b + b2 + b3 + b4 + b5)

# 34. WEEE
b = stock(280, 140, "Appliance inventory")
b2 = stock(90, 40, "Producer profit")
b3 = stock(560, 40, "Processor profit")
body = flow(398, 160, 560, 160, "formal / informal split", valve_at=(480, 160))
body += flow(340, 120, 340, 60, "levy, subsidy flows", valve_at=(340, 90), dashed=True)
body += arrow_pts([(480, 180), (480, 240), (300, 240)], "scrapping = HAI*eta/(n-HASL+1)")
DIAGRAMS["weee"] = wrap("34. WEEE management system (Guo et al., Fig.2)", body + b + b2 + b3)

out = pathlib.Path(__file__).parent / "diagrams"
out.mkdir(exist_ok=True)
for name, svg in DIAGRAMS.items():
    (out / f"{name}.svg").write_text(svg)
    print(f"wrote diagrams/{name}.svg")
