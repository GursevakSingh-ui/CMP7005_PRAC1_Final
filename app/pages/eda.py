import streamlit as st

from src.eda_functions import city_aqi_summary, missing_value_summary, monthly_aqi_summary, pollutant_correlations, seasonal_aqi_summary
from src.preprocessing import POLLUTANT_COLUMNS
from src.visualisation import (
    plot_aqi_distribution,
    plot_aqi_trend,
    plot_average_aqi_by_city,
    plot_correlation_heatmap,
    plot_missing_values,
    plot_monthly_aqi,
    plot_pollutant_vs_aqi,
    plot_seasonal_aqi,
)


def show_page(data):
    st.title("Exploratory Data Analysis")
    st.write("Use the filters to explore city, pollutant, date, and AQI category patterns in the dataset.")

    if data.empty:
        st.error("The dataset is empty. Please run the data pipeline before using this page.")
        return

    cities = sorted(data["City"].dropna().unique())
    selected_cities = st.sidebar.multiselect("City", cities, default=cities[:5])
    pollutant_options = [col for col in POLLUTANT_COLUMNS if col in data.columns]
    pollutant = st.sidebar.selectbox("Pollutant", pollutant_options)
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
        st.warning("No records match the selected filters. Broaden the city, date, or AQI category selection.")
        return

    st.subheader("Missing Data in Current Selection")
    missing = missing_value_summary(filtered)
    st.plotly_chart(plot_missing_values(missing), use_container_width=True)

    st.subheader("AQI Distribution and Trends")
    st.plotly_chart(plot_aqi_distribution(filtered.dropna(subset=["AQI"])), use_container_width=True)
    st.plotly_chart(plot_aqi_trend(filtered.dropna(subset=["AQI"])), use_container_width=True)

    st.subheader("City, Month, and Season Comparisons")
    st.plotly_chart(plot_average_aqi_by_city(city_aqi_summary(filtered)), use_container_width=True)
    st.plotly_chart(plot_monthly_aqi(monthly_aqi_summary(filtered)), use_container_width=True)
    st.plotly_chart(plot_seasonal_aqi(seasonal_aqi_summary(filtered)), use_container_width=True)

    st.subheader("Pollutant Relationships")
    pollutant_data = filtered.dropna(subset=[pollutant, "AQI"])
    if pollutant_data.empty:
        st.info(f"No complete records are available for {pollutant} and AQI under the current filters.")
    else:
        st.plotly_chart(plot_pollutant_vs_aqi(pollutant_data, pollutant), use_container_width=True)

    corr = pollutant_correlations(filtered)
    if corr.empty:
        st.info("A correlation heatmap cannot be produced for the current filtered selection.")
    else:
        st.plotly_chart(plot_correlation_heatmap(corr), use_container_width=True)
