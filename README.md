# Dawn to Dusk

Data visualization project for the eBird 2025 Newfoundland and Labrador
dataset. ~300,000 observations, 300+ species, 11 counties. Built as the
COMP 4304 final project at MUN.

Two deliverables:

  - infographic.ipynb  — a 24x36" printable poster
  - dashboard.ipynb    — an interactive ipywidgets dashboard

Both answer the same question: when and where do Newfoundland's birds
come alive?

## Visualizations

Three charts, shared across both deliverables:

  1. The Birding Clock. Polar bar chart of observations by hour of day.
     Peak is 08:00 with 42,000+ observations. Night is near-silent.

  2. The Birding Day Compresses. Summer vs winter observations split
     into five time buckets. Summer: 160,254. Winter: 32,654. Winter
     evening: 69.

  3. A Day in the Life. Per-species hourly activity, normalized by
     total observations per hour to remove observer bias. Different
     species peak at different times.

## Running it

    git clone https://github.com/mnbmnd/dawn-to-dusk.git
    cd dawn-to-dusk
    pip install -r requirements.txt
    jupyter lab

Open either notebook and run all cells. The infographic renders a
single figure. The dashboard renders a widget panel with four
controls: season, county, hour range, and species.

## Dependencies

  - pandas
  - numpy
  - matplotlib
  - ipywidgets
  - jupyterlab

See requirements.txt.

## Data

eBird Basic Dataset, Cornell Lab of Ornithology, 2025. Filtered to
Newfoundland and Labrador. birds.csv in the repo root.

## Credits

Bird silhouettes from PhyloPic. The NL flag is public domain.

## License

MIT. See LICENSE.
