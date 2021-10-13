import streamlit as st 
import pandas as pd
import numpy as np 
import home
import visualise

st.set_page_config(
    page_title = 'Data Report Generator',
    page_icon = 'chart_with_upwards_trend',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.sidebar.title('Navigation Bar')
user_choice = st.sidebar.radio('Go to',('Home','Data Visulisation'))
about = st.sidebar.expander('About me')
with about:
    st.write('Name:')
    st.info('Gurpreet')
    st.write('Contact:')
    st.info('gurpreetmeelu900@gmail.com')
    st.markdown('''### LinkedIn: [Gurpreet](https://www.linkedin.com/in/gurpreet-meelu-68421a201/)''')
if user_choice == 'Home':
    home.home()
if user_choice == 'Data Visulisation':
    visualise.visualize()







    
