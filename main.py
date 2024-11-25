import streamlit as st
from model import doUserTesting
import pandas as pd
st.set_page_config(
    page_title="HOME",
    page_icon="🏠"
)
st.title("AIR QUALITY ")
data = pd.read_csv('https://raw.githubusercontent.com/heetmiyani/AQI/main/Heet/data.csv', header=0)
# data,predictions,accuracy= doUserTesting()

st.text("Raw data")
st.dataframe(data)
st.text("")


st.write("Try with Custom Values!")
st.text("")
col1,col2=st.columns(2)
# Create input widgets for each variable
with col1:
    v1 = st.slider('CO(GT)', min_value=0.0,max_value=10.0)
    v2 = st.slider('PT08.S1(CO)', min_value=1000.0,max_value=2000.0)
    #v3 = st.number_input('NMHC(GT)', value=0, step=1)
    v4 = st.slider('C6H6(GT)', min_value=0.0,max_value=50.0)
    v5 = st.slider('PT08.S2(NMHC)', min_value=500.0,max_value=1500.0)
    v6 = st.slider('NOx(GT)', min_value=0.0,max_value=500.0)
    
with col2: 
    v7 = st.slider('PT08.S3(NOx)', min_value=500.0,max_value=2000.0)   
    v8 = st.slider('NO2(GT)', min_value=0.0,max_value=200.0)
    v9 = st.slider('PT08.S4(NO2)', min_value=1000.0,max_value=3000.0)
    v10 = st.slider('PT08.S5(O3)', min_value=500.0,max_value=2000.0)
    
    v12 = st.slider('AH', min_value=0.0,max_value=2.0)
v11 = st.slider('T', min_value=0.0,max_value=40.0)
st.text("")
st.title("Here Are your selected values:")
# Display the selected values
st.write(f'CO(GT): {v1}')
st.write(f'PT08.S1(CO): {v2}')
#st.write(f'NMHC(GT): {v3}')
st.write(f'C6H6(GT): {v4}')
st.write(f'PT08.S2(NMHC): {v5}')
st.write(f'NOx(GT): {v6}')
st.write(f'PT08.S3(NOx): {v7}')
st.write(f'NO2(GT): {v8}')
st.write(f'PT08.S4(NO2): {v9}')
st.write(f'PT08.S5(O3): {v10}')
st.write(f'AH: {v12}')
st.write(f'T: {v11}')
# data = {"CO(GT)": [v1], "PT08.S1(CO)": [v2], "NMHC(GT)": [v3], "C6H6(GT)": [v4], "PT08.S2(NMHC)": [v5], "NOx(GT)": [v6], "PT08.S3(NOx)": [v7], "NO2(GT)": [v8], "PT08.S4(NO2)": [v9], "PT08.S5(O3)": [v10], "T": [v11]}

# # Create a DataFrame from the dictionary with a specified index
# usertest_df = pd.DataFrame(data, index=[0])

# # Display the resulting DataFrame
# print("\n Data: ",usertest_df)
new_row = [v1,v2,v4,v5,v6,v7,v8,v9,v10,v11,v12]

st.text("")
list=["Linear Regression","Polynomial Regression","Ridge Regression","Lasso Regression"]
result=st.selectbox("Type of Regression",list)
if st.button("Proceed to Predict"):
    data,predictions,accuracy = doUserTesting(new_row, result)

    st.text("Predictions are ")
    st.text(predictions) 
    st.text("")

    st.text("Accuracy(R2 score) is ")
    st.text(accuracy)
    st.text("")

