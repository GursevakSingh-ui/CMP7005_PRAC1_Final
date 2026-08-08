import pandas as pd
from .preprocessing import POLLUTANT_COLUMNS


def city_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by city."""
    return (
        data.groupby("City", as_index=False)["AQI"]
        .agg(Mean_AQI="mean", Median_AQI="median", Records="count")
        .sort_values("Mean_AQI", ascending=False)
    )


def city_date_coverage(data: pd.DataFrame) -> pd.DataFrame:
    """Return first date, last date, and observation count for each city."""
    return (
        data.groupby("City", as_index=False)
        .agg(Start_Date=("Date", "min"), End_Date=("Date", "max"), Records=("Date", "count"), AQI_Records=("AQI", "count"))
        .sort_values(["Start_Date", "City"])
    )


def duplicate_city_dates(data: pd.DataFrame) -> pd.DataFrame:
    """Return duplicated City-Date combinations, if any exist."""
    duplicated = data[data.duplicated(["City", "Date"], keep=False)]
    return duplicated.sort_values(["City", "Date"])


def yearly_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by year."""
    return data.groupby("Year", as_index=False)["AQI"].mean().rename(columns={"AQI": "Mean_AQI"})


def monthly_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by month."""
    return data.groupby(["Month", "Month_Name"], as_index=False)["AQI"].mean().rename(columns={"AQI": "Mean_AQI"}).sort_values("Month")


def seasonal_aqi_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise AQI by season."""
    order = ["Winter", "Summer", "Monsoon", "Post-Monsoon"]
    summary = data.groupby("Season", as_index=False)["AQI"].mean().rename(columns={"AQI": "Mean_AQI"})
    summary["Season"] = pd.Categorical(summary["Season"], categories=order, ordered=True)
    return summary.sort_values("Season")


def pollutant_correlations(data: pd.DataFrame) -> pd.DataFrame:
    """Return correlations among pollutant variables and AQI."""
    columns = [col for col in POLLUTANT_COLUMNS + ["AQI"] if col in data.columns]
    return data[columns].corr(numeric_only=True)


def ranked_aqi_correlations(data: pd.DataFrame) -> pd.DataFrame:
    """Return pollutant correlations with AQI ranked by absolute strength."""
    corr = pollutant_correlations(data)["AQI"].drop("AQI").dropna()
    result = corr.rename("Correlation_with_AQI").reset_index().rename(columns={"index": "Variable"})
    result["Absolute_Correlation"] = result["Correlation_with_AQI"].abs()
    return result.sort_values("Absolute_Correlation", ascending=False)


def missing_value_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and percentages for each variable."""
    missing = data.isna().sum().rename("Missing_Count")
    percent = (data.isna().mean() * 100).round(2).rename("Missing_Percent")
    return pd.concat([missing, percent], axis=1).sort_values("Missing_Count", ascending=False).reset_index(names="Variable")


def comparable_city_subset(data: pd.DataFrame, min_year: int = 2015, max_year: int = 2020) -> pd.DataFrame:
    """Return records for cities with AQI observations spanning the selected years."""
    valid = data.dropna(subset=["AQI"])
    coverage = valid.groupby("City")["Year"].agg(Start_Year="min", End_Year="max")
    cities = coverage[(coverage["Start_Year"] <= min_year) & (coverage["End_Year"] >= max_year)].index
    return data[data["City"].isin(cities)].copy()
