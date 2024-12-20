import streamlit as st
import pandas as pd 

st.title('PENGIUM SPECIES PREDICTOR')
st.info('This APP builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/LakshayBondwal27/app.ML/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X_raw = df.drop('species' , axis = 1)
  X_raw

  st.write('**Y**')
  y_raw = df.species
  y_raw
 
with st.expander('Data Visualization'):
  st.scatter_chart(data = df  , x = 'bill_length_mm' , y = 'body_mass_g' , color = 'species')

# Input Features

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island' , ('Bisoe' , 'Dream' , 'Torgerson ') )

  bill_length_mm = st.slider('Bill length (mm)', 32.1 , 59.6 , 43.9)
  bill_depth_mm = st.slider('Bill length (mm)' , 13.1 , 21.5 , 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)' , 172.0 , 231.0 , 201.0)
  body_mass_g = st.slider('Body mass (g)' , 2700.0 , 6300.0 , 4207.0)
  gender = st.selectbox('Gender' , ('Male' , 'Female'))

  #Create a Data frame
  data = {'island':island,
          'bill_length_mm':bill_length_mm,
          'flipper_length_mm':flipper_length_mm,
          'body_mass_g':body_mass_g,
          'sex':gender
         }
  
  input_df = pd.DataFrame(data , index = [0])
  input_penguins = pd.concat([input_df , X_raw] , axis = 0)

with st.expander('Input Features'):
  st.write('**Input Pengiuns**')
  input_df
  st.write('**Combined Pengiun Data**')
  input_penguins
  

# Data prep

# encode X
encode = ['island' , 'sex']
df_penguins= pd.get_dummies(input_penguins, prefix = encode)
input_row = df_penguins[:1]

# encode y

target_mapper = {'Adelie':0,
                 'Chinstrap':1,
                 'Gentoo':2
}

def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)
y
y_raw

with st.expander('Data Prepration'):
  st.write('**Encoded X (input Pengiun)**')
  input_row
  st.write('**Encoded y**')
  y

#model training and frence



  












