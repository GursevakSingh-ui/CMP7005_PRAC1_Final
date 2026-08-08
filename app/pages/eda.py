import streamlit as st

from src.eda_functions import city_aqi_summary, pollutant_correlations
from src.preprocessing import POLLUTANT_COLUMNS
from src.visualisation import (
    plot_aqi_distribution,
    plot_aqi_trend,
    plot_average_aqi_by_city,
    plot_correlation_heatmap,
    plot_pollutant_vs_aqi,
)


def show_page(data):
    st.title("Exploratory Data Analysis")
    st.write("Use the filters to explore city, pollutant, date, and AQI category patterns in the dataset.")

    cities = sorted(data["City"].dropna().unique())
    selected_cities = st.sidebar.multiselect("City", cities, default=cities[:5])
    pollutant = st.sidebar.selectbox("Pollutant", [col for col in POLLUTANT_COLUMNS if col in data.columns])
    categories = sorted(data["AQI_Bucket"].dropna().unique())
    selected_categories = st.sidebar.multiselect("AQI Category", categories, default=categories)
    min_date = data["Date"].min().date()
    max_date = data["Date"].max().date()
    date_range = st.sidebar.date_input("Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

    filtered = data.copy()
    if selected_cities:
        filtered = filtered[filtered["City"].isin(selected_cities)]
    if selected_categories:
        filtered = filtered[filtered["AQI_Bucket"].isin(selected_categories)]
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start, end = date_range
        filtered = filtered[(filtered["Date"].dt.date >= start) & (filtered["Date"].dt.date <= end)]

    st.metric("Filtered Records", f"{len(filtered):,}")
    if filtered.empty:
        st.warning("No records match the selected filters.")
        return

    st.plotly_chart(plot_aqi_distribution(filtered), use_container_width=True)
    st.plotly_chart(plot_aqi_trend(filtered), use_container_width=True)
    st.plotly_chart(plot_average_aqi_by_city(city_aqi_summary(filtered)), use_container_width=True)
    st.plotly_chart(plot_pollutant_vs_aqi(filtered.dropna(subset=[pollutant, "AQI"]), pollutant), use_container_width=True)
    st.plotly_chart(plot_correlation_heatmap(pollutant_correlations(filtered)), use_container_width=True)
