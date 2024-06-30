#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd

# Load the Excel file and get sheet names
file_path = 'C:/Users/wpall/Desktop/tamo.xlsx'
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

# Create a select box for selecting the sheet
selected_sheet = st.selectbox('Select a company:', sheet_names)

# Read the selected sheet into a DataFrame
df = pd.read_excel(xls, sheet_name=selected_sheet)

# Convert all column names to strings
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


# In[ ]:




