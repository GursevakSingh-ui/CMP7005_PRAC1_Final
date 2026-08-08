import pandas as pd

POLLUTANT_COLUMNS = ["PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3", "Benzene", "Toluene", "Xylene"]
TARGET_COLUMN = "AQI"
CATEGORY_COLUMN = "AQI_Bucket"


def add_date_features(data: pd.DataFrame) -> pd.DataFrame:
    """Add year, month, month name, and season features from the Date column."""
    df = data.copy()
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.month_name()
    season_map = {
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Summer", 4: "Summer", 5: "Summer",
        6: "Monsoon", 7: "Monsoon", 8: "Monsoon", 9: "Monsoon",
        10: "Post-Monsoon", 11: "Post-Monsoon",
    }
    df["Season"] = df["Month"].map(season_map)
    return df


def clean_air_quality_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean data for EDA while preserving traceable, simple transformations."""
    df = data.copy()
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    numeric_columns = POLLUTANT_COLUMNS + [TARGET_COLUMN]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df.loc[df[column] < 0, column] = pd.NA

    df = add_date_features(df)
    return df


def prepare_model_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return rows usable for AQI regression without leaking AQI_Bucket into the model."""
    df = clean_air_quality_data(data)
    modelling_columns = POLLUTANT_COLUMNS + ["City", "Year", "Month", TARGET_COLUMN]
    return df[modelling_columns].dropna(subset=[TARGET_COLUMN])


def aqi_category_from_value(aqi: float) -> str:
    """Map a numeric AQI value to the Indian AQI category labels used in the dataset."""
    if aqi <= 50:
        return "Good"
    if aqi <= 100:
        return "Satisfactory"
    if aqi <= 200:
        return "Moderate"
    if aqi <= 300:
        return "Poor"
    if aqi <= 400:
        return "Very Poor"
    return "Severe"
