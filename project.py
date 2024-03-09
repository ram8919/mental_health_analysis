import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


data = pd.read_csv(".\input\Mental Health Dataset.csv")

df.groupby(['Country', 'Coping_Struggles']).size().unstack().plot(kind='bar')

df.groupby(['Country', 'Gender']).size().unstack().plot(kind='bar')
