import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import load_combined_dataset, save_combined_dataset
from src.preprocessing import clean_air_quality_data
from src.utils import COMBINED_DATA_PATH, RAW_DATA_DIR

st.set_page_config(page_title="CMP7005 Air Quality Analysis", layout="wide")


@st.cache_data
def get_data():
    if not COMBINED_DATA_PATH.exists():
        data = save_combined_dataset(RAW_DATA_DIR, COMBINED_DATA_PATH)
    else:
        data = load_combined_dataset(COMBINED_DATA_PATH)
    return clean_air_quality_data(data)


st.sidebar.title("CMP7005")
page = st.sidebar.radio("Navigation", ["Data Overview", "Exploratory Data Analysis", "Modelling and Prediction"])
data = get_data()

if page == "Data Overview":
    from pages.data_overview import show_page
elif page == "Exploratory Data Analysis":
    from pages.eda import show_page
else:
    from pages.prediction import show_page

show_page(data)
