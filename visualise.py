import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt

def barchart(df, x_axis, y_axis):
    ca = alt.Chart(df).mark_bar().encode(
        x=x_axis,
        y=y_axis,
        ).interactive().properties(
        width=650,
        height=400)
    st.subheader('The Bar chart for '+ x_axis + ' and '+ y_axis)
    st.altair_chart(ca)

def scatter_chart(df, x_axis, y_axis, grouped_by):
    ca = alt.Chart(df).mark_circle(size=60).encode(
    x=x_axis,
    y=y_axis,
    color=grouped_by,
    tooltip=[x_axis,y_axis,grouped_by]).interactive().properties(
        width=650,
        height=400)
    st.subheader('The scatter plot for '+ x_axis + ' and '+ y_axis)
    st.altair_chart(ca)

def histogram_chart(df, x_axis, no_bins):
    ca = alt.Chart(df).mark_bar().encode(
        x = alt.X(x_axis, bin = alt.BinParams(maxbins = no_bins)),
        y = 'count()').interactive().properties(
            height = 400,
            width = 650,
        )
    st.subheader('The Histogram plot for '+ x_axis + ' is:')
    st.altair_chart(ca)

def line_chart(df, x_axis, y_axis):
    ca = alt.Chart(df).mark_line().encode(
        x = x_axis,
        y = y_axis,
        ).interactive().properties(
            width = 650,
            height = 400)
    st.subheader('The line chart for '+ x_axis + ' and '+ y_axis)
    st.altair_chart(ca)

def area_chart(df, x_axis, y_axis):
    ca = alt.Chart(df).mark_area(color = 'green',
        opacity = 0.5,
        line = {'color':'darkgreen'}).encode(

    x = x_axis,
    y = y_axis).interactive().properties(
        width = 650,
        height = 400)
    st.subheader('The Area chart for '+ x_axis + ' and '+ y_axis)
    st.altair_chart(ca)


def visualize():
    st.header("Upload the Dataset")

    uploaded_file = st.file_uploader("Upload a CSV file", type = ['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        columns= df.columns
        numerical_cols = df.select_dtypes(include = np.number).columns.tolist()
        categorical_cols = df.select_dtypes(include = ['object']).columns.tolist()
        chart_type = st.selectbox('Select the type of chart:',('Line','Bar','Scatter','Histogram','Area Chart'))

        if chart_type == 'Bar':
            x_axis = st.selectbox('Select the X Axis:', tuple(categorical_cols))
            y_axis = st.selectbox('Select the Y Axis:', tuple(numerical_cols))
            group_by = st.selectbox('Group by:', tuple(categorical_cols))
            barchart(df,x_axis,y_axis)
    
        if chart_type == 'Scatter':
            x_axis = st.selectbox('Select the X Axis:', tuple(numerical_cols))
            y_axis = st.selectbox('Select the Y Axis:', tuple(numerical_cols))
            group_by = st.selectbox('Group by:', tuple(categorical_cols))
            scatter_chart(df,x_axis,y_axis,group_by)
    
        if chart_type == 'Histogram':
            x_axis = st.selectbox('Select the X Axis:', tuple(columns))
            no_bins = st.slider('Number of bins:',min_value=5, max_value = 50, step = 5)
            histogram_chart(df,x_axis,no_bins)
    
        if chart_type == 'Line':
            x_axis = st.selectbox('Select the X Axis:', tuple(columns))
            y_axis = st.selectbox('Select the Y Axis:', tuple(numerical_cols))
            line_chart(df,x_axis, y_axis)
    
        if chart_type == 'Area Chart':
            x_axis = st.selectbox('Select the X Axis:', tuple(columns))
            y_axis = st.selectbox('Select the Y Axis:', tuple(numerical_cols))
            area_chart(df,x_axis, y_axis)
        



        


