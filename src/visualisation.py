import plotly.express as px


def plot_aqi_distribution(data):
    return px.histogram(data, x="AQI", nbins=40, title="Distribution of AQI", labels={"AQI": "Air Quality Index"})


def plot_average_aqi_by_city(city_summary, top_n=15):
    chart_data = city_summary.head(top_n).sort_values("Mean_AQI")
    return px.bar(chart_data, x="Mean_AQI", y="City", orientation="h", title=f"Top {top_n} Cities by Average AQI")


def plot_aqi_trend(data):
    trend = data.groupby("Date", as_index=False)["AQI"].mean()
    return px.line(trend, x="Date", y="AQI", title="Average AQI Trend Over Time")


def plot_pollutant_vs_aqi(data, pollutant):
    return px.scatter(data, x=pollutant, y="AQI", color="City", opacity=0.55, title=f"{pollutant} Compared with AQI")


def plot_correlation_heatmap(correlation_matrix):
    return px.imshow(correlation_matrix, text_auto=".2f", aspect="auto", title="Correlation Heatmap")
