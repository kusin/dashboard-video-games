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
    
    def bar_plot(df, indexs, columns):
        # create a plot
        fig = go.Figure()
        
        # add barplot with graph object
        fig.add_trace(
            go.Bar(
                x=df[indexs],y=df[columns], name=columns, width=0.75
            )
        )

        # update traces barplot
        fig.update_traces(
            marker_color = px.colors.diverging.RdYlBu
        )
        
        # update layout barplot
        fig.update_layout(
            title = "Sales Video Games by Region",
            xaxis_title = "Region Sales",
            yaxis_title = "Sum of Sales",
        )

        # return values
        return fig
    
    def line_plot(df, indexs, columns):
        # fig = px.line(
        #     df, x=indexs, y=columns, title='Time Series Plot of Total Global Sales by Region'
        # )
        # return fig

        # create a plot
        fig = go.Figure()
        
        # add lineplot with graph object
        fig.add_trace(
            go.Bar(
                x=df[indexs],y=df[columns], name=columns, width=0.75
            )
        )

        # update traces lineplot
        fig.update_traces(
            marker_color = px.colors.diverging.RdYlBu
        )
        
        # update layout lineplot
        fig.update_layout(
            title = "Sales Video Games by Region",
            xaxis_title = "Region Sales",
            yaxis_title = "Sum of Sales",
        )

        # return values
        return fig