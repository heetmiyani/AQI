import streamlit as st
import webbrowser


st.title("CONTACT")



col1,col2=st.columns(2)
with col1:
    st.image(r'/Users/heetmiyani/Downloads/Heet/Pages/Heet.jpeg',width=400)
    st.markdown("HEET MIYANI")
    linkedin = 'https://www.linkedin.com/in/heet-miyani-7053ba1ba/'
    github='https://github.com/heetmiyani'
    # instagram='https://www.instagram.com/khushiii_0108/'
    if st.button('LinkedIn'):
        webbrowser.open_new_tab(linkedin)
    if st.button('GitHub'):
        webbrowser.open_new_tab(github)
    # if st.button('Instagram'):
    #     webbrowser.open_new_tab(instagram)
        
