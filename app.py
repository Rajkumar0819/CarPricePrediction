import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open('model.pkl','rb') as f:
	model_loaded = pickle.load(f)


# Load the sample dataset
data = pd.read_csv('CleanData.csv')

# Create a list of unique company names
company_names = data['company'].unique()

# Create a dictionary to store vehicle models for each company
vehicle_dict = {company: data[data['company'] == company]['name'].unique() for company in company_names}

# Streamlit app layout
st.title('Car Price Prediction')


selected_company = st.selectbox('Select Company', company_names)

selected_vehicle = st.selectbox('Select Vehicle', vehicle_dict[selected_company])

selected_year = data[(data['company'] == selected_company) & (data['name'] == selected_vehicle)]['year'].values[0]
st.selectbox('Year of Model', [selected_year])


selected_fuel_type = data[(data['company'] == selected_company) & (data['name'] == selected_vehicle)]['fuel_type'].values[0]
st.selectbox('Fuel Type', [selected_fuel_type])

kms_driven = st.number_input('Kilometers Driven', min_value=0)

predict_button = st.button('Predict')

# Add logic to perform prediction when the button is clicked
if predict_button:
    if selected_company!='' and kms_driven!=0 and selected_vehicle !='' and selected_fuel_type!= "":
        predicted_price = model_loaded.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([selected_vehicle, selected_company, selected_year, kms_driven ,selected_fuel_type]).reshape(1,5)))
        predicted_price = round(predicted_price[0])
        st.write(f'Predicted Price: {predicted_price}')
    else:
         st.write("Enter the data correctly")

