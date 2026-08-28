# Poietic-MCP Build Cases from the Stock-and-Flow Bibliography

Every modelable case found in `system-dynamics-stock-flow-sources.md` and the PDFs in
`stock-flow-library/`, expressed as a Poietic build recipe: stocks, flows, key auxiliaries.
Books/Papers are sources to model from; PDFs (✓ in `stock-flow-library/`) are already on disk.

Legend: stocks **[S]**, flows **[F]**, auxiliaries/parameters **[A]**.
⚠ = needs an aging-chain or cohort pattern (Poietic has no arrays — use separate linked stocks).
GF = graphical function (nonlinear lookup).

---

## A. Core textbooks

### A1. Industrial Dynamics — Forrester (1961)
1. **Inventory–workforce oscillation**: [S] Inventory, Workforce, Backlog; [F] Production start, Hiring/Layoff, Order fulfillment; [A] desired inventory coverage, delivery delay. The founding case.
2. **Advertising–sales loop**: [S] Sales backlog; [A] ad budget as function of backlog (GF).

### A2. Urban Dynamics — Forrester (1969) ⚠
3. **City model**: [S] New housing, Middle housing, Slum housing (aging chain), Business structures ×3, Population by skill class ×3; [F] construction, aging/decay, demolition, migration; [A] land as fixed constraint, attractiveness multipliers. The archetype cohort/aging-chain case.

### A3. Study Notes in System Dynamics — Goodman (1974)
4. **Coffee/commodity price stabilizer**: [S] commodity inventory; [F] harvest, consumption; [A] price via inventory-coverage GF. Classic oscillator with policy (buffer stock) experiments.
5. **Thermostat/room heating**: [S] room temperature; [F] heat flow; [A] thermostat on/off logic. Simplest control-loop starter case.
6. **Predator–prey exercise**: [S] rabbits, foxes; [F] births, deaths by predation (GF for encounter rate).

### A4. Limits to Growth / World3 — Meadows et al. (1972) ⚠
7. **World3 core**: [S] Population (cohort chain), Industrial capital, Agricultural capital, Pollution, Nonrenewable resource, Land fertility; [F] births/deaths, investment/depreciation, pollution generation/assimilation, resource extraction; [A] persistent-pollution GFs, adaptive technology switches. The big multi-day build.
8. **World3 subsystem**: just Population + Capital + Resource — same loop structure at 1/5 the size.

### A5. Thinking in Systems — Meadows (2008)
9. **Bathtub**: [S] water; [F] inflow, outflow. Chapter 1's teaching case; ideal smoke test (the repo's smoke.mjs territory).
10. **Capital plant** (already a fixture in `capital.test.mjs`): [S] capital; [F] investment, depreciation; [A] net-growth trap (gross vs net rate — the README's lesson).
11. **Fishing fleet economy**: [S] fish, fleet capital; [F] regeneration (density GF), harvest (catch per boat GF), fleet investment; [A] price as scarcity GF, profit → investment. The README's example build.
12. **Renewable vs nonrenewable resource extraction**: [S] resource stock, capital; [F] discovery (nonrenewable) or regeneration (renewable), extraction; [A] yield-per-capital GF declining with stock.

### A6. Business Dynamics — Sterman (2000)
13. **Beer Game / supply chain chain** ⚠: [S] Inventory at retailer/wholesaler/factory, Backlog, Supply line (orders in transit); [F] shipments, ordering; [A] anchor-and-adjust order policy. Serially connected — build as three planes or three copies.
14. **Workforce–overtime management**: [S] Workforce, Backlog; [F] hiring (with delay), production; [A] overtime fraction, fatigue GF.
15. **Market growth with word of mouth (Bass-like)**: [S] Potential adopters, Adopters; [F] adoption (advertising term + WOM term, contact-rate GF).
16. **Drug development pipeline** ⚠: [S] Molecules in discovery/preclinical/clinical phases (aging chain with attrition rates), Approved drugs; [F] phase advancement, failure attrition.

### A7. Modeling the Environment — Ford (2009)
17. **Columbia River reservoir operations**: [S] reservoir storage; [F] inflow, release (through-turbine and spill); [A] power output GF (head × flow), flood-control rule curves. Literal hydraulics; GFs shine here.
18. **Salmon lifecycle** ⚠: [S] eggs, fry, smolts, adults; [F] hatching, migration, harvest; [A] dam mortality fractions.
19. **Climate box model**: [S] atmospheric CO2, earth temperature; [F] emissions, absorption, radiative balance (GF).

### A8. Analytical Methods for Dynamic Modelers — Rahmandad/Oliva/Osgood (2015)
20. **Calibration case**: any of the above + [A] measured-vs-simulated gap; exercise is using `poietic_run` parameter sweeps, not new structure.

---

## B. Civil engineering & infrastructure

### B1. Project management
21. **Rework cycle** (Lyneis & Ford 2007; Cooper 1980 shipyard ✓-related literature): [S] Work to do, Work done, Undiscovered rework, Known rework; [F] work accomplishment, error discovery, rework generation; [A] productivity vs overtime GF, schedule pressure. *The* construction-PM case; Cooper's shipyard is its famous instance.
22. **Change/rework management** (Park & Peña-Mora 2003): adds [S] Change orders pending/approved to case 21.
23. **Software project dynamics** (Abdel-Hamid & Madnick 1991): same skeleton as 21 plus [S] personnel in training; [A] morale/turnover loops.
24. **Ship production** (Cooper 1980 — the Interfaces paper): case 21 parameterized to the Litton shipyard data.

### B2. Building stock & materials
25. **Dwelling stock by cohort** (Müller 2006 ✓-literature; Bergsdal 2007) ⚠: [S] Dwellings by age cohort (chain), [F] new construction inflow, cohort outflow (demolition, lifetime distribution), [A] stock-driven construction demand (in-use stock per capita target → gap → construction). The paper is literally a stock-flow model in Ecological Economics dress.
26. **Material embodied in buildings** (Pauliuk 2017): case 25 plus [S] steel/concrete mass per cohort; [F] material inflow with construction, outflow with demolition (EOL recycling loop).
27. **Urban residential stock with policy** (Zhang 2021; Håkansson 2020): case 25 + [A] renovation and energy-standard split (efficient vs inefficient sub-stocks).

### B3. Asset management & traffic
28. **Pavement deterioration & rehabilitation** (ASCE J. Infrastructure Systems 2015): [S] Pavement in good/fair/poor condition (chain); [F] deterioration (condition-index GF), rehabilitation (budget-driven); [A] maintenance budget, cost GF by condition.
29. **Traffic queue / congestion** (Abbas & Bell 1994): [S] Vehicles in network zone (queue); [F] inflow (demand), outflow (capacity GF); [A] demand generation, rush-hour profile (time GF).
30. **Reservoir/dam operations** (Ford): case 17.

---

## C. Household appliances & durables

31. **Appliance efficiency substitution** (JORS 1995) ⚠: [S] Installed standard appliances, Installed efficient appliances; [F] new purchases, replacement, failure; [A] electricity demand, price premium vs efficiency GF.
32. **Appliance ownership diffusion** (McNeil 2010): [S] Households without appliance, Households owning appliance; [F] purchase flow via Gompertz/logistic GF of income per capita. Direct from the LBNL methodology.
33. **Bass diffusion** (Bass 1969): [S] Potential adopters, Adopters; [F] adoption = p·Potential + q·(Adopters/N)·Potential. Two stocks, one flow — cleanest possible diffusion case.
34. **WEEE / e-waste system** (J. Cleaner Production 2018; van Schaik & Reuter 2009) ⚠: [S] EEE in-use stock (cohort chain), Hoarded/discarded stock, Formal-recycled, Informal flows; [F] sales, end-of-first-life, hoard-release, collection (collection-rate GF), recycling yield GF.
35. **Car fleet & scrappage** (Chow 1957; Greenspan & Cohen 1999 ✓): [S] Registered cars by vintage; [F] new sales, scrappage (survival-probability GF of age); [A] GDP per capita → ownership target GF.

---

## D. The twelve "other source" domains (all ✓-PDF-backed)

36. **SIR epidemic** (Kermack & McKendrick 1927 ✓): [S] Susceptible, Infectious, Recovered; [F] infection (contact-rate GF × prevalence), recovery; [A] N conservation check. The three-stock flagship.
37. **SFC household sector** (Godley & Lavoie 2007; Tobin 1969 ✓; Nikiforos & Zezza 2017 ✓): [S] Household deposits, Loans outstanding; [F] wage income, consumption, interest payments, borrowing; [A] propensity to consume. The *Prophet* (simplest) SFC model from Godley-Lavoie ch.3.
38. **Predator–prey** (Lotka 1925 ✓; Goodman ex.6): [S] prey biomass, predator biomass; [F] prey birth, predation (Holling GF), predator death.
39. **Gordon–Schaefer fishery** (Gordon 1954 ✓): [S] fish biomass, fishing effort (boats); [F] natural growth (logistic GF), harvest (catchability × effort × stock), entry/exit of effort (profit-driven); [A] price, unit cost. Open-access tragedy-of-commons experiment. (Overlaps case 11 — build both, different feedback emphasis.)
40. **DICE-lite** (Nordhaus 1994; Fiddaman 2002; Sterman 2013 ✓): [S] atmospheric carbon, capital, temperature anomaly; [F] emissions (capital × intensity), decay, heat uptake; [A] damage function GF, abatement cost GF.
41. **Nash cascade reservoirs** (Nash 1957 ✓; Sugawara 1961): [S] water in N serial linear reservoirs; [F] outflow = k·storage each; [A] rainfall input time-series. Hydrology's native stock-flow model.
42. **Leslie cohort population** (Leslie 1945 ✓; Preston 2001; Rogers 1995) ⚠: [S] population by 5-year age class (chain of, say, 16 stocks); [F] aging flows, age-specific birth flows into class 0, death flows; [A] fertility schedule GF, survival GF. Converts the Leslie matrix directly.
43. **One-compartment pharmacokinetics** (Gibaldi & Perrier 1982 ✓; Teorell 1937; Reddy 2005 ✓): [S] drug in gut, drug in plasma; [F] absorption (first-order), elimination (clearance); [A] dosing schedule (pulse/repeat). Extend to two-compartment with peripheral tissue stock.
44. **CSTR reactor** (Luyben 1996; Fogler 2016; Ramkrishna 2000 ✓): [S] tank volume, reactant mass; [F] feed in, effluent out, consumption (Arrhenius GF); [A] concentration, temperature with cooling jacket. Process control's canonical case.
45. **Multi-echelon inventory** (Clark & Scarf 1960 ✓; Sterman 1989): case 13's two-echelon version with echelon stock policies.
46. **MESSAGE capacity vintages** (Messner & Strubegger 1995 ✓; IEA 2009) ⚠: [S] generation capacity by technology vintage (coal/gas/renewable chains); [F] new investment (demand-gap + policy driven), retirement (lifetime); [A] electricity demand growth, capacity factor GF.
47. **Markov reliability states** (Billinton & Allan 1992; Rausand & Høyland 2004; Barlow & Proschan 1975 ✓): [S] Units operating, Units failed/under repair; [F] failure rate, repair rate; [A] availability index. Pairs naturally with case 28 (deterioration = slow failure loop).
48. **Anthropogenic iron cycle** (Müller 2006 ✓ PNAS; Brunner & Rechberger 2016; Pauliuk & Müller 2014 ✓): [S] iron in-use stock (cohort chain), scrap/trash stock; [F] fabrication inflow (GDP-driven GF), end-of-life outflow (lifetime distribution), scrap recycling loop; [A] recycling yield GF. The downloaded PNAS paper is a ready specification sheet.

---

## Quick picks

- **Smoke tests (1–2 stocks):** bathtub (9), Bass (33), SIR (36), PK one-compartment (43).
- **Graphical-function showcases:** coffee stabilizer (4), reservoir (17), appliance diffusion (32), fishery (39), Nash cascade (41).
- **Aging-chain/cohort stress tests ⚠:** Urban Dynamics (3), World3 (7), dwelling stock (25), WEEE (34), Leslie (42), iron cycle (48).
- **Already in the repo:** Capital model (case 10) is the `capital.test.mjs` fixture; fishing economy (11) is the README example.
- **PDFs on disk ready to model from:** Kermack 1927, Leslie 1945, Lotka 1925, Tobin 1969, Clark-Scarf 1960, Nash 1957, Gordon 1954, Greenspan-Cohen 1999, Müller 2006, Rahmandad-Sterman 2008, Nikiforos-Zezza 2017, Messner 1995, Sterman 2013, plus the two book scans.

---

## 6. Full-text extracted recipes (from PDFs in `stock-flow-library/`)

These five cases were re-specified from the actual paper text (pdftotext mining, 2026-08-28).
Structures below are the authors' own stock-flow diagrams and equations, ready for
`build_stock_and_flow_model`.

### 6.1 Rework Cycle — Lyneis & Ford 2007 (§2.2 of the paper; upgrades case 21)
From "the most important single feature of system dynamics project models" (originally Cooper 1980/1993):

- **Stocks (4):** `Work to Do` (all work starts here) · `Work Done` (correct work, terminal) · `Undiscovered Rework` (done-with-errors, invisible to management) · `Rework to Do` (discovered backlog).
- **Flows (4):** Work accomplishment (effort × productivity) → splits by error fraction into Work Done vs Undiscovered Rework; Rework discovery (downstream work or testing, delayed by months/years) moves Undiscovered → Rework to Do; Rework doing sends items back through the cycle (recursive: rework can generate rework).
- **Controlling loops (Fig 2):** expected completion delay = work remaining/time remaining − time to deadline drives three negative loops: **Add People** (hiring), **Work More** (overtime), **Work Faster** (intensity/productivity); plus **Deadline slip** (move the target) and the **gold-plating** variation (slack → unnecessary features).
- **Ripple effects (Fig 3, the policy-resistance core):** hiring → experience dilution → lower productivity; overtime → fatigue → lower productivity *and* higher error fraction; faster work → higher error fraction → more rework. Model these as GFs on error fraction and productivity.
- Poietic notes: needs the aging-chain pattern (Undiscovered → discovered is a material delay with discovery fraction); perceived progress = Work Done + Undiscovered (managers count undiscovered as done — overestimates progress early, underestimates late).

### 6.2 Jinan Urban Residential Building Stock — Zhang et al. 2021 (upgrades case 27)
Built in Stella Architect; structure from their Table 1 + Fig 2:

- **Stocks (4):** `BC stock` (brick-concrete) · `SC stock` (steel-concrete) · `BW stock` (brick-wood) · `Total residential stock` = sum, in m².
- **Key auxiliaries:** `Urban population` (exogenous time series, starts 1.81M) · `PCFA` per-capita floor area (starts 4.06 m²) — desired stock ≈ P(t)·PCFA(t); new construction split by `BC ratio` (74.79%), `SC ratio` (20.21%), `S ratio`.
- **Flows:** new construction (demand-driven: gap between desired stock and total stock, plus replacement of demolished), demolition, refurbishment rate.
- **Impact auxiliaries:** recycling rates for steel scrap / brick-concrete / glass, combustible (incineration) rate → annual energy use, CO2, and C&D waste generation.
- **Policy experiments (their §4):** raising C&D recycling rates dominates other levers; A1/B1 scenario pairs. In Poietic: parameter sweep the recycling rates via `poietic_run`.
- Causal loops to encode: stock(+→)C&D waste(−)recycled material(−)demand for new construction (recycled-material substitution loop).

### 6.3 Appliance Diffusion — McNeil et al. 2010 (upgrades case 32)
The LBNL logistic method, per appliance and country:

- **Core equation (Eq 1):** `Diff_c = α / (1 + γ·exp(β_inc·I_c + β_elec·E_c + β_urb·U_c))` — logistic in income `I = GDP/households`, electrification `E` (0–1), urbanization `U` (0–1), with β ≤ 0; scaled by saturation `α`.
- **Saturation levels α:** refrigerators 1.4 · washing machines 1.0 · TVs 3.0 · air conditioners = `ClimateMaximum(CDD)` (cooling-degree-days GF). For AC: `Diff = Availability(I) × ClimateMaximum(CDD)`.
- **Stock-flow:** `Appliances owned` [S]; `purchases` [F] = Diff(t+1)·households − Diff(t)·households + scrappage; `scrappage` [F] via service life; optional `Stock hoarded` for second units.
- In Poietic the logistic is an Auxiliary with `EXP` — one GF for ClimateMaximum; country = parameter set.

### 6.4 WEEE Management System — Guo, Wang, Nie & Shen 2017/18 (upgrades case 34)
Vensim DSS model; structure from their Fig 2 + Equations 1–9:

- **Stocks (5):** `Producer Profit` · `Processor Profit` · `Consumer Profit` · `Processing Fund` · `Household Appliance Inventory` (units).
- **Flows:** sales revenue in (S·SP), levy on producer out (S·LPU), recycled-material revenue in (ARM·RMP), subsidy out (FR·SPU), processor cost out (FR·PUPC); Processing Fund = ∫(LProd + LoC − SoP)dt.
- **Scrapping equation (Eq 7, inventory-coefficient approach):** `AHAS(t) = HAI(t) · η / (n − HASL + 1)` with n = 16-year max service life, η = 0.6 (no consumer levy) or 0.4 (with levy); `HASL` shifts m₁→m₂ years when consumers pay levies (e.g. fridge +2 years — the model's behavioral lever).
- **Channels:** scrapping splits into `Formal Recycling` vs `Informal Recycling` (peddlers pay consumers more; formal recycler gets subsidy); `FRR` formal recovery rate = FR/scrapping evaluates policy efficiency.
- **Scenario set:** producer levy vs consumer levy vs processor subsidy (policies 1–3); outputs = economic (profits, fund) + environmental (formal vs informal treatment volumes).
- Poietic notes: no arrays needed; the levy→price→sales feedback (LPU raises sales price) is the one endogenous loop worth encoding.

### 6.5 FREE Integrated Climate-Economy Model — Fiddaman 1997 thesis (upgrades case 40)
Full Vensim equation listing in the thesis appendix — the richest single spec sheet in the library:

- **Carbon cycle (5 reservoirs, their Figure 68):** `CO2_in_Atmos = INTEG(CO2_Net_Emiss − CO2_Storage, 6.77e11)`; `CO2_in_Mixed_Layer` (ocean surface); `CO2_in_Deep_Ocean[layer]` — 10 diffusion layers, `Diffusion_Flux[upper] − Diffusion_Flux[lower]`; `CO2_in_Biomass`; `CO2_in_Humus`. In Poietic: model deep ocean as 3–5 serial stocks (drop to 1st-order for the smoke test).
- **Temperature:** `Atmos_UOcean_Temp = INTEG(Chg_A_UO_Temp)` (mixed layer), `Deep_Ocean_Temp = INTEG(Chg_DO_Temp, 0.1)`; `Adapted_Temperature[Damage] = INTEG(Adaptation_Rate)` — society adapts to the temperature it is used to (the behavioral twist).
- **Economy:** `Capital = INTEG(Investment_Rate − Discard_Rate)`, Capital_Lifetime = 15 yr; `Energy_Capital[source] = INTEG(Completion − Discard)` fed by `Capital_under_Construction = INTEG(Order_Rate − Completion)` — a two-stage capital aging chain with construction delays (Poietic-friendly).
- **Energy/depletion:** `Resource_Remaining[nonrenewable] = INTEG(−Energy_Production)`; `Embodied_AEEI = INTEG(Install + Retrofit − Discard)` — energy efficiency physically embodied in capital vintages (the thesis's key structure; lock-in dynamics).
- **Other stocks:** `Population = INTEG(Net_Pop_Incr)` (0.0224 initial growth rate), `Factor_Productivity`, `Carbon_Tax = INTEG(Adj_Rate)`, `Cum_Disc_Utility`.
- Build ladder: (a) DICE-lite = Capital + CO2_in_Atmos + Temp; (b) + Energy_Capital chain + Resource_Remaining; (c) + Adapted_Temperature + Embodied_AEEI for the full behavioral story.
