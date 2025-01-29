import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Title and introduction
st.title("Hello Wilders, welcome to my application!")
st.write("Exploring Streamlit's possibilities with weather data analysis.")

# Load dataset
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# Display dataset
st.subheader("Dataset Overview")
st.dataframe(df_weather)

# Line chart for max temperature
df_weather['DATE'] = pd.to_datetime(df_weather['DATE'])  # Ensure DATE is in datetime format
st.subheader("Max Temperature Over Time")
st.line_chart(df_weather.set_index('DATE')['MAX_TEMPERATURE_C'])

# Correlation matrix (trimmed)
st.subheader("Correlation Heatmap (Upper Triangle)")
df_weather_numeric = df_weather.select_dtypes(include=[np.number])
corr_matrix = df_weather_numeric.corr()

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Plot heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, mask=mask, cmap="vlag", center=0, annot=True, fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Interactive name input
st.subheader("Your Name Analyzer")
name = st.text_input("Please enter your name:")
if name:
    name_length = len(name)
    st.write(f"Your name has {name_length} characters.")
