#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('music_data.csv')
print(df.head())
numeric_df = df.select_dtypes(include='number')
plt.figure(figsize=(12, 8))
correlation = numeric_df.corr() 
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
print("\nDataset Info:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())
print("\nMissing Values in Dataset:")
print(df.isnull().sum())
plt.figure(figsize=(10, 6))
sns.histplot(df['popularity'], kde=True)
plt.title('Distribution of Popularity')
plt.show()
plt.figure(figsize=(10, 6))
sns.histplot(df['danceability'], kde=True)
plt.title('Distribution of Danceability')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['duration_ms'])
plt.title('Boxplot of Song Duration (ms)')
plt.show()
plt.figure(figsize=(12, 8))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
plt.figure(figsize=(10, 6))
sns.scatterplot(x='danceability', y='popularity', data=df)
plt.title('Danceability vs Popularity')
plt.show()
sns.pairplot(df[['danceability', 'energy', 'popularity', 'tempo']])
plt.show()


# In[ ]:




