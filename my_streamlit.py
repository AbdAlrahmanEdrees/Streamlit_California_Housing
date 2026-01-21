import streamlit as st
import pandas as pd
# import plotly.express as px
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame

st.title("California Housing Dashboard")

# 111. Slider for MedInc
income_val = st.slider("Filter by Minimum Median Income",
                       float(df['MedInc'].min()), float(df['MedInc'].max()), 3.0)

df = df.rename(columns={
    'Latitude': 'latitude',
    'Longitude': 'longitude'
})

filtered_df = df[df['MedInc'] >= income_val]

st.map(filtered_df[['latitude', 'longitude']])

# 110. Map of California
st.subheader("Map of House Values")
# df = df.rename(columns={'Latitude': 'latitude', 'Longitude':'logitude'},inplace=True)
# st.map(filtered_df[['latitude', 'longitude']]) # Streamlit expects 'latitude/longitude' lowercase

st.write(f"Showing {len(filtered_df)} locations.")