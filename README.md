# UGT-hackathon

Data analysis of Barcelona city open data (2017) for the Uber Global Hackathon 2023 (virtual regionals).
We cleaned 16 city datasets (population, transport, accidents, air quality, life expectancy, migration,
unemployment), clustered neighbourhoods and looked at how transport coverage, demographics and accidents differ
between them.

- Pitch deck: [Virtual Global Hackathon - Regionals Deck FINAL.pdf](Virtual%20Global%20Hackathon%20-%20Regionals%20Deck%20FINAL.pdf)
- Design slides: [Project design slides/Uber_Talks_Slides.pdf](Project%20design%20slides/Uber_Talks_Slides.pdf)

## What's here

| Folder | What it does |
|---|---|
| `Og_dataset/`, `csvs/` | Raw Barcelona datasets |
| `null_analysis/` | Share of missing values per column, per dataset |
| `fixed_datasets/`, `transports_cleaning/`, `fixed_datasetdupes/` | Missing-value and duplicate cleaning (bus stops, stations, life expectancy, air quality) |
| `transport_analysis/` | Bus and train stops per district |
| `cluster_analysis/` | Neighbourhood clusters by age group and population |
| `immi/` | Immigration and emigration by year |
| `Accidents.ipynb` | Neighbourhoods with the most accidents |
| `Uber Hackathon Study Case/` | Case study: PCA, linear regression and an MLP on the global power plant database |

## Run

Python 3 with pandas, matplotlib, seaborn and scikit-learn. Run scripts from the repo root, e.g.

```bash
python null_analysis/raw_analysis.py
python cluster_analysis/barcharts.py
```
