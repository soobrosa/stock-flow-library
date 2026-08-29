# Poietic-MCP Build Cases from the Stock-and-Flow Bibliography

48 modelable cases from `system-dynamics-stock-flow-sources.md` and the PDFs in
`stock-flow-library/`, expressed as Poietic build recipes.

**Fidelity tags:**
- `[full-text]` — extracted from the actual paper/book (PDF in the library; verified equations/parameters)
- `[canonical]` — re-specified from the standard documented structure of a well-known model (text not in library)

**Now in the library as full text** (Anna's Archive haul, 2026-08-29): Sterman 2000 *Business
Dynamics* (1008 pp), Forrester 1961 *Industrial Dynamics* (480 pp), Forrester 1969 *Urban
Dynamics* (scan), Meadows 1972 *Limits to Growth*, Meadows 2008 *Thinking in Systems* (epub),
Godley & Lavoie 2007 *Monetary Economics* (2nd ed., 575 pp). Book-derived case upgrades:
A1–A6 are now `[full-text]`-anchored (G&L's Model SIM equations in ch. 3, pp. 103–108).

Legend: stocks **[S]**, flows **[F]**, auxiliaries **[A]**. ⚠ = needs aging-chain/cohort pattern
(Poietic has no arrays). GF = graphical function.

---

## A. Core textbooks

### A1. Industrial Dynamics — Forrester (1961) `[canonical]`
1. **Inventory–workforce oscillation**: [S] Inventory, Workforce, Backlog; [F] Production start (desired production smoothed by inventory-coverage gap), Hiring/Layoff (workforce gap / adjustment time), Order fulfillment; [A] desired inventory (weeks-of-supply × demand), delivery delay, productivity. Signature behavior: damped oscillation from the two nested negative loops (inventory → production; workforce → output) with delays.
2. **Advertising–sales loop**: [S] Sales backlog, Brand awareness; [F] orders, advertising spend; [A] ad budget as function of backlog (GF), awareness decay. Reinforcing loop: sales → profit → ads → awareness → orders.

### A2. Urban Dynamics — Forrester (1969) `[full-text]` ⚠ (scan; OCR-mined)
3. **City model**: [S] Premium housing, Worker housing, Underemployed(slum) housing (3-level housing chain) · New enterprise, Mature business, Declining industry (3-level business chain) · Managerial-professional, Labor, Underemployed population (3-level people chain) — units: housing units / enterprise units / people (initials: PH 14,470 · WH 450,300 · UH 174,300 · MB 11,300 · DI 18,000 · MP 96,000 · L 530,800 · U 316,900).
   - [F] Housing: premium-housing construction, premium→worker obsolescence, worker-housing construction (direct), worker→underemployed obsolescence, low-cost-housing program creation, slum-housing demolition. Business: new-enterprise construction, new→mature aging, mature→declining aging, declining-industry demolition. People: arrival/departure rates per class (attractiveness-driven).
   - [A] Example rate law (Eq 82–84, p. 96–97): `WHC.KL = (WHCN)(WH.K)·WHM.K` — worker-housing construction = normal rate × existing stock (area-size proxy) × multiplier WHM, which bundles WHAM (adequacy: labor/worker-housing ratio GF), WHUM (labor/underemployed GF), tax, land, and enterprise multipliers. Perceive-and-act delays on attractiveness (perceived AMMP = smoothed AMM). Job multipliers from employment mixes: a new-enterprise unit employs 4 managers + 20 labor + 10 underemployed.
   - Signature behavior: growth → stagnation → decay as land fills and structures age; the classic policy paradoxes (slum demolition → more underemployed, not less). Diagram: `figures/urban_dynamics_fig2-4.png` (nine levels, 22 rates, three subsystems).

### A3. Study Notes — Goodman (1974) `[canonical]`
4. **Coffee/commodity price stabilizer**: [S] commodity inventory; [F] harvest (weather-perturbed), consumption; [A] price = f(inventory-to-consumption ratio) GF — steeply convex; optional [S] buffer-stock held by stabilization authority, release/purchase flows. Oscillator + policy dampener.
5. **Thermostat/room heating**: [S] room temperature; [F] heat flow to outside (proportional to T_in − T_out), furnace heat input (on/off via threshold logic); [A] desired temperature, insulation coefficient. Simplest control-loop starter.
6. **Predator–prey exercise**: same as case 38 (Lotka) with Goodman's pedagogical parameter set.

### A4. Limits to Growth / World3 — Meadows et al. (1972) `[canonical]` ⚠
7. **World3 core**: [S] Population (4-stage cohort chain: 0-14, 15-44, 45-64, 65+), Industrial capital, Service capital, Agricultural inputs (capital share), Arable land, Land fertility, Persistent pollution, Nonrenewable resource; [F] births/deaths (life-expectancy GF of health services, food, pollution), capital investment/discard (desired growth vs depreciation), pollution generation/assimilation (GF with delay), resource extraction (capital × yield GF); [A] food per capita (land × inputs / population GF), industrial output per capita, technology adaptation switches. Full build ~40 stocks/auxiliaries.
8. **World3 subsystem (Population + Capital + Resource)**: same loop skeleton, 1/5 size: [S] Population, Capital, Resource; [F] births, deaths, investment, discard, extraction; [A] output per capita, resource yield GF, desired capital growth.

### A5. Thinking in Systems — Meadows (2008) `[canonical]` (ch.2 already a repo fixture)
9. **Bathtub**: [S] water volume; [F] inflow, outflow. Chapter 1 teaching case; smoke test.
10. **Capital plant** (the `capital.test.mjs` fixture; Meadows ch.2 Figs 42–45): [S] capital; [F] investment (gross = depreciation + desired growth — the net-rate trap), depreciation; [A] desired growth rate, depreciation fraction.
11. **Fishing fleet economy**: [S] fish, fleet capital; [F] regeneration (density GF), harvest (catch per boat GF), fleet investment (profit-driven); [A] price as scarcity GF, profit → gross investment. README's example build.
12. **Renewable vs nonrenewable resource extraction**: [S] resource stock, capital; [F] regeneration or discovery (discovery = exploration capital × remaining-fraction GF), extraction; [A] yield-per-capital GF declining with stock; behavior: overshoot-and-collapse (renewable w/ slow regeneration) vs peak-and-decline (nonrenewable).

### A6. Business Dynamics — Sterman (2000) `[canonical]`
13. **Beer Game chain** ⚠: [S] Inventory + Backlog + Supply line (orders in transit) at retailer, wholesaler, factory; [F] shipments (min of desired, available), orders; [A] anchor-and-adjust order policy: desired production = forecast demand + inventory-gap correction + supply-line correction. Build as 3 copies connected; lesson: supply-line neglect → oscillation amplification up the chain.
14. **Workforce–overtime management**: [S] Workforce, Backlog; [F] hiring (delay via training pipeline stock), work accomplishment; [A] overtime fraction (schedule-pressure GF), fatigue GF reducing effective productivity.
15. **Word-of-mouth market growth**: [S] Potential adopters, Adopters; [F] adoption = advertising (p·Potential) + WOM (q·Adopters/N·Potential, contact-rate GF on market saturation); = Bass (case 33) with marketing lever.
16. **Drug development pipeline** ⚠: [S] Molecules in discovery, preclinical, phase I, II, III (aging chains with attrition), Approved drugs on market; [F] phase advancement, phase-failure attrition (per-phase success fraction), market exit (patent expiry); [A] R&D effort allocation (gap-driven), NPV of pipeline.

### A7. Modeling the Environment — Ford (2009) `[canonical]`
17. **Columbia River reservoir operations**: [S] reservoir storage; [F] inflow (seasonal time series), turbine release, spill; [A] power output = head(flow, storage GF) × flow × efficiency, flood-control rule curve GF (max storage by season), demand for firm power. Literal hydraulics, GF showcase.
18. **Salmon lifecycle** ⚠: [S] eggs, fry, smolts, ocean adults, spawning adults; [F] hatching, smolting, ocean migration, harvest, spawning return, dam passage mortality (fraction per dam × n dams); [A] hatchery input policy.
19. **Climate box model**: [S] atmospheric CO2, earth surface temperature; [F] emissions (exogenous scenario), absorption (Revelle-buffer GF), radiative cooling (σT⁴ vs absorbed forcing); [A] forcing = ln(GF of CO2 concentration). DICE-lite skeleton, cf. case 40.

### A8. Analytical Methods for Dynamic Modelers — Rahmandad/Oliva/Osgood (2015) `[canonical]`
20. **Calibration exercise**: take case 10 or 33; add [A] simulated-vs-measured error, run parameter sweeps via `poietic_run` (multiple runs, minimizing error); the "case" is the workflow, not new structure.

---

## B. Civil engineering & infrastructure

### B1. Project management
21. **Rework cycle** `[full-text]` — Lyneis & Ford 2007 (§2.2; originally Cooper 1980/1993; PDF in library):
   - [S] `Work to Do` (all work starts here) · `Work Done` (correct, terminal) · `Undiscovered Rework` (done-with-errors, invisible to management) · `Rework to Do` (discovered backlog). Units: tasks or person-hours of work.
   - [F] Work accomplishment (effort × productivity) → splits by **error fraction** into Work Done vs Undiscovered Rework; Rework discovery (downstream work or testing; delayed months/years) moves Undiscovered → Rework to Do; Rework doing returns items through the cycle recursively.
   - [A] Controlling loops (their Fig 2): expected completion delay = work remaining/time remaining vs time-to-deadline → **Add People** (hiring), **Work More** (overtime), **Work Faster** (intensity), **Deadline slip**, **gold-plating** (slack → unnecessary features).
   - [A] Ripple effects (their Fig 3 — the policy-resistance core): hiring → experience dilution → lower productivity; overtime → fatigue → lower productivity *and* higher error fraction; faster work → higher error fraction → more rework. Implement dilution/fatigue/error as GFs.
   - Key trap (paper §3): perceived progress = Work Done + Undiscovered Rework (managers count undiscovered as done) → overestimate progress early, underestimate late.
22. **Change/rework management** `[canonical]` — Park & Peña-Mora 2003: case 21 + [S] Change orders pending/approved; [F] change initiation (client-driven), change approval, change-induced rework. Distinguishes error rework from change rework.
23. **Software project dynamics** `[canonical]` — Abdel-Hamid & Madnick 1991: case 21 skeleton + [S] Personnel in training, Experienced personnel; [F] hiring, training completion, turnover (morale GF); [A] schedule pressure, morale.
24. **Ship production** `[canonical]` — Cooper 1980 (Interfaces): case 21 parameterized to the Litton shipyard data (work-months of tasks, error rate ~5-10%, discovery delay ~months, overtime/dilution loops active).

### B2. Building stock & materials
25. **Dwelling stock by cohort** `[canonical]` — Müller 2006 (Ecological Economics) / Bergsdal 2007: [S] Dwellings by age cohort (chain, e.g., 10-yr classes); [F] construction inflow, cohort outflow (demolition via lifetime survival GF), [A] stock-driven demand: desired stock = population × dwellings-per-capita (saturating GF of income) → gap → construction start. The "in-use stock drives flows" archetype; same math as case 46.
26. **Material embodied in buildings** `[canonical]` — Pauliuk et al. 2017 (JIE): case 25 + [S] steel/concrete mass per cohort (parallel chains or one chain with material-intensity auxiliary); [F] material inflow with construction, outflow with demolition → EOL scrap → recycling loop back to production; [A] recycling yield GF, material intensity per m² by building type.
27. **Urban residential stock with policy** `[full-text]` — Zhang et al. 2021 (Jinan; PDF in library, §6.2 below).

### B3. Asset management & traffic
28. **Pavement deterioration & rehabilitation** `[canonical]` — ASCE JIS 2015-style: [S] Pavement area in good/fair/poor condition (3-stage chain); [F] deterioration (condition-index GF: load + weather), rehabilitation (budget-driven, resets poor→good), [A] maintenance budget (gap-driven), rehab cost per m² by condition GF, user cost. Pair with case 47.
29. **Traffic queue / congestion** `[canonical]` — Abbas & Bell 1994: [S] Vehicles in network zone; [F] inflow (demand: generation + mode choice), outflow (capacity = speed-density GF); [A] rush-hour demand profile (time GF), induced demand (travel time → trip generation). Congestion as accumulating queue.
30. **Reservoir/dam operations**: = case 17.

---

## C. Household appliances & durables

31. **Appliance efficiency substitution** `[canonical]` — JORS 1995: [S] Installed standard appliances, Installed efficient appliances; [F] new purchases (split by price premium vs lifetime-savings decision), replacement (failure via lifetime), efficiency-upgrade purchases; [A] electricity demand (stock × unit consumption), price premium vs electricity price GF, payback period. Substitution dynamics + residential demand.
32. **Appliance ownership diffusion** `[full-text]` — McNeil et al. 2010 (LBNL; PDF in library, §6.3 below).
33. **Bass diffusion** `[canonical]` — Bass 1969: [S] Potential adopters (N), Adopters; [F] adoption = p·Potential + q·(Adopters/N)·Potential. Two stocks, one flow. Defaults: p≈0.03, q≈0.38. The cleanest diffusion case; also case 20's calibration target.
34. **WEEE / e-waste system** `[full-text]` — Guo, Wang, Nie & Shen 2017/18 (Kobe RIEB WP = JCP paper; PDF in library, §6.4 below).
35. **Car fleet & scrappage** `[canonical]` — Chow 1957 / Greenspan-Cohen 1999 (PDF in library): [S] Registered cars by vintage (cohort chain); [F] new sales, scrappage (survival GF of age: ~zero before 3 yr, 50% at 12-13 yr); [A] ownership target = households × %owning × avg-per-owning (income GF) → desired stock → gap → sales. Detailed spec in §6.7.

---

## D. The twelve other domains (PDF-backed)

36. **SIR epidemic** `[full-text]` — Kermack & McKendrick 1927 (PDF in library, §6.6 below). Flagship: threshold density N₀ = ℓ/κ; epidemic peaks exactly when S falls to N₀.
37. **SFC household sector** `[full-text]` — Tobin 1969 + Nikiforos & Zezza 2017 (PDFs in library, §6.7 below).
38. **Predator–prey** `[full-text]` — Lotka 1925 (PDF in library, §6.5 below).
39. **Gordon–Schaefer fishery** `[full-text]` — Gordon 1954 (PDF in library, §6.8 below). Open-access tragedy of commons.
40. **DICE-lite / FREE** `[full-text]` — Fiddaman 1997 thesis (PDF in library, §6.9 below); C-ROADS equations documented in Sterman 2013 (PDF in library, §6.9 below).
41. **Nash cascade reservoirs** `[canonical]` — Nash 1957 / Sugawara 1961: [S] water in N serial linear reservoirs (N=2–4); [F] outflow = k·storage each (k = 1/time constant), rainfall input (time series or pulse); [A] unit hydrograph output at last stage. Hydrology's native stock-flow model; calibrate k to match a measured hydrograph.
42. **Leslie cohort population** `[full-text]` — Leslie 1945 (PDF in library, §6.8 below; brown-rat worked example with all 42 matrix values).
43. **Pharmacokinetics** `[canonical]` — Teorell 1937 / Gibaldi & Perrier 1982: [S] drug in gut, drug in plasma (+ tissue for 2-cmt); [F] absorption (first-order k_a), elimination (Cl/V·C); [A] dosing schedule (single/repeat pulse via time-dependent input), volume of distribution V, clearance Cl. 1:1 compartmental conversion; verify C-t curve against one-compartment analytic solution.
44. **CSTR reactor** `[canonical]` — Luyben 1996 / Fogler 2016: [S] tank volume, reactant mass; [F] feed in, effluent out, reaction consumption (rate = k₀·exp(−E/RT)·C^order GF); [A] concentration, temperature (energy balance with cooling-jacket heat removal), residence time. Process control canonical; add temperature feedback loop (jacket flow on temp error).
45. **Multi-echelon inventory** `[full-text]` — Clark & Scarf 1960 (PDF in library, §6.10 below; discrete DP → SD ordering policy).
46. **MESSAGE capacity vintages** `[full-text]` — Messner & Strubegger 1995 (PDF in library, §6.10 below).
47. **Markov reliability states** `[canonical]` — Billinton & Allan 1992 / Rausand & Høyland 2004: [S] Units operating, Units failed; [F] failure (λ·operating), repair (μ·failed); [A] availability = operating/(operating+failed), expected outage cost. Pairs with case 28 (deterioration as slow failure loop).
48. **Anthropogenic iron cycle** `[full-text]` — Müller et al. 2006 PNAS (PDF in library, §6.11 below).

---

## 6. Full-text extracted recipes

### 6.1 Rework Cycle — Lyneis & Ford 2007 (case 21)
See case 21 for the complete four-stock structure, control loops, and ripple-effect GFs, extracted from the paper's §2.2 and Figures 1–3.

### 6.2 Jinan Urban Residential Building Stock — Zhang et al. 2021 (case 27) `[full-text]`
Built in Stella Architect; from their Table 1 + Fig 2:
- **Stocks (4):** `BC stock` (brick-concrete) · `SC stock` (steel-concrete) · `BW stock` (brick-wood) · `Total residential stock` = sum. Units: m². Initials: PCFA 4.06 m², urban population 1.81 M.
- **Key auxiliaries:** `Urban population` (exogenous time series) · `PCFA` — desired stock ≈ P(t)·PCFA(t); new-construction split: `BC ratio` 74.79%, `SC ratio` 20.21%, `S ratio` (remainder).
- **Flows:** new construction (demand-driven gap + replacement of demolished), demolition, refurbishment rate.
- **Impact auxiliaries:** recycling rates (steel scrap / brick-concrete / glass), combustible (incineration) rate → annual energy use, CO2, C&D waste.
- **Causal loop:** stock(+)→C&D waste(−)→recycled material(−)→demand for new construction.
- **Policy experiments (§4):** raising C&D recycling rates dominates; A1/B1 scenario pairs → `poietic_run` parameter sweeps.

### 6.3 Appliance Diffusion — McNeil et al. 2010 (case 32) `[full-text]`
LBNL logistic method, per appliance and country:
- **Eq 1:** `Diff_c = α / (1 + γ·exp(β_inc·I_c + β_elec·E_c + β_urb·U_c))` — logistic in income `I = GDP/households`, electrification `E` (0–1), urbanization `U` (0–1), β ≤ 0; scaled by saturation `α`.
- **Saturation α:** refrigerators 1.4 (above Australia's 1.26) · washing machines 1.0 · TVs 3.0 (above US 2.49) · air conditioners = `ClimateMaximum(CDD)` GF; for AC: `Diff = Availability(I) × ClimateMaximum(CDD)`.
- **Stock-flow:** [S] Appliances owned; [F] purchases = Diff(t+1)·HH − Diff(t)·HH + scrappage; [F] scrappage via service life; optional [S] hoarded second units.
- Poietic: logistic = Auxiliary with `EXP`; ClimateMaximum = GF; country = parameter set.

### 6.4 WEEE Management System — Guo, Wang, Nie & Shen 2017/18 (case 34) `[full-text]`
Vensim DSS model; from their Fig 2 + Eqs 1–9. Note: their stocks are mostly **monetary**:
- **Stocks (5):** `Producer Profit` · `Processor Profit` · `Consumer Profit` · `Processing Fund` · `Household Appliance Inventory` (units).
- **Flows:** sales revenue in (S·SP), levy on producer out (S·LPU), recycled-material revenue in (ARM·RMP), subsidy out (FR·SPU), processor cost out (FR·PUPC). **Eq 9:** `PF = ∫(LProd + LoC − SoP)dt`.
- **Scrapping (Eq 7, inventory-coefficient approach):** `AHAS(t) = HAI(t)·η/(n − HASL + 1)`, n = 16-yr max service life, η = 0.6 (no consumer levy) or 0.4 (with levy); `HASL` shifts m₁→m₂ years when consumers pay levies (fridge +2 yr — the behavioral lever).
- **Channels:** scrapping splits into `Formal Recycling` vs `Informal Recycling` (peddlers pay consumers more; formal gets subsidy); `FRR = FR/scrapping` evaluates policy.
- **Scenarios:** producer levy vs consumer levy vs processor subsidy; historical fit 2013–15 (Theil/MAPE, refrigerators).
- Poietic: the levy→price→sales feedback (LPU raises sales price) is the one endogenous loop worth encoding.

### 6.5 Predator–Prey — Lotka 1925 (case 38) `[full-text]`
From Elements of Physical Biology, ch. VIII + collision derivation (pp. 88–95, 359–360):
- **Stocks:** [S] `X₁` prey/food species; [S] `X₂` predator/feeding species (individuals; optional mass).
- **Flows:** prey net growth `r₁·X₁` (r₁ = b₁ − d₁, births minus non-predation deaths); **kills `k·X₁·X₂`** — one shared flow draining prey and filling predator (mass-action collision law: k = c·v·area-per-individual; "must vanish with either X₁ or X₂"); predator deaths `r₂·X₂`.
- **Parameters:** r₁, r₂ (1/time), k (1/(individual·time)). Parasitoid variant: predator births = K·N₁·N₂ with K = k·k′ (hatch fraction k′ < 1).
- **Dynamics:** neutrally stable closed orbits, period T = 2π/√(r₁·d₂) near equilibrium; equilibrium N₁ = d₂/K, N₂ = r₁/k. Expect slight numerical damping in a stock-flow integrator (tool artifact).
- **Refinement (their eq. 28):** k = α₀ + β·N₁ (density-dependent capture) → damped spiral (their fig. 14).
- Three-species extension (eq. 44): add [S] X₃ (second prey) with kill flow h·X₂·X₃ — note Lotka's result: a second prey species *can* drive the first extinct.

### 6.6 SIR — Kermack & McKendrick 1927 (case 36) `[full-text]`
The general model is age-of-infection-structured; the constant-rate special case (§10) is the classic SIR:
- **Stocks:** [S] `x` susceptible, [S] `y` infectious (ill), [S] `z` removed (recovered + dead) — persons/area; conservation x + y + z = N.
- **Flows:** Infection `κ·x·y` (mass-action); Removal `ℓ·y` (recovery + death).
- **Threshold:** density N₀ = ℓ/κ — no epidemic if N ≤ ℓ/κ; epidemic peaks when x falls to ℓ/κ; ends with susceptibles left. Final size: −log(x∞/N) = A·N·p.
- **Empirical anchor:** Bombay plague 1905–06, deaths z = 890·sech²(0.24(t − 3.4)) per week.
- Poietic: 3 stocks suffice; expose N₀ = ℓ/κ as an auxiliary; optional refinement — chain 2–3 Infectious stocks to capture the paper's c₀ = 0 (no infectivity at moment of infection) delay.

### 6.7 SFC Monetary Block — Tobin 1969 + Nikiforos & Zezza 2017 (case 37) `[full-text]`
**Tobin (Model I, money–capital):**
- **Stocks:** [S] `K` physical capital; [S] `M/p` real money; wealth constraint `W = qK + M/p`.
- **Market clearing:** `f₁(r_R, r_M, Y/W)·W = qK`; `f₂(...)·W = M/p` (one redundant — drop one); rates: `r_R·q = R` (marginal efficiency), `r_M = r_M′ − π_pe`.
- **Investment lever:** "the rate of investment … should be related, if to anything, to **q**" — capital flows respond to market-vs-replacement value.
- Comparative-static signs in his Table 2 validate any SD implementation.
**Nikiforos & Zezza (canonical SFC behavioral set):**
- Consumption `C = α·YD + c·V_(−1)` (eq. 6); investment `I/K = γ₀ + γ₁·Π/K + γ₂·q + γ₃·u` (eq. 7); portfolio shares `λ = λ₀ + λ_R·R + λ_YD·(YD/W)` with adding-up (Σλ = 1, column sums zero) (eq. 8); wealth-norm saving `ΔV = s·[β·YD − V_(−1)]` (eq. 9).
- Accounting: stocks as levels, FoF rows as flows, Σ sectoral net lending = 0, drop one redundant identity per matrix; three balances: NL_private + NL_govt + NL_foreign = 0.
- Poietic build: start with household sector (deposits [S], loans [S], consumption/income/interest flows) then add firms' capital account; enforce the adding-up constraints in auxiliaries.

### 6.8 Leslie Cohorts — Leslie 1945 (case 42) `[full-text]`
Brown-rat worked example (monthly steps, 21 age classes, reproduction span 3–21 months):
- **Recurrence:** `n_{x+1,t+1} = P_x·n_{x,t}`; `n_{0,t+1} = Σₓ F_x·n_{x,t}` — first row fertility, subdiagonal survival.
- **Full parameter set (their Table 5):** P₀=0.94697 … P₁₉=0.91649, P₂₀=0.0035; F₀=F₁=0, F₂=0.3964, F₃=1.4989, F₄=2.1777, F₅=2.5250, F₆=2.6282, F₇=2.6749 (peak), F₈=2.6018, … F₁₉=0.0901, F₂₀=0.0022.
- **Derived:** net reproduction R₀ = 25.66; intrinsic growth r = 0.44565/month; stable distribution: 74.45% under 3 months.
- Poietic: 21 stocks is heavy — lump classes 0–1 (prereproductive), 2–19 (reproductive, keep ~10 classes), 20+ (post-reproductive); aging rate = 1/class-width per month; deaths = −ln(P_x)·n_x; births = Σ F_x·n_x into class 0. Validate against R₀ and the stable distribution.

### 6.8 Car Fleet — Greenspan & Cohen 1999 (case 35) `[full-text]`
FEDS methodology (annual, cars/trucks separate):
- **Identity (Eq 1):** `Sales = ΔV + EngineeringScrappage + CyclicalScrappage`.
- **Stock driver:** `V_HH = households × %owning × avg-per-owning` (cars: avg = 1·%1 + 2·%2 + 3.1·%≥3; trucks: 1·%1 + 2.1·%≥2); 1995 values: 100.6 M households, 83.1% own cars, 37.4% trucks → 171 M vehicles.
- **Engineering scrappage:** per-vintage survival `ln y_it = a + b_i·t² + c·t³` (right half of normal density); b_i improves −0.01611 (1960) → −0.00600 (1986); c = 1.195e−4; age at 50% survival: 10 yr (1960s) → 13 (1977–79); trucks >15 yr.
- **Cyclical scrappage:** `−4.3 − 0.38·RU + 0.31·RU_(−1) + 9.3·(PR/PN) − 0.05·PG` (unemployment, repair-vs-new price ratio, gas price; adj R²=.70).
- **COEFF model for b_i:** `−0.02 − 0.0007·EPA + 4e−6·TEEN + 0.0003·TIME` (R²=.95).
- Poietic: cohort chain with cohort-specific scrappage fractions from the b_i/c fit; cyclical-scrappage GF on oldest cohorts. 1995 validation: ΔV 3.4 + Eng 11.1 + Cyc 0.8 = 15.3 M sales (actual 15.3).

### 6.9 C-ROADS — Sterman et al. 2013 (case 40b) `[full-text]`
Full equation set printed in the paper (evolved from FREE):
- **Carbon stocks:** Atmosphere · Biomass · Soils (humus) · Mixed Layer (100 m) · Deep Ocean (4 layers: 300/300/1300/1800 m) — GtC.
- **Key equations:** NPP = NPP0·(1 + βC·ln(Ca/Ca0))·(1 − βTL·ΔT); mixed-layer equilibrium Cm = Cm*·(Ca/Ca0)^(1/ξ) with Revelle ξ = ξ0 + dβ·ln(Ca/Ca0) and solubility Cm* = Cm0·(1 − βTO·ΔT); ocean diffusion dC_ij/dt = ε·(d_ij/d̄)·(C_i/d_i − C_j/d_j); forcing F = γ·ln(Ca/Ca0); heat dHm/dt = F_T − R − diffusion, R = (γ·ln2/S)·ΔT; sea level dSLR/dt = (a0 + bI)·(ΔT − ΔT0) + a1·dΔT/dt.
- **Feedbacks:** βTL, βTO, βM, βP (permafrost), bI — all zero in base case, user-settable (switchable parameters).
- **Fit:** CO2 R²=0.995 (RMSE 2.25 ppm); ΔT RMSE 0.13 °C.
- Poietic build ladder: atmosphere + mixed layer only → + biosphere/soils → + 2-3 deep-ocean layers → + heat stocks.

### 6.10 MESSAGE III capacity vintages — Messner & Strubegger 1995 (case 46) `[full-text]`
IIASA User's Guide (equations are images; transcribed from notation definitions):
- **Structure:** installed capacity of technology v = historic capacity h(t,v) + Σ of annual additions Y_τ still within plant life `pll` (e.g., 30 yr); activity z ≤ plant factor `plf` × installed capacity (per load region).
- **Growth constraints (market-penetration limits):** `Y_t ≤ (1+γ)·Y_(t−1)·(Δt/Δt−1) + gy` and symmetric lower bound — the standard diffusion-speed limit.
- **Construction:** no explicit under-construction stock in the LP (investment is time-distributed via `discon`: equal/logistic/polynomial shares); `lag` = years between input and output.
- Poietic: FIFO aging chain of capacity cohorts (one stock per period or year), inflow = new installations (demand-gap driven, growth-constrained), retirement after pll years; add a Construction pipeline stock (ordered → installed after lead time) for the SD version; total capacity = sum of cohorts.

### 6.11 Anthropogenic Iron Cycle — Müller et al. 2006 PNAS (case 48) `[full-text]`
US 1900–2004, top-down MFA (units Tg Fe):
- **Stocks:** Products in use 3,200 Tg (Construction 1,600; Machinery & Appliances 750; Transportation 650; Others 200) · obsolete-products stock (unmeasured, confounded with exports) · landfills ~700 Tg · tailings ~600 Tg · slag ~100 Tg · lithosphere: reserves 2,100 Tg, reserve base 4,600 Tg.
- **Flows (2000):** into use 124 Tg/a (mining 38 + net imports 54.1 + scrap 52.5 → pig iron 53, raw steel 107, finished 111); obsolete generation 77 Tg/a (Eq 1: `X^ObsD(t) = ∫ L_s(t,t′)·X^NewD(t′)dt′` — convolution with normal lifetime distribution, Eq 2: `L = [1/(σ√2π)]·exp(−(t−t′−τ)²/2σ²)`); scrap collected 57 Tg/a; landfills 20; tailings 15.
- **Lifetime parameters (τ/σ, yr):** Construction 50/75/100 (σ=20) · Transportation 15/20/30 (σ=7.5) · M&A 20/30/40 (σ=10) · Others 10/15/20 (σ=5).
- **Per-capita in-use stock:** saturates ~11–12 Mg/person (1980).
- Poietic: four parallel chains (Con/Tra/M&A/Oth) with cohort exits from the normal lifetime distributions; approximate the convolution with an aging chain of width ~σ/2 (25-yr cohorts for Construction, 5–10 for others); the "engine": in-use stock drives demand (replacement + growth), EOL outflow feeds scrap recycling loop (yield GF).

---

## Quick picks

- **Smoke tests (1–2 stocks):** bathtub (9), Bass (33), SIR (36), PK one-compartment (43).
- **Graphical-function showcases:** coffee stabilizer (4), reservoir (17), appliance diffusion (32), fishery (39), Nash cascade (41).
- **Aging-chain/cohort stress tests ⚠:** Urban Dynamics (3), World3 (7), dwelling stock (25), WEEE (34), Leslie (42), iron cycle (48).
- **Already in the repo:** Capital model (case 10) is the `capital.test.mjs` fixture; fishing economy (11) is the README example.
- **Full-text specs available (15):** cases 21, 27, 32, 34, 35, 36, 37, 38, 39, 40, 42, 45, 46, 48 + C-ROADS in 6.9 — from PDFs in `stock-flow-library/`.
- **Calibration data anchors:** Bombay plague fit (6.6), Jinan parameters (6.2), Leslie Table 5 (6.8), 1995 US vehicle sales (6.8), C-ROADS fit metrics (6.9), iron-cycle lifetimes (6.11).

### 6.12 Model SIM — Godley & Lavoie 2007, ch. 3 (upgrades case 37) `[full-text]`
The complete simplest SFC model, from pp. 103–108 (balance sheet p. 104, transactions matrix p. 105, equations in Appendix 3.1):
- **Balance-sheet stocks:** [S] household money H_h, household bills B_h, household wealth V (identity: V = H_h + B_h); [S] government/central-bank consolidated: bills B_s = H_s + B_cb.
- **Transactions-flow matrix (households, govt, production, CB):** consumption −C/+C; govt spending +G/−G; taxes −T/+T; bill interest r·B_(−1) across sectors.
- **Behavioral set:** C = α₁·YD + α₂·V_(−1); T = θ·Y; YD = Y − T + r·B_(−1); bill demand B_h/V = λ₀ + λ_r·r − λ_Y·(YD/V); money residual: ΔH = ΔB_s − ΔB_h.
- **Dynamics:** Y = G + C (+ money closure). Steady state: Y* = G/θ.
- Poietic build: household money/bills stocks + government bills; purely linear; validate Y* = G/θ and ΔV = 0 in steady state. Figures: `figures/gl_sim_balance.png`, `figures/gl_sim_tfm.png`.
