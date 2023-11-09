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
from class_exploratory import exploratory

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
	st.markdown("- Created By. Aryajaya Alamsyah, Nov 2023")
	avs.add_vertical_space(2);

# container-header
with st.container():
	st.dataframe(data=np.round(dataset().get_dataset(),2), use_container_width=True, hide_index=True)
	st.text("-link download on https://www.kaggle.com/datasets/gregorut/videogamesales")
	avs.add_vertical_space(2);
	
# container-resume-sales
with st.container():
    st.success("Sum of video games sales from all regions")
	
    # metric sum sales from all regions
    sum_na, sum_eu, sum_jp, sum_ot = exploratory().get_sum_of_sales_regions()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="North America (NA)",value=str(sum_na) + " M")
    col2.metric(label="Europe (EU)",value=str(sum_eu) + " M")
    col3.metric(label="Japan (JP)",value=str(sum_jp) + " M") 
    col4.metric(label="Other regions",value=str(sum_ot) + " M")
    