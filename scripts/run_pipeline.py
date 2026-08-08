import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import save_combined_dataset, load_combined_dataset, inspect_dataset
from src.model import train_and_compare_models, save_model
from src.utils import RAW_DATA_DIR, COMBINED_DATA_PATH, MODEL_PATH, RESULTS_PATH


def main():
    data = save_combined_dataset(RAW_DATA_DIR, COMBINED_DATA_PATH)
    inspection = inspect_dataset(data)
    print("Combined dataset shape:", inspection["shape"])
    print("Date range:", inspection["date_min"], "to", inspection["date_max"])
    print("Cities:", len(inspection["cities"]))

    model, results, _ = train_and_compare_models(load_combined_dataset(COMBINED_DATA_PATH))
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(RESULTS_PATH, index=False)
    save_model(model, MODEL_PATH)
    print("Model comparison:")
    print(results.to_string(index=False))
    print(f"Saved model to {MODEL_PATH}")


if __name__ == "__main__":
    main()
