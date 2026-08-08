# CMP7005 Final Compliance Audit

| Assessment Requirement | Implemented | Evidence or File | Remaining Action |
|---|---|---|---|
| Data imported | Yes | `src/data_loader.py`, `scripts/run_pipeline.py` | None |
| Multiple CSV files combined | Yes | `src/data_loader.py` | Explain merge reason in notebook narrative |
| Dataset inspected | Yes | `notebooks/CMP7005_PRAC1.ipynb` | Run notebook and keep outputs |
| Dataset dimensions reported | Yes | Notebook Task 1 | None after execution |
| Column names and data types checked | Yes | Notebook Task 1 | None after execution |
| Missing values assessed | Yes | `src/eda_functions.py`, notebook Task 2 | Add interpretation text |
| Duplicate records assessed | Yes | `src/data_loader.py`, notebook Task 1 | None after execution |
| Date variable parsed | Yes | `src/data_loader.py`, `src/preprocessing.py` | None |
| Numeric pollutant handling | Yes | `src/preprocessing.py` | None |
| Original/raw data preserved | Yes | `data/raw/` | None |
| Clean processed data created | Yes | `data/processed/air_quality.csv` | None |
| Feature engineering applied | Yes | `src/preprocessing.py` | Justify date features in notebook |
| Fundamental data understanding | Yes | Notebook Task 2.1 | Add student interpretations |
| Univariate EDA completed | Yes | Notebook Task 2.3 | Add interpretation below charts |
| Bivariate EDA completed | Yes | Notebook Task 2.4 | Add interpretation below charts |
| Multivariate EDA completed | Yes | Notebook Task 2.5 | Add interpretation below heatmap |
| Analytical questions supported | Partial | Notebook EDA sections | Add answer-style summaries after running outputs |
| AQI prediction objective defined | Yes | Notebook Task 3, `src/model.py` | None |
| Target leakage considered | Yes | `src/model.py`, notebook text | None |
| Train/test split used | Yes | `src/model.py` | None |
| Encoding considered | Yes | `OneHotEncoder` in `src/model.py` | None |
| Scaling considered | Yes | `StandardScaler` in `src/model.py` | None |
| Missing values handled for model | Yes | `SimpleImputer` in `src/model.py` | None |
| Model comparison completed | Yes | `models/model_comparison.csv` | Discuss model choice in notebook |
| Model evaluated with regression metrics | Yes | `src/model.py`, `models/model_comparison.csv` | None |
| Final model saved | Yes | `models/trained_model.pkl` | None |
| GUI developed | Yes | `app/app.py` | Add screenshots |
| Data Overview page included | Yes | `app/pages/data_overview.py` | None |
| EDA page included | Yes | `app/pages/eda.py` | None |
| Prediction page included | Yes | `app/pages/prediction.py` | None |
| User input validation considered | Yes | Streamlit numeric bounds in prediction page | None |
| README prepared | Yes | `README.md` | Add GitHub URL if required |
| Requirements file prepared | Yes | `requirements.txt` | None |
| Git repository connected | To complete locally | Git remote command | Push after commits |
| GitHub commit evidence | To complete | GitHub screenshots | Student must capture screenshots |
| Reflection included | Draft placeholder | Notebook Task 6 | Student must personalise |
| AI-use acknowledgement included | Draft | Notebook and README | Adjust to required university wording |
