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
    
    def get_sum_of_sales_by_year(self):
        df = self.get_dataset()
        df = df.groupby(by=['Year'])['Global_Sales'].sum().reset_index()
        df.sort_values(by="Year")
        return df
    
    def get_sum_of_sales_by_region(self):
        df = self.get_dataset()
        df = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().sort_values(ascending=False).reset_index()
        df.columns = ["Region", "Sales"]
        return df
    
    def get_best_genre(self):
        df = self.get_dataset()
        df = df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).head(5).reset_index()
        return df