# library ui-dashboard
import streamlit as st

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
	