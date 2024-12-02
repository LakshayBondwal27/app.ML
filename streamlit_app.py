import streamlit as st
import pandas as pd 

st.title('ML APP')
st.info('This APP builds a machine learning model!')

df = pd.read_csv('https://github.com/LakshayBondwal27/app.ML/blob/master/penguins_cleaned.csv')
df
