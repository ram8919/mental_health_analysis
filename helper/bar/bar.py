import numpy as np
import pandas as pd

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

data=pd.read_csv("/content/Mental Health Dataset.csv")
data.groupby(['Country', 'Gender']).size().unstack().plot(kind='bar')
data.groupby(['Country', 'Coping_Struggles']).size().unstack().plot(kind='bar')
