#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# GitHub raw file URL
github_url = 'https://github.com/parag0710/earnings/raw/main/tamo.xlsx'

# Function to fetch Excel file from GitHub
@st.cache
def fetch_excel_from_github(url):
    response = requests.get(url)
    return pd.read_excel(BytesIO(response.content), sheet_name=None)

# Load the Excel file from GitHub
try:
    xls_data = fetch_excel_from_github(github_url)
    sheet_names = list(xls_data.keys())  # Get sheet names from the loaded Excel file
    selected_sheet = st.selectbox('Select a company:', sheet_names)
    df = xls_data[selected_sheet]  # Read the selected sheet into a DataFrame
except Exception as e:
    st.error(f"Error loading data: {e}")
    df = pd.DataFrame()  # Empty DataFrame in case of error

# Convert all column names to strings
if not df.empty:
    df.columns = df.columns.astype(str)

    # Get unique values from the first column
    first_column_values = df[df.columns[0]].unique()
    options = ['All'] + list(first_column_values)

    # Create a select box for filtering the first column
    selected_value = st.selectbox('Select a guidance parameter:', options)

    # Filter the DataFrame based on the selected value
    if selected_value == 'All':
        filtered_df = df
    else:
        filtered_df = df[df[df.columns[0]] == selected_value]

    # Display the filtered DataFrame
    st.dataframe(filtered_df)
else:
    st.warning("No data to display.")


# In[ ]:




