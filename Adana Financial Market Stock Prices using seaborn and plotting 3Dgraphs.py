#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


#Import data
df = pd.read_csv("C:/Users/User/Downloads/archive (7)/adani.csv", parse_dates = True)
df.head()


# In[11]:


df['H-L'] = df.high - df.low


# In[13]:


df['100MA'] = df['close'].rolling(100).mean()


# In[15]:


# Set style to darkgrid
sns.set_style('darkgrid')


# In[18]:


#Plotting 3D Graph
ax = plt.axes(projection= '3d') # setting axes
ax.scatter(df.index,df['H-L'],df['100MA'] )
ax.set_xlabel('Index')
ax.set_ylabel('H-L')
ax.set_zlabel('100MA')
plt.show()


# In[20]:


import numpy as np


# In[24]:


z1 = np.linspace(0,10,100)
x1 = np.cos(4 * z1)
y1 = np.sin(4* z1)


# In[25]:


sns.set_style('whitegrid')
ax = plt.axes(projection= '3d') # setting axes
ax.plot3D(x1,y1,z1)
plt.show()

