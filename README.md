# CMP_7005_Prac1

## CMP7005 Programming for Data Analysis Reassessment

This project supports the reassessment for **CMP7005 Programming for Data Analysis**. It demonstrates a complete Python workflow from raw air quality data to data cleaning, exploratory data analysis, machine learning, and an interactive Streamlit application.

## Dataset

The supplied assessment data contains daily Indian city air quality records from 2015 to 2020. The raw data is provided as separate city CSV files and is combined into one processed dataset for analysis.

Main variables include:

- City and Date
- PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3
- Benzene, Toluene, Xylene
- AQI and AQI_Bucket

## Main Features

- Loads and combines all supplied city CSV files
- Performs dataset inspection and missing value analysis
- Cleans dates, numeric pollutant fields, duplicates, and invalid negative values
- Creates year, month, month name, and season features
- Provides univariate, bivariate, and multivariate EDA
- Compares regression models for AQI prediction
- Saves the best trained model for reuse
- Provides a multipage Streamlit GUI for data overview, EDA, and prediction

## Project Structure

```text
CMP_7005_Prac1/
??? app/
?   ??? app.py
?   ??? pages/
??? assets/
?   ??? screenshots/
??? data/
?   ??? raw/
?   ??? processed/
??? models/
??? notebooks/
??? scripts/
??? src/
??? requirements.txt
??? README.md
??? .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Analysis Pipeline

```bash
python scripts/run_pipeline.py
```

This creates the combined processed dataset, trains the model, saves the model comparison table, and stores the trained model.

## Run the Streamlit Application

```bash
streamlit run app/app.py
```

If the `streamlit` command is not recognised, use:

```bash
python -m streamlit run app/app.py
```

## Notebook

The main academic notebook is:

```text
notebooks/CMP7005_PRAC1.ipynb
```

It contains the assessment narrative, code cells, EDA sections, model-building section, application-development summary, version-control evidence placeholders, reflection placeholders, and final compliance audit.

## Model Summary

The current pipeline compares Linear Regression, Decision Tree, Random Forest, and Gradient Boosting regression models. Based on the generated evaluation table, Random Forest currently gives the strongest performance on the supplied dataset.

## Important Student Notes

Before submission, the student should:

- Run the notebook from top to bottom
- Add written interpretations below important outputs
- Add genuine screenshots of the Streamlit app and GitHub commit history
- Complete the reflection in their own words
- Check the university AI-use declaration wording
- Ensure all GitHub evidence is real and current

## AI Use Declaration

AI support was used to help structure, code, and review this project. The student must review, understand, test, and adapt the final work before submission.
