import pandas as pd
import plotly.express as px
import streamlit as st

class SalesBarPlot:
    def __init__(self, df):
        self.df = df

    def barplot(self, column, title):
        sales_by_column = self.df.groupby(column)[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().sort_values(by=['Global_Sales'],ascending=[False]).head(5).reset_index()
        
        fig = px.bar(sales_by_column, x=column, y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                     barmode='group', labels={'value': 'Total Sales', 'variable': 'Region'}, 
                     title=title)
        return fig

# Load dataset
df = pd.read_csv("dataset/vgsales_after_smoothing.csv")  # Ganti dengan path sesuai lokasi file CSV vgsales

# Create an instance of the SalesBarPlot class
sales_plot = SalesBarPlot(df)

# Top Genre by Sales
top_genre_sales_plot = sales_plot.barplot('Genre', 'Top Genre by Sales')
st.plotly_chart(top_genre_sales_plot)

# Top Platform by Sales
top_platform_sales_plot = sales_plot.barplot('Platform', 'Top Platform by Sales')
st.plotly_chart(top_platform_sales_plot)

# Top Publisher by Sales
top_publisher_sales_plot = sales_plot.barplot('Publisher', 'Top Publisher by Sales')
st.plotly_chart(top_publisher_sales_plot)

top_publisher_sales_plot = sales_plot.barplot('Name', 'Top Publisher by Sales')
st.plotly_chart(top_publisher_sales_plot)
