# CMP7005_PRAC1_Final

## Project Purpose

This repository contains a complete reassessment project for **CMP7005 Programming for Data Analysis**. The project demonstrates a Python workflow from raw data handling to exploratory data analysis, machine learning, and an interactive Streamlit application using Indian air quality data.

## Dataset

The supplied assessment data contains daily air quality records for 26 Indian cities between 2015 and 2020. The raw data is provided as separate city CSV files and is combined into one processed dataset for analysis.

Main variables include City, Date, PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene, AQI, and AQI_Bucket.

## Main Functionality

- Loads and validates all 26 city CSV files.
- Combines the raw files into one reproducible processed dataset.
- Performs missing-value, duplicate, descriptive, temporal, city-level, and pollutant relationship analysis.
- Builds and compares regression models for AQI prediction.
- Tests Random Forest hyperparameter optimisation using GridSearchCV.
- Saves the final AQI prediction model.
- Provides a multipage Streamlit application for data overview, EDA, and AQI prediction.
- Includes GitHub and application screenshot evidence.

## Project Structure

```text
CMP7005_PRAC1_Final/
??? app/
?   ??? app.py
?   ??? pages/
??? assets/
?   ??? screenshots/
??? data/
?   ??? raw/
?   ??? processed/
??? docs/
??? models/
??? notebooks/
??? scripts/
??? src/
??? .gitignore
??? README.md
??? requirements.txt
```

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run the Pipeline

```bash
python scripts/run_pipeline.py
```

The pipeline combines the raw data, compares models, runs Random Forest optimisation, saves model results, and stores the final trained model.

## Run the Notebook

```bash
python -m notebook
```

Open:

```text
notebooks/CMP7005_PRAC1.ipynb
```

Then run all cells from top to bottom.

## Run the Streamlit Application

```bash
python -m streamlit run app/app.py
```

The app contains three user-facing sections: Data Overview, Exploratory Data Analysis, and Modelling and Prediction.

## Model Overview

The project compares Linear Regression, Decision Tree, Random Forest, Gradient Boosting, and a tuned Random Forest. The untuned Random Forest remains the final model because it produced the strongest RMSE on the held-out test set in the executed pipeline.

## Repository

Final GitHub repository:

```text
https://github.com/GursevakSingh-ui/CMP7005_PRAC1_Final
```
