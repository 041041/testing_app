import streamlit as st
import pandas as pd

st.title("📊 Excel File Uploader")

# Upload Excel test file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read Excel into pandas dataframe
    df = pd.read_excel(uploaded_file, engine="openpyxl")

    # Show uploaded data
    st.write("✅ File Uploaded Successfully!")
    st.dataframe(df)

    # Show summary statistics
    st.write("🔹 Summary Statistics")
    st.write(df.describe())


