#!/usr/bin/env python
# coding: utf-8

# In[14]:


import scipy.stats as stats 
import matplotlib.pyplot as plt

# Define the rate parameter lambda
lambda_parameter = 3.0

# Generate random samples
random_samples = stats.poisson.rvs(lambda_parameter, size=1000)

# Plot a histogram of the random samples
plt.hist(random_samples, bins=30, density=True, alpha=0.8, color='b')
plt.title('Poisson Distribution')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.show()


