import re
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv', header=0)

st.title("EDA")

a=["CO(GT)","PT08.S1(CO)","C6H6(GT)","PT08.S2(NMHC)","NOx(GT)","PT08.S3(NOx)","NO2(GT)","PT08.S4(NO2)","PT08.S5(O3)","T","AH","RH"]
result1=st.selectbox("X-axis Feature",a)
b=["CO(GT)","PT08.S1(CO)","C6H6(GT)","PT08.S2(NMHC)","NOx(GT)","PT08.S3(NOx)","NO2(GT)","PT08.S4(NO2)","PT08.S5(O3)","T","AH","RH"]
result2=st.selectbox("Y-axis Feature",b)

c=["Scatter Plot","Bar Plot"]
result3=st.selectbox("Type of Plot",c)


if st.button("Plot the graph"):
    if result3=="Scatter Plot":
        fig,ax=plt.subplots()
        sns.scatterplot(x=result1, y=result2, data=data,ax=ax)
        st.pyplot(fig)
    if result3=="Bar Plot":
        fig,ax=plt.subplots()
        plt.hist(a,b)
        # plt.hist(b)
        st.pyplot(fig)
