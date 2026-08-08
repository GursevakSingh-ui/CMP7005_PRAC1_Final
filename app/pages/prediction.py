from pathlib import Path
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.model import load_model
from src.preprocessing import POLLUTANT_COLUMNS, aqi_category_from_value
from src.utils import MODEL_PATH, RESULTS_PATH


def show_page(data):
    st.title("Modelling and Prediction")
    st.write("This academic model predicts numerical AQI from pollutant measurements, city, year, and month. It should not be used as official environmental or health advice.")

    if not MODEL_PATH.exists():
        st.warning("The trained model file was not found. Run `python scripts/run_pipeline.py` before using prediction.")
        return

    model = load_model(MODEL_PATH)
    if RESULTS_PATH.exists():
        st.subheader("Model Comparison")
        st.dataframe(pd.read_csv(RESULTS_PATH), use_container_width=True)

    st.subheader("Enter Prediction Values")
    col1, col2, col3 = st.columns(3)
    city = col1.selectbox("City", sorted(data["City"].dropna().unique()))
    year = col2.number_input("Year", min_value=2015, max_value=2030, value=2020, step=1)
    month = col3.number_input("Month", min_value=1, max_value=12, value=1, step=1)

    values = {}
    cols = st.columns(3)
    for index, pollutant in enumerate(POLLUTANT_COLUMNS):
        default_value = float(data[pollutant].median()) if pollutant in data.columns else 0.0
        values[pollutant] = cols[index % 3].number_input(pollutant, min_value=0.0, value=default_value, step=1.0)

    input_data = pd.DataFrame([{**values, "City": city, "Year": int(year), "Month": int(month)}])

    if st.button("Predict AQI"):
        prediction = float(model.predict(input_data)[0])
        st.success(f"Predicted AQI: {prediction:.2f}")
        st.info(f"Estimated AQI category: {aqi_category_from_value(prediction)}")
        st.dataframe(input_data, use_container_width=True)
