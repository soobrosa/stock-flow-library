#!/usr/bin/env bash
# Download the open-access PDFs of the stock-and-flow bibliography.
# Paywalled sources are not included; see README.md for the missing list.
set -euo pipefail
cd "$(dirname "$0")"

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

fetch () { # $1 = output name, $2 = url
  [ -s "$1" ] && { echo "have  $1"; return; }
  echo "fetch $1"
  curl -sL -A "$UA" --max-time 120 -o "$1" "$2"
  # reject HTML error pages
  if [ "$(head -c 5 "$1")" != "%PDF-" ]; then echo "WARN  $1 is not a PDF, removing"; rm -f "$1"; fi
}

# Epidemiology
fetch Kermack-McKendrick_1927.pdf            "https://web.archive.org/web/2017id_/http://alun.math.ncsu.edu/wp-content/uploads/sites/2/2017/01/kermack_27.pdf"
# Ecology
fetch Lotka_1925_Elements-Physical-Biology.pdf "https://archive.org/download/elementsofphysic017171mbp/elementsofphysic017171mbp.pdf"
fetch Gordon_1954_fishery.pdf                "https://www.econ.ucsb.edu/~tedb/Courses/Ec100C/Readings/ScottGordonFisheries.pdf"
# Macroeconomics
fetch Tobin_1969.pdf                         "https://mail.tku.edu.tw/niehcc/paper/T(1969-jmcb).pdf"
fetch Nikiforos-Zezza_2017_SFC-survey.pdf    "https://www.levyinstitute.org/pubs/wp_891.pdf"
# Demography
fetch Leslie_1945.pdf                        "https://www.math.utah.edu/~keener/classes/math5110/papers/leslie.pdf"
# Operations
fetch Clark-Scarf_1960.pdf                   "http://dido.econ.yale.edu/~hes/pub/echelon1.pdf"
# Climate
fetch Sterman_2013_C-ROADS.pdf               "https://img.climateinteractive.org/2014/01/C-ROADS-ENSO-2013.pdf"
fetch Fiddaman_1997_thesis.pdf               "https://dspace.mit.edu/server/api/core/bitstreams/7a5e6fb2-1a86-4871-85d1-105829ed8579/content"
# Energy systems
fetch Greenspan-Cohen_1999_motorized-stocks.pdf "https://www.federalreserve.gov/pubs/feds/1996/199640/199640pap.pdf"
fetch Messner-Strubegger_1995_MESSAGE-III.pdf "https://pure.iiasa.ac.at/id/eprint/4527/1/WP-95-069.pdf"
# Industrial ecology
fetch Muller_2006_iron-cycles_PNAS.pdf       "https://web.archive.org/web/2023id_/https://www.pnas.org/doi/pdf/10.1073/pnas.0603375103"
# Appliances / e-waste
fetch McNeil_2010_appliance-diffusion.pdf    "https://www.osti.gov/servlets/purl/985912"
fetch WEEE_2018_kobe-WP.pdf                  "https://www.rieb.kobe-u.ac.jp/academic/ra/dp/English/DP2017-30.pdf"
fetch Zhang_2021_building-stock-Jinan.pdf    "https://europepmc.org/articles/PMC8472286?pdf=render"
# Project management
fetch Lyneis-Ford_2007_PM-survey.pdf         "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/sdr.377" # needs browser (Turnstile)
fetch Rahmandad-Sterman_2008.pdf             "https://www.mit.edu/~jsterman/Rahmandad-Sterman_0512221.pdf"

echo "done. valid PDFs:"
for f in *.pdf; do [ "$(head -c 5 "$f")" = "%PDF-" ] && echo "  ok  $f"; done
