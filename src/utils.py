from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
COMBINED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "air_quality.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "trained_model.pkl"
RESULTS_PATH = PROJECT_ROOT / "models" / "model_comparison.csv"
