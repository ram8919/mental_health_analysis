import matplotlib.pyplot as plt
import pandas as pd
from helper import *

data = pd.read_csv(".\input\Mental Health Dataset.csv")# Define a function to create grouped bar plots
def grouped_bar_plot(data, group_cols, value_col):
    
    # Group the data by the specified columns
    grouped_data = data.groupby(group_cols).size().unstack()

    # Plot the grouped data as a bar chart
    grouped_data.plot(kind='bar')

# Import DATA
data=pd.read_csv("/content/Mental Health Dataset.csv")

# Plotting based on coping struggles
grouped_bar_plot(data, ['Country', 'Coping_Struggles'], 'Count')

# Plotting based on gender
grouped_bar_plot(data, ['Country', 'Gender'], 'Count')
print(grouped_bar_plot)

