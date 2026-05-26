import pandas as pd
from spicy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

#using the cleaned data from project 1
file = pd.read_excel('cleaned data set.xlsx')
print('--- the descriptive data ---')
print(file.describe())

#calculating z-scores for Quantity and UnitPrice columns
zscore_Quantity = np.abs(stats.zscore(file['Quantity']))
print('--- Outliers of Quantity column ---')
print(file[zscore_Quantity > 3])

zscore_UnitPrice = np.abs(stats.zscore(file['Quantity']))
print('--- outliers of UnityPrice ---')
print(file[zscore_UnitPrice > 3])

#TotalPrice column is skewed 
#using mean wont be accurate
#calculating the IQR for TotalPrice column
Q1 = file['TotalPrice'].quantile(0.25)
Q3 = file['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1

#using the IQR to determine the outliers
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = file[(file['TotalPrice'] < lower) | (file['TotalPrice'] > upper)]
print('--- outliers of TotalPrice ---')
print(outliers)

#making the charts 
sea.set_theme(style='whitegrid')
plt.figure(figsize=(10,2))
sea.boxplot(x=file['TotalPrice'], color='skyblue' ,flierprops=dict(markerfacecolor='red' , markersize= 10 , markeredgecolor='darkred'))

#the outlirs of TotalPrice column 
plt.title('TotalPrice distribution: revenue driven by VIP spenders' , fontsize=14 , fontweight='bold')
plt.xlabel('Total price')
plt.show()

#the correlation heatmap
correlation_matrix = file.corr(numeric_only=True)
plt.figure(figsize=(8 , 6))
sea.heatmap(correlation_matrix , annot=True , cmap='coolwarm' , fmt=".2f" , linewidths=0.5 , vmin=-1 , vmax=1)
plt.title('variable relationship: correlation heatmap', fontsize=14 , fontweight='bold')
plt.show()