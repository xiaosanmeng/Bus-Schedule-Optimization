import csv
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns




df = pd.read_csv('C:/Users/Jonathan/Documents/GitHub/Transloc-Bus-Tracking/data.csv', skiprows= 0)
df['date'] = pd.to_datetime(df[['Month','Day','Year', 'Hour', 'Minute', 'Second']]) # Convert individual date/time cols to single datetime
# df = df.set_index(['date']) # Set the DateTime column to the index
df = df.drop(columns=['Month','Day','Year', 'Hour', 'Minute', 'Second'])    # Deleting unecessay Date/Time cols
# print(df.head(5))

# df1 = df.resample(rule='35Min', on='date').mean()
# # df1 = df1.set_index('date', drop=False)
# # df1 = df1.between_time('0:00','23:59')
# # print(df1.head(5))
# print(df1)

# Weekend RIT Inn
dfwri = df.drop(columns=['Weekend Retail #1','Weekend Retail #2'])
dfwri = dfwri.set_index('date', drop=False)
dfwri = dfwri.between_time('7:00','1:40')
dfwri = dfwri.resample(rule='35Min', on='date').mean()
# print(dfwri)

# # Weekend Retail 1
dfwr1 = df.drop(columns=['Weekend RIT Inn','Weekend Retail #2'])
dfwr1 = dfwr1.set_index('date', drop=False)
dfwr1 = dfwr1.between_time('9:45','22:53')
dfwr1 = dfwr1.resample(rule='87Min', on='date').mean()
# print(dfwr1)

# # Weekend Retail 2
dfwr2 = df.drop(columns=['Weekend RIT Inn','Weekend Retail #1'])
dfwr2 = dfwr2.set_index('date', drop=False)
dfwr2 = dfwr2.between_time('10:30','22:11')
dfwr2 = dfwr2.resample(rule='87Min', on='date').mean()
# print(dfwr2)



dfwr3 = df.drop(columns=['Weekend Retail #1','Weekend Retail #2'])
dfwr3 = dfwr3.set_index('date', drop=False)
dfwr3 = dfwr3.between_time('7:00','1:40')
dfwr3 = dfwr3.resample(rule='35Min', on='date').mean()
print(dfwr3)

vec1 = dfwr3['Weekend RIT Inn']
fig, ax = plt.subplots()
# sns.heatmap([vec1])
# plt.show()
# YlGnBu
ax = sns.heatmap([vec1], xticklabels = dfwr3.index, yticklabels= "Weekend retail 2",cmap="viridis", vmin=0, vmax=5)
plt.show()
