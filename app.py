import streamlit as st
import pandas as pd

st.title("Retail Analytics Dashboard")

file = st.file_uploader("Upload CSV", type="csv")

df = pd.read_csv(file)

st.subheader("Dataset")
st.dataframe(df)

st.subheader("First 5 Rows")
st.dataframe(df.head())

st.subheader("Statistics")
st.dataframe(df.describe())
