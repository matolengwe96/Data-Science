#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Sample data
data = {'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
        'Category': ['A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40]}

df = pd.DataFrame(data)

# Pivot the data
pivot_df = df.pivot(index='Date', columns='Category', values='Value')

print(pivot_df)


# In[3]:


df


# ISNA functio

# In[8]:


import pandas as pd

# Create a DataFrame with missing values
data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]}
df = pd.DataFrame(data)

# Check for missing values
missing_values = df.isna()

print(missing_values)


# In[10]:


# Create a Series with missing values
s = pd.Series([1, 2, None, 4])

# Check for missing values
missing_values = s.isna()

print(missing_values)


# ILOC FUNCTION

# In[15]:


# Create a DataFrame
dataB = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(dataB)
df
# Select specific rows and columns using iloc
subset_iloc = df.iloc[0:2, 1:3]

print(subset_iloc)


# In[16]:


# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Select the second row using iloc
row_iloc = df.iloc[1]

print(row_iloc)

