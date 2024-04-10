import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# Here we use "magic commands":
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

import seaborn as sns
import numpy as np

df_weather_numeric = df_weather.select_dtypes(include=[np.number])
viz_correlation = sns.heatmap(df_weather_numeric.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
st.pyplot(viz_correlation.figure)

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")