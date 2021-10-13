import requests
import streamlit as st 
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_lottie import st_lottie
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pandas as pd

def home():
    @st.cache
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    st.header('Data Report Generator')
    lottie_url = "https://assets4.lottiefiles.com/packages/lf20_tljjahng.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)


    uploaded_file = st.file_uploader("Upload a CSV file", type = ['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination()
        gb.configure_side_bar()
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
        gridOptions = gb.build()
        AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True)
    
        if(st.button("Generate Report")):
            profile = ProfileReport(df)
            st_profile_report(profile)
    
    

