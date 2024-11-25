import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import time

st.set_page_config(
    page_title="Home",
    page_icon="🏠"
    
)
st.image(r"/Users/heetmiyani/Downloads/Heet/Pages/ccc.png")
st.title("Predicting Air Quality for a Healthier Future")
col1,col2=st.columns(2)
with col1:
    st.markdown("""Air in its purest form is best suited to the critical task of sustaining life. A significant environmental risk to human health is air pollution. Air pollution has been the biggest source of heart attacks and heart strokes. In fact, the suffering from heart related diseases which can be exacerbated by increase in air pollution. 
The risk of lung cancer, heart disease, stroke, as well as acute and chronic respiratory illnesses like asthma, can all be reduced by breathing clean air. Long-term and short-term cardiovascular and respiratory health are both improved by lower air pollution levels. Air pollution caused by humans includes emissions from industrial plants, automobiles, planes, the combustion of plastics, coal, kerosene and so on. Every day, dangerous pollutants such as CO, CO2, Particulate Matter (PM), NO2, SO2, O3, NH3, Pb, and others are released into our environment. Humans, animals, and even plants are harmed by the chemicals and particles that make up air pollution. 
Other contemporary environmental issues caused by poor air quality include global warming, acid rain, reduced visibility, smog, climate change, and premature deaths. The Air Quality Index (AQI), an assessment parameter which is directly related to the health of the human. A higher level of AQI indicates a greater risk of human exposure.
""")

# with col2:
#     st.image(r"/Users/heetmiyani/Downloads/Heet/image.jpg")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with col2:
    lottie_url_hello = "https://assets10.lottiefiles.com/packages/lf20_f7wf1y3d.json"
    lottie_hello = load_lottieurl(lottie_url_hello)

    st_lottie(lottie_hello, key="hello")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.title("Introduction")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

col3,col4=st.columns(2)

with col3:
    st.markdown("""Air in its purest form is best suited to the critical task of sustaining life. A significant environmental risk to human health is air pollution. Air pollution has been the biggest source of heart attacks and heart strokes. In fact, the suffering from heart related diseases which can be exacerbated by increase in air pollution. 
The risk of lung cancer, heart disease, stroke, as well as acute and chronic respiratory illnesses like asthma, can all be reduced by breathing clean air. Long-term and short-term cardiovascular and respiratory health are both improved by lower air pollution levels. Air pollution caused by humans includes emissions from industrial plants, automobiles, planes, the combustion of plastics, coal, kerosene and so on. Every day, dangerous pollutants such as CO, CO2, Particulate Matter (PM), NO2, SO2, O3, NH3, Pb, and others are released into our environment. Humans, animals, and even plants are harmed by the chemicals and particles that make up air pollution. 
Other contemporary environmental issues caused by poor air quality include global warming, acid rain, reduced visibility, smog, climate change, and premature deaths. The Air Quality Index (AQI), an assessment parameter which is directly related to the health of the human. A higher level of AQI indicates a greater risk of human exposure.
""")

with col4:
    lottie_url1 = "https://assets2.lottiefiles.com/packages/lf20_YZrGzO2pAP.json"
    lottie_1 = load_lottieurl(lottie_url1)

    st_lottie(lottie_1, key="bye")
# if st.button("Download"):
#     with st_lottie_spinner(lottie_download, key="download"):
#         time.sleep(5)
#     st.balloons()

if st.button("Predict the AIR Quality"):
    switch_page("main")

if st.button("EDA"):
    switch_page("EDA")