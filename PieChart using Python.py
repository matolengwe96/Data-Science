#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Import libraries
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


#Create a list of causes of death
causes = [ ' HIV', 'TB', 'Diabetes', 'Cancer','High Blood']
percentage = [40,15,5,25,15] 


# In[22]:


plt.figure(figsize =(15,10))
explode=[0,0.1,0,0,0] # explode TB to be visible
plt.pie(percentage, labels = causes, explode = explode, autopct = '%2.1f%%', startangle = 90)
#plt.axis('Equal')
plt.title('Pie chart')
plt.show()

