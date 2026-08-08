# CMP7005 Final Compliance Audit

| Assessment requirement | Status | Evidence | File or section |
|---|---|---|---|
| Task 1: 26 raw city files loaded | Complete | Raw files retained and loaded by reusable function | `data/raw/`, `src/data_loader.py` |
| Task 1: data combined | Complete | Combined dataset generated from raw files | `data/processed/air_quality.csv`, `scripts/run_pipeline.py` |
| Task 1: dimensions, columns, types checked | Complete | Notebook inspection section reports shape, columns, types, and date range | `notebooks/CMP7005_PRAC1.ipynb` |
| Task 1: duplicates checked | Complete | Exact duplicates and City-Date duplicates assessed | Notebook Task 1, `src/eda_functions.py` |
| Task 1: missing values checked | Complete | Count and percentage table included | Notebook Task 2, `src/eda_functions.py` |
| Task 2: fundamental understanding | Complete | Dataset scope, variables, cities, categories, and coverage discussed | Notebook Task 2 |
| Task 2: preprocessing explained | Complete | Date conversion, numeric conversion, duplicate handling, and temporal features explained | Notebook Task 2, `src/preprocessing.py` |
| Task 2: missing-data analysis | Complete | Missingness table, visualisation, and modelling implications discussed | Notebook Task 2 |
| Task 2: univariate analysis | Complete | AQI, selected pollutants, and category distributions analysed | Notebook Task 2 |
| Task 2: bivariate analysis | Complete | Pollutant-AQI, city, year, month, and season relationships analysed | Notebook Task 2 |
| Task 2: multivariate analysis | Complete | Correlation matrix and ranked AQI correlations interpreted | Notebook Task 2 |
| Task 2: unequal city coverage addressed | Complete | City date coverage and comparable-city limitation discussed | Notebook Task 2 |
| Task 3: prediction target defined | Complete | AQI regression objective stated | Notebook Task 3, `src/model.py` |
| Task 3: leakage avoided | Complete | AQI_Bucket excluded from model predictors | Notebook Task 3, `src/model.py` |
| Task 3: feature preparation | Complete | Numeric scaling, imputation, and city encoding in pipeline | `src/model.py` |
| Task 3: model comparison | Complete | Four baseline models plus tuned Random Forest compared | `models/model_comparison.csv`, Notebook Task 3 |
| Task 3: optimisation | Complete | GridSearchCV integrated and reported | `scripts/run_pipeline.py`, `models/model_optimisation.json` |
| Task 3: model interpretation | Complete | Feature importance and train-test comparison included | Notebook Task 3 |
| Task 4: Data Overview works | Complete | Date metric bug fixed and page tested | `app/pages/data_overview.py`, screenshots |
| Task 4: EDA page works | Complete | Filters and charts render with empty-data handling | `app/pages/eda.py`, screenshots |
| Task 4: Prediction page works | Complete | Model loads and prediction controls work | `app/pages/prediction.py`, screenshots |
| Task 4: navigation works | Complete | Single custom Streamlit navigation configured | `app/app.py`, `.streamlit/config.toml` |
| Task 5: GitHub repository | Complete | Final repository pushed | GitHub repository |
| Task 5: commit history evidence | Complete | Screenshot evidence included | `assets/screenshots/github_commit_history.png` |
| Task 5: repository screenshot | Complete | Screenshot evidence included | `assets/screenshots/github_repository_structure.png` |
| Task 5: README | Complete | Operational README included | `README.md` |
| Task 6: reflection completed | Complete | Evidence-based reflection included | Notebook Task 6, `docs/STUDENT_REFLECTION.md` |
| References | Complete | Genuine references included in notebook | Notebook References section |
| AI-use acknowledgement | Complete | AI-use statement included | Notebook AI Use Declaration |
