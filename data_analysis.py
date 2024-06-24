#data_analysis.py
import pandas as pd

def calculate_statistics(data):
    return {
        "mean": data.mean(),
        "median": data.median(),
        "std_dev": data.std()
    }

def filter_data(data, column, value):
    return data[data[column] == value]