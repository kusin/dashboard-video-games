# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# call method from other file
from class_dataset import dataset

# define class exploratory
class visualization:

    def line_plot():
        x = 1
        return x
    
    def bar_plot(df, indexs, columns):
        # barplot with plotly
        fig = px.bar(df, x=indexs, y=columns, color_discrete_sequence=["#1E90FF"], title="Sum Video Games Sales by Region")

        # return values
        return fig
