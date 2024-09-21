import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    #Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

    #Data Filter
    st.subheader("Data Filter")
    kolom = df.columns.to_list()
    selected_column = st.selectbox("Select Column to Filter by", kolom)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Select Value", unique_value)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X Axis Column", kolom)
    y_column = st.selectbox("Select Y Axis Column", kolom)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting for uploading file")
