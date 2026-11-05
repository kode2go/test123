import streamlit as st
import pandas as pd

st.title("Retail Analytics Dashboard")

file = st.file_uploader("Upload CSV", type="csv")

if file is None: st.stop()

df = pd.read_csv(file)

st.subheader("Dataset")
st.dataframe(df)

st.subheader("First 5 Rows")
st.dataframe(df.head())

st.subheader("Statistics")
st.dataframe(df.describe())








st.subheader("Explore Your Data")

columns = st.multiselect("Select Columns", df.columns, default=df.columns)

category = st.selectbox("Select Category", df["Category"].unique())

filtered = df[df["Category"] == category]

st.dataframe(filtered[columns])
