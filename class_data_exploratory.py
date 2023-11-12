# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# call method from other file
from class_dataset import dataset

# define class exploratory
class exploratory:

    def get_dataset(self):
        df = dataset().get_dataset()
        return df

    def get_sum_of_video_games_sales(self):
        df = self.get_dataset()
        sum_na = np.round(df["NA_Sales"].sum(), 2)
        sum_eu = np.round(df["EU_Sales"].sum(), 2)
        sum_jp = np.round(df["JP_Sales"].sum(), 2)
        sum_ot = np.round(df["Other_Sales"].sum(), 2)
        sum_global = np.round(df["Global_Sales"].sum(),2)
        return sum_na, sum_eu, sum_jp, sum_ot, sum_global
    
    def get_sum_of_sales_by_region(self):
        df = self.get_dataset()
        df = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().sort_values(ascending=False).reset_index()
        df.columns = ["Region", "Sales"]
        return df
    
    def get_sum_of_sales_by_year(self):
        df = self.get_dataset()
        df = df.groupby(by=['Year'])['Global_Sales'].sum().reset_index()
        df.sort_values(by="Year")
        return df