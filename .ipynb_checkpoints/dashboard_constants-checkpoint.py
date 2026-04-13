"""dawn to dusk — shared constants"""

BG          = "#000000"
TEXT        = "#f4ecd8"
TEXT_MUTED  = "#8a8578"
GRID        = "#1e2332"

PREDAWN  = "#3d2c5c"
DAWN     = "#e85d24"
MORNING  = "#f2a623"
MIDDAY   = "#fcde5a"
AFTNOON  = "#e8a23c"
DUSK     = "#8b5cf6"
NIGHT    = "#3b5998"
DEEPNITE = "#1e2a4a"

SPECIES_PALETTE = [DAWN, MIDDAY, DUSK, NIGHT, MORNING, "#5dcaa5"]

COUNTY_SHORT = {
    "Avalon Peninsula-St. John's":              "Avalon",
    "St. George's-Stephenville":                "St. George's",
    "Northern Peninsula-St. Anthony":           "Northern Pen.",
    "Bonavista/Trinity-Clarenville":            "Bonavista",
    "Labrador-Happy Valley-Goose Bay":          "Labrador",
    "Central Newfoundland-Grand Falls-Windsor": "Central NL",
    "Burin Peninsula-Marystown":                "Burin",
    "Humber District-Corner Brook":             "Humber",
    "Notre Dame Bay-Lewisporte":                "Notre Dame",
    "South Coast-Channel-Port aux Basques":     "South Coast",
    "Nunatsiavut-Nain":                         "Nunatsiavut",
}

DEFAULT_SPECIES = (
    "Lincoln's Sparrow",
    "Mourning Dove",
    "Iceland Gull",
    "Northern Yellow Warbler",
)

SPECIES_POOL_SIZE = 100