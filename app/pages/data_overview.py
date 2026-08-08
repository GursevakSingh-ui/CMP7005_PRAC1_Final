import streamlit as st

from src.eda_functions import missing_value_summary
from src.preprocessing import POLLUTANT_COLUMNS


def _format_date(value):
    """Return a readable date string for Streamlit metric display."""
    if value is None or getattr(value, "isna", lambda: False)():
        return "Not available"
    return value.strftime("%d %B %Y")


def show_page(data):
    st.title("Data Overview")
    st.write("This page summarises the supplied Indian air quality dataset after loading and basic type preparation.")

    if data.empty:
        st.error("The dataset is empty. Please run the data pipeline before using the application.")
        return

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", f"{len(data):,}")
    col2.metric("Cities", f"{data['City'].nunique():,}")
    col3.metric("Start Date", _format_date(data["Date"].min()))
    col4.metric("End Date", _format_date(data["Date"].max()))

    st.subheader("Available Pollutants")
    st.write(", ".join([col for col in POLLUTANT_COLUMNS if col in data.columns]))

    st.subheader("Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)

    st.subheader("Missing Values Summary")
    st.dataframe(missing_value_summary(data), use_container_width=True)

    st.subheader("AQI Summary Statistics")
    st.dataframe(data["AQI"].describe().to_frame("AQI"), use_container_width=True)

    st.subheader("AQI Category Distribution")
    counts = data["AQI_Bucket"].fillna("Missing").value_counts().reset_index()
    counts.columns = ["AQI_Bucket", "Records"]
    st.bar_chart(counts.set_index("AQI_Bucket"))
