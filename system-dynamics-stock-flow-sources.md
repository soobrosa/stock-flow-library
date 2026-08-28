# Books & Papers with System Dynamics (Stock-and-Flow) Models

A collection of sources that either (a) already contain stock-and-flow (system dynamics) models, or
(b) are **stock-and-flow convertible**: their formalism maps directly onto stocks (accumulations),
flows (rates), and auxiliary variables.

Legend: **[SD]** = native system dynamics / stock-flow model; **[C]** = convertible (different
formalism, but directly translatable to stocks and flows).

---

## 1. Core textbooks (the canonical model sources)

- Forrester, J.W. (1961). *Industrial Dynamics*. MIT Press. **[SD]** — the original: inventories, workforce, orders as stocks/flows.
- Forrester, J.W. (1969). *Urban Dynamics*. MIT Press. **[SD]** — housing, industry, and population as aging stocks; the grandfather of city/infrastructure SD.
- Alfeld, L.E. & Graham, A.K. (1976). *Introduction to Urban Dynamics*. Wright-Allen (Productivity Press). **[SD]** — worked urban models, exercises.
- Goodman, M.R. (1974). *Study Notes in System Dynamics*. MIT Press. **[SD]** — classic exercise book; every problem is a stock-flow diagram.
- Richardson, G.P. & Pugh, A.L. (1981). *Introduction to System Dynamics Modeling with DYNAMO*. MIT Press. **[SD]**.
- Randers, J. (ed.) (1980). *Elements of the System Dynamics Method*. MIT Press. **[SD]**.
- Meadows, D.H., Meadows, D.L., Randers, J., Behrens, W.W. (1972). *The Limits to Growth*. Universe Books. **[SD]** — World3: population, capital, pollution, resources as stocks.
- Meadows, D.H. (2008). *Thinking in Systems: A Primer*. Chelsea Green. **[SD]** — best conceptual intro to stocks vs flows.
- Sterman, J.D. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World*. Irwin/McGraw-Hill. **[SD]** — the standard reference textbook; chapters on supply chains, workforce, project management, all in stock-flow form.
- Ford, A. (2009). *Modeling the Environment*, 2nd ed. Island Press. **[SD]** — ecosystems, hydropower (Columbia River), climate; Vensim models included.
- Rahmandad, H., Oliva, R., Osgood, N. (2015). *Analytical Methods for Dynamic Modelers*. MIT Press. **[SD]** — includes optimization, calibration, spatial SD.

---

## 2. Civil engineering & infrastructure

### 2.1 Construction & project management
- Lyneis, J.M. & Ford, D.N. (2007). "System dynamics applied to project management: a survey, assessment, and directions for future research." *System Dynamics Review* 23(2-3): 157–189. **[SD]** — the entry-point survey for the field.
- Park, M. & Peña-Mora, F. (2003). "Dynamic change management for construction: introducing the change cycle into model-based project management." *System Dynamics Review* 19(3). **[SD]** — rework backlog as a stock.
- Abdel-Hamid, T. & Madnick, S. (1991). *Software Project Dynamics: An Integrated Approach*. Prentice-Hall. **[SD]** — software work as completed-work / undiscovered-error stocks; directly transferable to engineering task backlogs.
- Cooper, K.G. (1980). "Naval ship production: A claim settled and a framework built." *Interfaces* 10(6): 20–36. **[SD]** — famous shipbuilding model; progress, work-to-do, and rework stocks.
- Lyneis, J.M., Cooper, K.G., Els, S.A. (2001). "Strategic management of complex projects: a case study using system dynamics." *System Dynamics Review* 17(3): 237–260. **[SD]**.
- Franco, L.A. et al. (2019). "System dynamics modeling for construction management research: literature review and research agenda." *Journal of Civil Engineering and Management* 25(8). **[SD]** — bibliography aggregator; start here to mine dozens of individual models.
- *Building and infrastructure construction projects as complex systems* (2020). *Frontiers of Engineering Management* 7. **[SD]** — survey of SD in construction project planning/control.

### 2.2 Building stock, housing, materials (bridges to material-flow analysis)
- Forrester's *Urban Dynamics* (above) — housing stock by condition class (new/middle/aged), construction and demolition as flows. **[SD]**
- Bergsdal, H., Brattebø, H., Bohne, R.A., Müller, D.B. (2007). "Dynamic material flow analysis for Norway's dwelling stock." *Building Research & Information* 35(5): 557–570. **[C→SD]** — dwelling stock by age cohort, inflow construction, outflow demolition.
- Müller, D.B. (2006). "Stock dynamics for forecasting material flows—Case study for housing in The Netherlands." *Ecological Economics* 59(1): 142–156. **[C→SD]** — the seminal "in-use stock drives flows" paper.
- Zhang, X. et al. (2021). "A System Dynamics Model for Urban Residential Building Stock towards Sustainability." *Int. J. Environmental Research and Public Health* 18. **[SD]** — explicit SD of urban residential building stock (Jinan case).
- Håkansson, H. et al. (2020). "Developing a generic System Dynamics model for building stock transformation." *Energy and Buildings* 224. **[SD]** — building stock decarbonization.
- Pauliuk, S., Sprecher, B., Müller, D.B. et al. (2017). "Maintenance and Expansion: Modeling Material Stocks and Flows for Residential Buildings and Cars." *J. Industrial Ecology* 21(4). **[C→SD]**.

### 2.3 Infrastructure asset management, deterioration, funding
- *Holistic Analysis of Infrastructure Deterioration and Rehabilitation Systems* (2015). *J. Infrastructure Systems* (ASCE). **[SD]** — pavement/asset stocks with deterioration and rehabilitation flows.
- *Application of System Dynamics to Evaluate the Social and Economic Benefits of Transport Infrastructure Investment* (2017). *Systems* 5(2): 29 (MDPI). **[SD]**.
- Ford, A. (2001) and successors on Columbia River hydropower operations (in *Modeling the Environment*). **[SD]** — reservoirs are literal stocks.

### 2.4 Transportation & traffic
- Abbas, K.A. & Bell, M.G.H. (1994). "System dynamics applicable to road traffic." *System Dynamics Review* 10(1): 3–28. **[SD]** — the classic paper; congestion as accumulating queues.
- Daganzo, C.F. (2005+). Input–Output and MFD (Macroscopic Fundamental Diagram) traffic models. *Transportation Research B*. **[C→SD]** — vehicle accumulation in a network zone is a stock; inflow/outflow are flows.
- *System Dynamics for Sustainable Transportation Policies* (2021). **[SD]** — modern SD transport reviews.

---

## 3. Household appliances & consumer durables

### 3.1 Appliance stock, diffusion, energy demand
- *System Dynamics Modelling for Residential Energy Efficiency Analysis* (1995). *J. Operational Research Society* 46. **[SD]** — substitution of installed household appliances by efficient ones; appliance fleet as stock with replacement flow.
- McNeil, M.A. et al. (2010). "Modeling diffusion of electrical appliances in the residential sector." (LBNL; eScholarship/OSTI). **[C→SD]** — S-curve (Gompertz/logistic) appliance ownership per household; trivially convertible: potential owners → owners stocks.
- *A systems dynamics approach to the bottom-up simulation of residential electricity demand* (2021). *Energy and Buildings*. **[SD]** — appliance-level demand generation.
- *System Dynamics Modeling of Households' Electricity Consumption and Efficiency Investments* (2017+). **[SD]** — appliance purchase/retirement with efficiency policy scenarios.
- Bass, F.M. (1969). "A new product growth for model consumer durables." *Management Science* 15(5): 215–227. **[C→SD]** — the founding diffusion model; adopters and potential adopters are stocks.

### 3.2 Appliance end-of-life, e-waste, circularity
- *Profit or Environment? A System Dynamic Model Analysis of WEEE Management System in China* (2018). *J. Cleaner Production*. **[SD]** — EEE in-use stock, hoarded stock, formal/informal recycling flows.
- *Dynamic modelling of E-waste recycling system performance based on product life cycle* (2009). *Resources, Conservation and Recycling* / *Minerals Engineering* line of work (van Schaik & Reuter school). **[C→SD]** — appliance stocks with age-structured disposal flows; also see their SIMBox/thermodynamic recycling models.
- *System dynamics applied to the e-waste value chain: A Brazilian urban mining case* (2025). *Waste Management*. **[SD]**.
- Tasaki, T. et al. (2004+). "Element flow analysis of durables with lifetimes" (NIES Japan, appliances: TVs, fridges, washing machines). **[C→SD]**.

### 3.3 Durable-goods economics (older, very convertible tradition)
- Chow, G.C. (1957). *Demand for Automobiles in the United States*. North-Holland. **[C→SD]** — car stock, scrappage function, purchase flow.
- Stone, R. (1954). *The Measurement of Consumers' Expenditure and Behaviour in the United Kingdom*. **[C→SD]** — stock-adjustment models of durables.

---

## 4. Proposed other sources (high-yield domains)

Each of these fields is rich in stock-flow models or directly convertible:

### 1. Epidemiology / public health — [C→SD] (compartmental models map 1:1)
1. Kermack, W.O. & McKendrick, A.G. (1927). "A contribution to the mathematical theory of epidemics." *Proc. Royal Society London A* 115: 700–721. — the original SIR; three stocks (S, I, R), two flows. [Open PDF](https://royalsocietypublishing.org/rspa/article/115/772/700/2165/A-contribution-to-the-mathematical-theory-of-epidemics)
2. Anderson, R.M. & May, R.M. (1991). *Infectious Diseases of Humans: Dynamics and Control*. Oxford University Press. — the standard textbook of compartmental transmission models. [Publisher](https://global.oup.com/academic/product/infectious-diseases-of-humans-9780198540403)
3. Rahmandad, H. & Sterman, J.D. (2008). "Heterogeneity and network structure in the dynamics of diffusion: Comparing agent-based and differential equation models." *Management Science* 54(6): 998–1014. — the explicit bridge between SD and agent-based epidemic/diffusion models. [Open PDF](https://www.mit.edu/~jsterman/Rahmandad-Sterman_0512221.pdf)

### 2. Macroeconomics — Stock-Flow Consistent (SFC) models — [C→SD, arguably SD]
1. Godley, W. & Lavoie, M. (2007). *Monetary Economics: An Integrated Approach to Credit, Money, Income, Production and Wealth*. Edward Elgar. — the SFC bible; balance sheets as stocks, transactions-flow matrix as flows. [Archive.org (borrowable)](https://archive.org/details/monetaryeconomic0000godl)
2. Tobin, J. (1969). "A general equilibrium approach to monetary theory." *Journal of Money, Credit and Banking* 1(1): 15–29. — the root of stock-flow consistency in monetary theory. [Open PDF](https://mail.tku.edu.tw/niehcc/paper/T(1969-jmcb).pdf)
3. Nikiforos, M. & Zezza, G. (2017). "Stock-flow consistent macroeconomic models: A survey." *Journal of Economic Surveys* 31(5): 1204–1239. — the entry-point survey; hundreds of simulatable models inside. [Open PDF (Levy WP version)](https://www.levyinstitute.org/pubs/wp_891.pdf)

### 3. Ecology & resource management — [C→SD]
1. Lotka, A.J. (1925). *Elements of Physical Biology*. Williams & Wilkins. (with V. Volterra 1926) — predator–prey biomass stocks with birth/death/harvest flows. [Archive.org full scan](https://archive.org/details/elementsofphysic017171mbp)
2. Gordon, H.S. (1954). "The economic theory of a common-property resource: The fishery." *Journal of Political Economy* 62(2): 124–142. — Gordon–Schaefer fishery: biomass stock vs harvest flow; the classic renewable-resource model. [Open PDF](https://www.econ.ucsb.edu/~tedb/Courses/Ec100C/Readings/ScottGordonFisheries.pdf)
3. Odum, H.T. (1996). *Environmental Accounting: EMERGY and Environmental Decision Making*. Wiley. — whole notation for stocks/flows of energy and matter in ecosystems (see also his 1971 *Environment, Power, and Society*). [Publisher](https://www.wiley.com/en-us/Environmental+Accounting:+Emergy+and+Environmental+Decision+Making-p-9780471114420)

### 4. Climate & integrated assessment — [SD]/[C→SD]
1. Nordhaus, W.D. (1994). *Managing the Global Commons: The Economics of Climate Change*. MIT Press. — the DICE model: atmospheric carbon, capital, and temperature stocks. [Publisher](https://mitpress.mit.edu/9780262140553/managing-the-global-commons/)
2. Fiddaman, T.S. (2002). "Exploring policy options with a behavioral climate-economy model." *System Dynamics Review* 18(2): 317–345. — fully SD climate-economy model (from his 1997 MIT thesis). [DOI](https://doi.org/10.1002/sdr.241)
3. Sterman, J.D., Fiddaman, T., Franck, T., et al. (2013). "Management flight simulators to support climate negotiations." *Environmental Modelling & Software* 44: 122–135. — the C-ROADS stock-flow climate model. [Open PDF](https://img.climateinteractive.org/2014/01/C-ROADS-ENSO-2013.pdf)

### 5. Hydrology & water resources — [C→SD] (the most literal pre-Forrester stock-flow tradition)
1. Sugawara, M. (1961). "On the analysis of runoff structure about several Japanese rivers." *Japanese Journal of Geophysics* 2. — the "tank model": literal cascaded water stocks. (No open copy; verified via citations in later hydrology literature.)
2. Nash, J.E. (1957). "The form of the instantaneous unit hydrograph." *IASH Publication* 45(3): 114–121. — linear-reservoir cascade; level = stock, outflow = k·stock. [Open PDF](https://uon.sdsu.edu/FIUH_Nash_1957.pdf)
3. Stave, K.A. (2003). "A system dynamics model to facilitate public understanding of water management options in Las Vegas, Nevada." *System Dynamics Review* 19(4): 369–386. — native SD water-management exemplar. [DOI](https://doi.org/10.1002/sdr.260)

### 6. Demography & population — [C→SD]
1. Leslie, P.H. (1945). "On the use of matrices in certain population mathematics." *Biometrika* 33: 183–212. — Leslie matrix: age cohorts as stocks, birth/death as flows. [Open PDF](https://www.math.utah.edu/~keener/classes/math5110/papers/leslie.pdf)
2. Preston, S.H., Heuveline, P., Guillot, M. (2001). *Demography: Measuring and Modeling Population Processes*. Blackwell. — the standard cohort-component projection reference. [Publisher](https://www.wiley.com/en-us/Demography:+Measuring+and+Modeling+Population+Processes-p-9781557862143)
3. Rogers, A. (1995). *Multiregional Demography: Principles, Methods and Extensions*. Wiley. — cohorts + migration flows across regions; direct SD conversion. [Publisher](https://www.wiley.com/en-us/Multiregional+Demography%3A+Principles%2C+Methods+and+Extensions-p-9780471958925)

### 7. Pharmacokinetics / physiology — [C→SD]
1. Teorell, T. (1937). "Kinetics of distribution of substances administered to the body." *Archives Internationales de Pharmacodynamie* 57: 205–225. — the founding compartmental PK model. (No open copy; citation verified via secondary literature.)
2. Gibaldi, M. & Perrier, D. (1982). *Pharmacokinetics*, 2nd ed. Marcel Dekker. — the standard text; every model is compartments (stocks) and clearance (flows). [Archive.org (borrowable)](https://archive.org/details/pharmacokinetics15milo)
3. Reddy, M.B., Yang, R.S.H., Clewell, H.J., Andersen, M.E. (2005). *Physiologically Based Pharmacokinetic Modeling: Science and Applications*. Wiley. — the PBPK reference; organ compartments as physical stocks. [DOI](https://doi.org/10.1002/0471478768)

### 8. Chemical & process engineering — [C→SD]
1. Luyben, W.L. (1996). *Process Modeling, Simulation and Control for Chemical Engineers*, 2nd ed. McGraw-Hill. — tank levels, holdups, reactor concentrations as stocks. (Print only; no reputable open copy.)
2. Fogler, H.S. (2016). *Elements of Chemical Reaction Engineering*, 5th ed. Prentice Hall. — CSTR/batch/PFR mass balances; the accumulated-mass equation is a flow integral. [Official companion site (full supplementary chapters)](https://websites.umich.edu/~elements/5e/)
3. Ramkrishna, D. (2000). *Population Balances: Theory and Applications to Particulate Systems in Engineering*. Academic Press. — size/age distributions of particles as cohort stocks (same math as vintage models). [Publisher (ScienceDirect)](https://www.sciencedirect.com/book/9780125769600/population-balances)

### 9. Operations & supply chain — [SD]/[C→SD]
1. Sterman, J.D. (1989). "Modeling managerial behavior: Misperceptions of feedback in a dynamic decision making experiment." *Management Science* 35(3): 321–339. — the Beer Game: inventory stocks, order and backlog flows. [DOI](https://doi.org/10.1287/mnsc.35.3.321)
2. Hopp, W.J. & Spearman, M.L. (2011). *Factory Physics*, 3rd ed. McGraw-Hill. — Little's Law formalizes queue-as-stock (WIP) and throughput-as-flow. [Archive.org (1st ed., borrowable)](https://archive.org/details/isbn_9780025624795)
3. Clark, A.J. & Scarf, H. (1960). "Optimal policies for a multi-echelon inventory problem." *Management Science* 6(4): 475–490. — the founding multi-echelon inventory-stock model. [Open PDF (Yale)](http://dido.econ.yale.edu/~hes/pub/echelon1.pdf)

### 10. Energy systems & vehicle fleets — [C→SD] (same math as §2.2 building cohorts)
1. Greenspan, A. & Cohen, D. (1999). "Motorized stocks, scrappage, and sales." *The Energy Journal* 20(3): 1–22. — car stock, scrappage function, purchase flow. [Open PDF (FEDS working-paper version)](https://www.federalreserve.gov/pubs/feds/1996/199640/199640pap.pdf)
2. IEA (2009). *Transport, Energy and CO2: Moving toward Sustainability*. OECD/IEA. — the fleet-turnover methodology behind the IEA Mobility Model (MoMo). [IEA page](https://www.iea.org/news/transport-energy-and-co2-moving-toward-sustainability)
3. Messner, S. & Strubegger, M. (1995). *User's Guide for MESSAGE III*. IIASA WP-95-069. — power-generation capacity vintages with installation/retirement flows (the IAM stock-accounting standard; also the basis of TIMES/Veda accounting). [Open PDF (IIASA)](https://pure.iiasa.ac.at/id/eprint/4527/1/WP-95-069.pdf)

### 11. Reliability & maintainability engineering — [C→SD] (pairs with §2.3 deterioration)
1. Barlow, R.E. & Proschan, F. (1975). *Statistical Theory of Reliability and Life Testing*. Holt, Rinehart & Winston. — state-transition foundations. [Archive.org (borrowable)](https://archive.org/details/statisticaltheor0000barl)
2. Billinton, R. & Allan, R.N. (1992). *Reliability Evaluation of Engineering Systems*, 2nd ed. Plenum. — Markov availability models: operating/degraded/failed states as stocks. [Open PDF (Springer)](https://link.springer.com/content/pdf/10.1007/978-1-4899-0685-4.pdf)
3. Rausand, M. & Høyland, A. (2004). *System Reliability Theory: Models, Statistical Methods, and Applications*, 2nd ed. Wiley. — the modern reference; repair/renewal flows between state stocks. [Publisher (Wiley Online)](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119373940)

### 12. Material flow analysis / industrial ecology (whole field) — [C→SD] (dynamic MFA = SD in disguise)
1. Brunner, P.H. & Rechberger, H. (2016). *Handbook of Material Flow Analysis*, 2nd ed. CRC Press. — the MFA bible: every system is stocks connected by flows. [DOI](https://doi.org/10.1201/9781315313450)
2. Müller, D.B., Wang, T., Duval, B., Graedel, T.E. (2006). "Exploring the engine of anthropogenic iron cycles." *PNAS* 103(44): 16111–16116. — in-use metal stocks by cohort driving future flows. [Open PDF](https://www.pnas.org/doi/pdf/10.1073/pnas.0603375103)
3. Pauliuk, S. & Müller, D.B. (2014). "The role of in-use stocks in the social metabolism and in climate change mitigation." *Global Environmental Change* 24: 132–142. — the conceptual bridge from stock accounting to policy modeling. [DOI](https://doi.org/10.1016/j.gloenvcha.2013.11.002)

---

## 5. Where to keep mining

### 5.1 Collection status (as of 2026-08-28)

17 of the sources are downloaded as PDFs in `stock-flow-library/` (validated, named `Author_Year.pdf`):
Kermack-McKendrick 1927, Lotka 1925, Tobin 1969, Leslie 1945, Nash-era hydrology (Nash 1957 not obtained),
Clark-Scarf 1960, Gordon 1954, Greenspan-Cohen 1999, Sterman 2013 C-ROADS, Rahmandad-Sterman 2008,
Nikiforos-Zezza 2017, Messner-Strubegger 1995, Muller 2006 PNAS, Fiddaman 1997 MIT thesis,
McNeil 2010, WEEE 2018 (Kobe RIEB WP version of the JCP paper), Zhang 2021, Lyneis-Ford 2007.

Acquisition methods that worked: direct repository URLs (OSTI, IIASA, Levy, MIT DSpace API, Yale, UCSB,
UTah, Federal Reserve, Europe PMC `?pdf=render`, Royal Society via Wayback `web.archive.org/web/<year>id_/...`).
OpenAlex/Crossref API sweeps found green-OA copies automatically.

Acquisition methods that failed: Wiley/T&F/MDPI block curl AND headless Chromium
(`navigator.webdriver` triggers an unsolvable Cloudflare Turnstile loop; MDPI hard-blocks HeadlessChrome UA).
A headed agent-browser session + one human Turnstile click DID clear Wiley once (Lyneis-Ford downloaded),
but Wiley's session cookie did not persist across subsequent pdfdirect URLs. Springer has no bot wall but
those papers are paywalled outright.

Still missing (no legitimate open copy found; needs institutional access, Archive.org borrowing,
or author request): Abbas-Bell 1994, Anderson-May 1991, Barlow-Proschan 1975, Bergsdal 2007,
Billinton-Allan 1992, Brunner-Rechberger 2016, Cooper 1980, Forrester 1961/1969, Gibaldi-Perrier 1982,
Godley-Lavoie 2007, Hakansson 2020, Hopp-Spearman 2011 (3rd ed.), Luyben 1996, Meadows 1972/2008,
Nash 1957, Nordhaus 1994, Park-PenaMora 2003, Preston 2001, Ramkrishna 2000, Reddy 2005, Richardson-Pugh 1981,
Rogers 1995, Rausand-Hoyland 2004, Stave 2003, Sterman 1989/2000, Sugawara 1961, Teorell 1937,
van Schaik-Reuter 2009, and the JORS 1995 appliance paper.

- *System Dynamics Review* (Wiley) — search "construction", "infrastructure", "energy", "appliance".
- System Dynamics Society conference proceedings (free online; <systemdynamics.org>) — hundreds of domain models each year.
- *Resources, Conservation and Recycling* and *Journal of Industrial Ecology* — dynamic MFA papers (all convertible).
- *Journal of Infrastructure Systems* (ASCE), *Journal of Construction Engineering and Management* (ASCE) — growing SD sections.
- Energy and Buildings / Applied Energy — building & appliance stock models, both SD and stock-turnover style.

### Search keyword tips
- `"system dynamics" + <domain>` in Google Scholar, filter by *System Dynamics Review* first.
- For convertible material: `"dynamic material flow analysis"`, `"in-use stocks"`, `"stock-turnover"`, `"vintage cohort model"`, `"compartmental model"`, `"stock-flow consistent"`.
- Distinguish from mechanical "system dynamics" (vibrations/control, e.g., Lobontiu's *System Dynamics for Engineering Students*) — that is a different meaning of the term and not stock-and-flow.
