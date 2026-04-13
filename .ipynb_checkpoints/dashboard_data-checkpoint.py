"""dawn to dusk — data loading and pre-aggregation (runs once at import)"""

import pandas as pd
import circlify as circ

from dashboard_constants import SPECIES_POOL_SIZE, COUNTY_SHORT


def _load_raw():
    df = pd.read_csv("birds.csv")
    df["OBSERVATION DATE"] = pd.to_datetime(df["OBSERVATION DATE"])
    df["month"] = df["OBSERVATION DATE"].dt.month
    df["hour"]  = pd.to_datetime(
        df["TIME OBSERVATIONS STARTED"], format="%H:%M:%S", errors="coerce"
    ).dt.hour
    df = df.dropna(subset=["hour", "COUNTY"])
    df["hour"] = df["hour"].astype(int)
    return df


def _build_hour_agg(df, species_pool):
    totals = (
        df.groupby(["month", "hour", "COUNTY"])
        .size()
        .reset_index(name="count")
    )
    species_df = df[df["COMMON NAME"].isin(species_pool)]
    species_counts = (
        species_df.groupby(["month", "hour", "COUNTY", "COMMON NAME"])
        .size()
        .reset_index(name="count")
    )
    return totals, species_counts


def _build_county_bubbles(df):
    county_counts = df["COUNTY"].value_counts().sort_values()
    values = county_counts.values.tolist()
    bubbles = circ.circlify(
        values,
        show_enclosure=False,
        target_enclosure=circ.Circle(x=0, y=0, r=1),
    )
    return county_counts, bubbles


def load():
    df = _load_raw()
    species_pool = (
        df["COMMON NAME"].value_counts().head(SPECIES_POOL_SIZE).index.tolist()
    )
    totals, species_counts = _build_hour_agg(df, species_pool)
    county_counts, county_bubbles = _build_county_bubbles(df)
    counties = sorted(df["COUNTY"].unique())
    return {
        "raw":            df,
        "totals":         totals,
        "species_counts": species_counts,
        "species_pool":   species_pool,
        "counties":       counties,
        "county_counts":  county_counts,
        "county_bubbles": county_bubbles,
    }


def hourly_from_totals(totals, month_range, hour_range, county):
    m_lo, m_hi = month_range
    h_lo, h_hi = hour_range
    mask = (
        (totals["month"] >= m_lo) & (totals["month"] <= m_hi) &
        (totals["hour"]  >= h_lo) & (totals["hour"]  <= h_hi)
    )
    if county != "All":
        mask &= (totals["COUNTY"] == county)
    sub = totals[mask]
    return sub.groupby("hour")["count"].sum().reindex(range(24), fill_value=0)


def hourly_species_from_counts(species_counts, sp_name, month_range, hour_range, county):
    m_lo, m_hi = month_range
    h_lo, h_hi = hour_range
    mask = (
        (species_counts["COMMON NAME"] == sp_name) &
        (species_counts["month"] >= m_lo) & (species_counts["month"] <= m_hi) &
        (species_counts["hour"]  >= h_lo) & (species_counts["hour"]  <= h_hi)
    )
    if county != "All":
        mask &= (species_counts["COUNTY"] == county)
    sub = species_counts[mask]
    return sub.groupby("hour")["count"].sum().reindex(range(24), fill_value=0)