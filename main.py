# library ui-dashboard
import streamlit as st
from streamlit_extras import add_vertical_space as avs

# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# library data visualization
import plotly.express as px

# call method from other file
from class_dataset import dataset
from class_data_visualization import visualization
from class_data_exploratory import exploratory
from PIL import Image

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2023 all rights reserved by Aryajaya Alamsyah"
    })

# container-header
with st.container():
    st.markdown("## Visualization Data of Video Games Sales with Exploratory Data Analysis ")
    st.markdown("- Created By. Aryajaya Alamsyah, Nov 2023 (link download on https://www.kaggle.com/datasets/gregorut/videogamesales)")
    # st.dataframe(dataset().get_dataset(),use_container_width=True)

# container-resume-sales
with st.container():
    # labels resume-sales
    st.error("Sum of video games sales from all regions")
    
    # visualization sum of sales by year
    df = exploratory().get_sum_of_sales_by_year()
    st.plotly_chart(visualization.line_plot(df, "Year", "Global_Sales"), use_container_width=True)
    
    # visualization of sum video games sales
    col1, col2 = st.columns([1,1], gap="medium")
    with col1:
        # show pieplot
        df = exploratory().get_sum_of_sales_by_region()
        st.plotly_chart(visualization.pie_plot(df, "Region", "Sales"),use_container_width=True)
    with col2:
        # show barplot
        df = exploratory().get_sum_of_sales_by_region()
        st.plotly_chart(visualization.bar_plot(df, "Region", "Sales"), use_container_width=True)
    
# container-game-name
with st.container():
    # labels resume-sales
    st.error("Best game-name of video games sales")

    # visualization of Best game-name of video games sales
    col1, col2 = st.columns([1,1], gap="medium")
    with col1:
        st.text("Top five best game-name by Sales of all region")
    with col2:
        st.text("Top five best game-name by group region")

# container-platform
with st.container():
    # labels resume-sales
    st.error("Best platform of video games sales")

    # visualization of Best platform of video games sales
    col1, col2 = st.columns([1,1], gap="medium")
    with col1:
        st.text("Top five best platform by Sales of all region")
    with col2:
        st.text("Top five best platform by group region")

# container-gendre
with st.container():
    # labels resume-sales
    st.error("Best gendre of video games sales")

    

    # visualization of Best gendre of video games sales
    col1, col2 = st.columns([1,1], gap="medium")
    with col1:
        df = exploratory().get_best_genre()
        st.dataframe(df)
        st.plotly_chart(
            px.bar(
                df, x="Genre", y=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"], barmode='group'
            )    
        )
        
        st.text("Top five best gendre by Sales of all region")
    with col2:
        st.text("Top five best gendre by group region")

# container-publisher
with st.container():
    # labels resume-sales
    st.error("Best publisher of video games sales")

    # visualization of Best publisher of video games sales
    col1, col2 = st.columns([1,1], gap="medium")
    with col1:
        st.text("Top five best publisher by Sales of all region")
    with col2:
        st.text("Top five best publisher by group region")