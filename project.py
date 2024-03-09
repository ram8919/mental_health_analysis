import matplotlib.pyplot as plt
import pandas as pd
from helper import *

data = pd.read_csv(".\input\Mental Health Dataset.csv")

data.groupby(['Country', 'Gender']).size().unstack().plot(kind='bar')
data.groupby(['Country', 'Coping_Struggles']).size().unstack().plot(kind='bar')

print(bar)
