import streamlit as st
import pandas as pd 

st.title('ML APP')
st.info('This APP builds a machine learning model!')

with st.expander('Data'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/LakshayBondwal27/app.ML/refs/heads/master/penguins_cleaned.csv')
  df
