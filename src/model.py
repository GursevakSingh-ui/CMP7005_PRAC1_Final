from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor

from .preprocessing import POLLUTANT_COLUMNS, TARGET_COLUMN, prepare_model_data

RANDOM_STATE = 42


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
    features = POLLUTANT_COLUMNS + ["City", "Year", "Month"]
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
    features = POLLUTANT_COLUMNS + ["City", "Year", "Month"]
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
    return search.best_estimator_, search.best_params_, metrics


def save_model(model, path: str | Path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)


def load_model(path: str | Path):
    return joblib.load(path)
