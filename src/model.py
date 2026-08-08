from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor

from .preprocessing import POLLUTANT_COLUMNS, TARGET_COLUMN, prepare_model_data

RANDOM_STATE = 42


def get_feature_columns():
    """Return the feature columns used for AQI prediction."""
    return POLLUTANT_COLUMNS + ["City", "Year", "Month"]


def build_preprocessor():
    numeric_features = POLLUTANT_COLUMNS + ["Year", "Month"]
    categorical_features = ["City"]
    return ColumnTransformer(
        transformers=[
            ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), numeric_features),
            ("categorical", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("encoder", OneHotEncoder(handle_unknown="ignore"))]), categorical_features),
        ]
    )


def evaluate_regression(model, X_test, y_test) -> dict:
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return {
        "R2": r2_score(y_test, predictions),
        "MAE": mean_absolute_error(y_test, predictions),
        "MSE": mse,
        "RMSE": float(np.sqrt(mse)),
    }


def train_and_compare_models(data: pd.DataFrame):
    df = prepare_model_data(data)
    features = get_feature_columns()
    X = df[features]
    y = df[TARGET_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)

    candidates = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=RANDOM_STATE, max_depth=10),
        "Random Forest": RandomForestRegressor(random_state=RANDOM_STATE, n_estimators=120, max_depth=16, n_jobs=-1),
        "Gradient Boosting": GradientBoostingRegressor(random_state=RANDOM_STATE),
    }

    results = []
    fitted_models = {}
    for name, estimator in candidates.items():
        pipeline = Pipeline([("preprocessor", build_preprocessor()), ("model", estimator)])
        pipeline.fit(X_train, y_train)
        metrics = evaluate_regression(pipeline, X_test, y_test)
        results.append({"Model": name, **metrics})
        fitted_models[name] = pipeline

    results_df = pd.DataFrame(results).sort_values("RMSE")
    best_name = results_df.iloc[0]["Model"]
    return fitted_models[best_name], results_df, (X_train, X_test, y_train, y_test)


def optimise_random_forest(data: pd.DataFrame):
    df = prepare_model_data(data)
    features = get_feature_columns()
    X = df[features]
    y = df[TARGET_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)
    pipeline = Pipeline([("preprocessor", build_preprocessor()), ("model", RandomForestRegressor(random_state=RANDOM_STATE, n_jobs=-1))])
    params = {
        "model__n_estimators": [100, 150],
        "model__max_depth": [12, 16, None],
        "model__min_samples_leaf": [1, 2],
    }
    search = GridSearchCV(pipeline, params, cv=3, scoring="neg_root_mean_squared_error", n_jobs=-1)
    search.fit(X_train, y_train)
    metrics = evaluate_regression(search.best_estimator_, X_test, y_test)
    cv_rmse = -search.best_score_
    return search.best_estimator_, search.best_params_, metrics, cv_rmse


def training_test_metrics(model, X_train, X_test, y_train, y_test) -> pd.DataFrame:
    """Compare training and testing performance for overfitting assessment."""
    rows = []
    for split_name, X, y in [("Train", X_train, y_train), ("Test", X_test, y_test)]:
        rows.append({"Split": split_name, **evaluate_regression(model, X, y)})
    return pd.DataFrame(rows)


def cross_validation_rmse(model, X, y, cv: int = 3) -> float:
    """Calculate cross-validated RMSE for a fitted-compatible pipeline."""
    scores = cross_val_score(model, X, y, cv=cv, scoring="neg_root_mean_squared_error", n_jobs=-1)
    return float(-scores.mean())


def feature_importance_table(model, top_n: int = 15) -> pd.DataFrame:
    """Return feature importances for tree-based pipeline models."""
    estimator = model.named_steps.get("model")
    preprocessor = model.named_steps.get("preprocessor")
    if not hasattr(estimator, "feature_importances_"):
        return pd.DataFrame(columns=["Feature", "Importance"])
    feature_names = preprocessor.get_feature_names_out()
    cleaned = [name.replace("numeric__", "").replace("categorical__", "") for name in feature_names]
    table = pd.DataFrame({"Feature": cleaned, "Importance": estimator.feature_importances_})
    return table.sort_values("Importance", ascending=False).head(top_n)


def save_model(model, path: str | Path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)


def load_model(path: str | Path):
    return joblib.load(path)
