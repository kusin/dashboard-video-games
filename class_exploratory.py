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

    def get_sum_of_sales_regions(self):
        df = self.get_dataset()
        sum_na = np.round(df["NA_Sales"].sum(), 2)
        sum_eu = np.round(df["EU_Sales"].sum(), 2)
        sum_jp = np.round(df["JP_Sales"].sum(), 2)
        sum_ot = np.round(df["Other_Sales"].sum(), 2)
        return sum_na, sum_eu, sum_jp, sum_ot