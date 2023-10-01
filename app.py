import streamlit as st
import pandas as pd
import time
from streamlit_lottie import st_lottie
import json
import plotly.express as px


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# Title and caption
st.title('Graph Wizard')
st.caption('Upload an excel file and generate a graph!')

# Sidebar
with st.sidebar:
    # Header
    st.header('Graph Editor')
    # st.write('Currently only supporting .xlsx files')

    # File uploader
    xy_options = ['File not uploaded']
    plots_options = ['Scatter Plot', 'Line Chart', 'Histogram', 'Bar Chart']
    file = st.file_uploader(label='label', label_visibility='collapsed')
    if file is not None:
        filename = file.name
        if filename[-4:] == '.csv':
            df_xl = pd.read_csv(file)
        else:
            df_xl = pd.read_excel(file)
    # X axis
    x_axis = st.selectbox(
        'Please select the variable for the x-axis',
        (xy_options)
    )

    # Y axis
    y_axis = st.selectbox(
        'Please select the variable for the y-axis',
        (xy_options)
    )

    # Plot type
    plot = st.selectbox(
        'Please select the type of plot you want to generate:',
        (plots_options)
    )

if file is not None:
    df_xl
    if (plot == 'Line Chart'):
        fig = px.line(df_xl, x=x_axis, y=y_axis)
    elif (plot == 'Histogram'):
        fig = px.histogram(df_xl, x=x_axis)
    elif (plot == 'Bar Chart'):
        fig = px.bar(df_xl, x=x_axis, y=y_axis)
    else:
        fig = px.scatter(df_xl, x=x_axis, y=y_axis)
    fig
else:
    files_animation = load_lottiefile("lottie/files.json")
    st_lottie(files_animation)
