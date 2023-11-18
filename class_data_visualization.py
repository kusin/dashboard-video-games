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
                x=df[indexs],y=df[columns], name=columns, width=0.5, 
            )
        )

        # update traces barplot
        fig.update_traces(
            marker_color = px.colors.diverging.RdYlBu,
        )
        
        # update layout barplot
        fig.update_layout(
            title = title,
            xaxis_title = x_title,
            yaxis_title = y_title,
            xaxis=dict(tickangle=0),
            yaxis=dict(tickangle=0),
        )

        # return values
        return fig
    
    def groupbar_plot(df, indexs, columns, title, x_title, y_title):
        # create a plot
        fig = px.bar(df, x=indexs, y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], barmode='group')

        colors = {
            'NA_Sales': 'rgb(165,0,38)', 
            'EU_Sales': 'rgb(215,48,39)', 
            'JP_Sales': 'rgb(244,109,67)', 
            'Other_Sales': 'rgb(253,174,97)'
        }
        for i, col in enumerate(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']):
            fig.update_traces(marker_color=colors[col], selector=dict(name=col), name=f'{col.split("_")[0]} Sales')
        
        # update layout barplot
        fig.update_layout(
            title = title,
            xaxis_title = x_title,
            yaxis_title = y_title,
            xaxis=dict(tickangle=0),
            yaxis=dict(tickangle=0),
            legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5),
        )

        # return valuess
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