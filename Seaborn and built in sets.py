#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
import pandas as pd
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 5, 7, 11]
})

# Scatter plot
sns.scatterplot(x='X', y='Y', data=data)
plt.title('Scatter Plot')
plt.show() 


# In[2]:


# Line plot
sns.lineplot(x='X', y='Y', data=data, marker='o', color='red')
plt.title('Line Plot')
plt.show()


# In[3]:


# Bar plot
sns.barplot(x='X', y='Y', data=data, color='blue')
plt.title('Bar Plot')
plt.show()


# INTERMEDIATE

# In[4]:


# Load a built-in dataset
tips = sns.load_dataset('tips')

# Box plot with categorical data
sns.boxplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('Box Plot with Categorical Data')
plt.show()


# In[7]:


# Pair plot for multiple variables
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species', markers=['o', 's', 'D']) #grouping the data according to species and put markers to differentiate
plt.title('Pair Plot')
plt.show()


# In[10]:


# Correlation heatmap
corr_matrix = iris.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# ADVANCED

# In[14]:


# FacetGrid for faceted visualizations
g = sns.FacetGrid(tips, col='time', row='smoker', margin_titles=True)
g.map(sns.scatterplot, 'total_bill', 'tip')
g.set_axis_labels('Total Bill ($)', 'Tip ($)')
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Faceted Scatter Plot')
plt.show()


# In[16]:


# Print the first few rows of the tips dataset
print(tips.head())


# In[17]:


iris.head()

