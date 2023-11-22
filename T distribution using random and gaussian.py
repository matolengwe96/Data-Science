#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
a = [random.gauss(50,20) for x in range(30)]
b = [random.gauss(55,15) for x in range(30)]


# In[9]:


import seaborn as sns
sns.set_style('darkgrid')
sns.kdeplot(a, fill = True)
sns.kdeplot(b, fill = True)


# In[11]:


import scipy.stats as stats


# In[17]:


t_stat, p_value = stats.ttest_ind(a,b, equal_var = False)
t_stat, p_value


# In[18]:


import numpy as np


# In[20]:


np.mean(a), np.mean(b)


# In[22]:


a = [random.gauss(50,20) for x in range(30)]
b = [random.gauss(60,25) for x in range(30)]


# In[24]:


t_stat, p_value = stats.ttest_rel(a,b)


# In[26]:


t_stat, p_value


# In[27]:


np.mean(a) - np.mean(b)

