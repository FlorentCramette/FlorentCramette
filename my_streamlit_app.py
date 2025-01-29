import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

# Title and introduction
st.markdown("<h1 style='text-align: center;'>Hello Wilders, welcome to my application!</h1>", unsafe_allow_html=True)
st.write("Exploration des possibilités de Streamlit avec une analyse des données météorologiques.")

# Load dataset
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# Display dataset
st.subheader("Aperçu du jeu de données")
st.dataframe(df_weather)

# Line chart for max temperature
df_weather['DATE'] = pd.to_datetime(df_weather['DATE'])  # Ensure DATE is in datetime format
st.subheader("Température maximale au fil du temps")

def highlight_extremes(val):
    if val == df_weather['MAX_TEMPERATURE_C'].max():
        return 'background-color: red; color: white'
    elif val == df_weather['MAX_TEMPERATURE_C'].min():
        return 'background-color: blue; color: white'
    return ''

styled_df = df_weather[['DATE', 'MAX_TEMPERATURE_C']].style.applymap(highlight_extremes, subset=['MAX_TEMPERATURE_C'])
st.dataframe(styled_df)

# Create Altair chart for red line chart
chart = alt.Chart(df_weather).mark_line(color='red').encode(
    x='DATE:T',
    y='MAX_TEMPERATURE_C:Q'
)
st.altair_chart(chart, use_container_width=True)

# Correlation matrix (trimmed)
st.subheader("Carte de corrélation (triangle supérieur)")
df_weather_numeric = df_weather.select_dtypes(include=[np.number])
corr_matrix = df_weather_numeric.corr()

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Plot heatmap with increased size
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr_matrix, mask=mask, cmap="vlag", center=0, annot=True, fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Conclusion
st.write("La carte de corrélation montre une forte relation entre les variables liées à la température, tandis que le vent et les précipitations présentent des corrélations plus faibles avec la température.")

# Interactive name input
st.subheader("Analyseur de nom")
name = st.text_input("Veuillez entrer votre nom :")
if name:
    name_length = len(name)
    st.write(f"Votre nom contient {name_length} caractères.")
