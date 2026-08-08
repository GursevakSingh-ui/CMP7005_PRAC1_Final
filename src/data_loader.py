from pathlib import Path
import pandas as pd

EXPECTED_COLUMNS = [
    "City", "Date", "PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2",
    "O3", "Benzene", "Toluene", "Xylene", "AQI", "AQI_Bucket"
]


def load_city_files(raw_dir: str | Path) -> pd.DataFrame:
    """Load and combine all city CSV files from the raw data directory."""
    raw_path = Path(raw_dir)
    csv_files = sorted(raw_path.glob("*_data.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No city CSV files found in {raw_path}")

    frames = []
    for file_path in csv_files:
        frame = pd.read_csv(file_path)
        missing = set(EXPECTED_COLUMNS) - set(frame.columns)
        if missing:
            raise ValueError(f"{file_path.name} is missing columns: {sorted(missing)}")
        frames.append(frame[EXPECTED_COLUMNS].copy())

    data = pd.concat(frames, ignore_index=True)
    data["Date"] = pd.to_datetime(data["Date"], dayfirst=True, errors="coerce")
    return data


def save_combined_dataset(raw_dir: str | Path, output_path: str | Path) -> pd.DataFrame:
    """Combine raw city files and save a single reproducible CSV file."""
    data = load_city_files(raw_dir)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output, index=False)
    return data


def load_combined_dataset(path: str | Path) -> pd.DataFrame:
    """Load the combined air quality dataset with parsed dates."""
    data = pd.read_csv(path)
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    return data


def inspect_dataset(data: pd.DataFrame) -> dict:
    """Return common inspection outputs used in Task 1."""
    return {
        "shape": data.shape,
        "columns": list(data.columns),
        "dtypes": data.dtypes.astype(str).to_dict(),
        "unique_values": data.nunique(dropna=False).to_dict(),
        "missing_values": data.isna().sum().to_dict(),
        "duplicates": int(data.duplicated().sum()),
        "date_min": data["Date"].min(),
        "date_max": data["Date"].max(),
        "cities": sorted(data["City"].dropna().unique().tolist()),
    }
