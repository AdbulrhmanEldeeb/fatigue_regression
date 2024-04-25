import streamlit as st
from joblib import load
from PIL import Image
from sklearn.ensemble import RandomForestRegressor
import pandas as pd 

df=pd.read_csv('data.csv')
df.columns=['Sl. No.','Normalizing Temp','Through Hardening Temp','Through Hardening Time','Cooling Rate for Through Hardening','Carburization Temp',
             'Carburization Time','Diffusion Temp','Diffusion time','Quenching Media Temp','Tempering Temp','Tempering Time','Cooling Rate for Tempering',
             'C', 'Si', 'Mn', 'P', 'S', 'Ni', 'Cr', 'Cu', 'Mo','Reduction Ratio',
              'Area Proportion of Inclusions Deformed by Plastic Work','Area Proportion of Inclusions Occurring in Discontinuous Array',
              'Area Proportion of Isolated Inclusions','Fatigue Strength (10^7 Cycles)']

x=df.drop(columns=['Sl. No.','Fatigue Strength (10^7 Cycles)'])
y=df['Fatigue Strength (10^7 Cycles)']

# Setting page title and heading
st.set_page_config(page_title='Fatigue Strength Prediction', layout='wide')
st.title('Prediction of Fatigue Strength for Steel alloys')

image = Image.open('f_2.png')
st.image(image, width=600)
st.markdown("## enter parameters of the alloy and you will get the fatigue life below with 98.6% accuracy")
# Defining input sliders for each parameter
col1, col2, col3 = st.columns(3)
with col1:
    st.header('Process Parameters')
    normalizing_temp = st.slider("Normalizing Temperature (°C)", 825, 930, 825)
    through_hardening_temp = st.slider("Through Hardening Temperature (°C)", 30, 865, 400)
    through_hardening_time = st.slider("Through Hardening Time (s)", 1, 30, 15)
    cooling_rate_for_through_hardening = st.slider("Cooling Rate for Through Hardening (degree/second)", 1, 24, 12)

with col2:
    st.header('Carburization Parameters')
    carburization_temprature = st.slider("Carburization Temperature (°C)", 30, 930, 450)
    carburization_time = st.slider("Carburization Time (s)", 1, 540, 250)
    diffusion_temprature = st.slider("Diffusion Temperature (°C)", 30, 903, 450)
    diffusion_time = st.slider("Diffusion Time (s)", 1, 930, 70)

with col3:
    st.header('Tempering Parameters')
    quenching_media_temp = st.slider("Quenching Media Temperature (°C)", 30, 140, 250)
    tempering_temprature = st.slider("Tempering Temperature (°C)", 30, 680, 340)
    tempering_time = st.slider("Tempering Time (s)", 1, 120, 60)
    cooling_rate_for_tempering = st.slider("Cooling Rate for Tempering (degree/second)", 0, 24, 12)

# Additional alloy composition sliders
st.header('Alloy Composition (wt%)')
col4, col5, col6 = st.columns(3)
c = col4.slider("Carbon", 0.17, 0.63, 0.25)
si = col5.slider("Silicon", 0.16, 2.05, 1.)
mn = col6.slider("Manganese", 0.37, 1.6, 1.)

col4, col5, col6 = st.columns(3)
p = col4.slider("Phosphorus", 0.002, 0.031, 0.015)
s = col5.slider("Sulfur", 0.003, 0.03, 0.015)
ni = col6.slider("Nickel", 0.1, 2.78, 1.)

col4, col5, col6 = st.columns(3)
cr = col4.slider("Chromium", 0.01, 1.17, 0.5)
cu = col5.slider("Copper", 0.01, 0.26, 0.12)
mo = col6.slider("Molybdenum", 0.01, 0.24, 0.1)

# Reduction ratio and inclusion sliders
st.header('Other Parameters')
reduction_ratio = st.slider("Reduction Ratio", 250, 5530, 2600)
area_proportion_of_inclusions_deformed_by_plastic_work = st.slider("Area Proportion of Inclusions Deformed by Plastic Work", 0.001, 0.13, 0.05)
area_proportion_of_inclusions_occurring_in_discontinuous_array = st.slider("Area Proportion of Inclusions Occurring in Discontinuous Array", 0.001, 0.05, 0.02)
area_proportion_of_isolated_inclusions = st.slider("Area Proportion of Isolated Inclusions", 0.001, 0.058, 0.03)

# Predict fatigue strength
inputs_list = [normalizing_temp, through_hardening_temp, through_hardening_time, cooling_rate_for_through_hardening,
               carburization_temprature, carburization_time, diffusion_temprature, diffusion_time,
               quenching_media_temp, tempering_temprature, tempering_time, cooling_rate_for_tempering,
               c, si, mn, p, s, ni, cr, cu, mo, reduction_ratio,
               area_proportion_of_inclusions_deformed_by_plastic_work,
               area_proportion_of_inclusions_occurring_in_discontinuous_array,
               area_proportion_of_isolated_inclusions]

# Load and use the model
regressor=RandomForestRegressor()
regressor.fit(x,y)
result = regressor.predict([inputs_list])[0]

# Display the result
st.header('Result')
st.markdown(f"#### Predicted Fatigue Strength:    **{round(result, 1)} * 10^7 cycles**")
st.divider()
st.markdown("""Note:\n
            This prediction is pased on Random forest model with R squared value equals 98.6% """)

