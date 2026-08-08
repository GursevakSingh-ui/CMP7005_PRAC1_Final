import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import json
import pandas as pd

from src.data_loader import inspect_dataset, load_combined_dataset, save_combined_dataset
from src.model import optimise_random_forest, save_model, train_and_compare_models
from src.utils import COMBINED_DATA_PATH, MODEL_PATH, RAW_DATA_DIR, RESULTS_PATH


def main():
    data = save_combined_dataset(RAW_DATA_DIR, COMBINED_DATA_PATH)
    inspection = inspect_dataset(data)
    print("Combined dataset shape:", inspection["shape"])
    print("Date range:", inspection["date_min"], "to", inspection["date_max"])
    print("Cities:", len(inspection["cities"]))

    model, results, _ = train_and_compare_models(load_combined_dataset(COMBINED_DATA_PATH))
    print("Baseline model comparison:")
    print(results.to_string(index=False))

    tuned_model, best_params, tuned_metrics, cv_rmse = optimise_random_forest(load_combined_dataset(COMBINED_DATA_PATH))
    print("Random Forest optimisation best parameters:", best_params)
    print("Random Forest optimisation CV RMSE:", round(cv_rmse, 4))
    print("Tuned Random Forest test metrics:", tuned_metrics)

    results_with_tuning = results.copy()
    tuned_row = {"Model": "Tuned Random Forest", **tuned_metrics}
    results_with_tuning = pd.concat([results_with_tuning, pd.DataFrame([tuned_row])], ignore_index=True).sort_values("RMSE")
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    results_with_tuning.to_csv(RESULTS_PATH, index=False)
    optimisation_path = RESULTS_PATH.parent / "model_optimisation.json"
    optimisation_path.write_text(json.dumps({"best_params": best_params, "cv_rmse": cv_rmse, "tuned_metrics": tuned_metrics}, indent=2), encoding="utf-8")

    final_model = tuned_model if tuned_metrics["RMSE"] <= results.iloc[0]["RMSE"] else model
    save_model(final_model, MODEL_PATH)
    print("Final model saved to:", MODEL_PATH)
    print("Final comparison table:")
    print(results_with_tuning.to_string(index=False))


if __name__ == "__main__":
    main()
