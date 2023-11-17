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

    def pie_plot(df, indexs, columns):
        # create a plot
        fig = go.Figure()
        
        # add pieplot with graph object
        fig.add_trace(
            go.Pie(
                labels=df[indexs], values=df[columns], hole=0.25,
            )
        )

        # update traces pieplot
        fig.update_traces(
            marker=dict(colors=px.colors.diverging.RdBu, line=dict(color='#FFFFFF', width=2))
        )

        # update layout pieplot
        fig.update_layout(
            title = "Sales Video Games by Region",
            legend=dict(orientation='h', x=0.05, y=0.0),
        )

        return fig
    
    def bar_plot(df, indexs, columns, title, x_title, y_title):
        # create a plot
        fig = go.Figure()
        
        # add barplot with graph object
        fig.add_trace(
            go.Bar(
                x=df[indexs],y=df[columns], name=columns, width=0.5
            )
        )

        # update traces barplot
        fig.update_traces(
            marker_color = px.colors.diverging.RdYlBu
        )
        
        # update layout barplot
        fig.update_layout(
            title = title,
            xaxis_title = x_title,
            yaxis_title = y_title,
        )

        # return values
        return fig
    
    def line_plot(df, indexs, columns):
        # create a plot
        fig = go.Figure()
        
        # add lineplot with graph object
        fig.add_trace(
            go.Scatter(
                x=df[indexs],y=df[columns], mode='lines',
            )
        )

        # update traces lineplot
        fig.update_traces(
            line_color="#67001f",
            line_width=2.5
        )
        
        # update layout lineplot
        fig.update_layout(
            title = "Historical of sales video games by all region",
            xaxis_title = "Year Sales",
            yaxis_title = "Sum of Sales",
        )

        # return values
        return fig