import pandas as pd
from .preprocessing import POLLUTANT_COLUMNS


def city_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by city."""
    return (
        data.groupby("City", as_index=False)["AQI"]
        .agg(Mean_AQI="mean", Median_AQI="median", Records="count")
        .sort_values("Mean_AQI", ascending=False)
    )


def yearly_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by year."""
    return data.groupby("Year", as_index=False)["AQI"].mean().rename(columns={"AQI": "Mean_AQI"})


def monthly_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by month."""
    return data.groupby(["Month", "Month_Name"], as_index=False)["AQI"].mean().rename(columns={"AQI": "Mean_AQI"})


def pollutant_correlations(data: pd.DataFrame) -> pd.DataFrame:
    """Return correlations among pollutant variables and AQI."""
    columns = [col for col in POLLUTANT_COLUMNS + ["AQI"] if col in data.columns]
    return data[columns].corr(numeric_only=True)


def missing_value_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and percentages for each variable."""
    missing = data.isna().sum().rename("Missing_Count")
    percent = (data.isna().mean() * 100).rename("Missing_Percent")
    return pd.concat([missing, percent], axis=1).sort_values("Missing_Count", ascending=False)
