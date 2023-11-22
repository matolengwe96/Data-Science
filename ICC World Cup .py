#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/User/Downloads/archive (3)/CWC23_all_innings.csv")
df.head()


# In[22]:


df.columns


# In[23]:


df.plot(x = 'team', y ='runs', kind = 'scatter',legend = True)


# In[21]:


df.plot()


# In[25]:


df['runs'].plot(legend = True)


# In[48]:


# Create a bar graph
plt.bar(df['team'],df['runs'])

# Add labels and title
plt.xlabel('team')
plt.ylabel('runs')
plt.title('Bar Graph of Runs by Teams in ICC World Cup 2023')

# Show the plot
plt.show()


# In[51]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import random
# Create a figure and axis
fig, ax = plt.subplots()


# Define colors for the bars (you can customize this list)
n = 10 #Number of players
bar_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(n+1)] #n +1 to include the last one

# Assuming df is the DataFrame with 'Player' and 'Wickets' columns
top_10_players = df.nlargest(n, 'wkts')

# Create a bar graph
plt.bar(top_10_players['player'], top_10_players['wkts'], color = bar_colors)
# Add labels and title
plt.xlabel('Players')
plt.ylabel('Wickets Taken')
plt.title('Top 10 Wicket Takers')
# Rotate x-axis labels by 90 degrees
plt.xticks(rotation= 75)

# Adjust layout to prevent clipping of labels
plt.tight_layout()


# Show the plot
plt.show()


# In[ ]:




