#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random samples between 0 and 1
random_samples = np.random.uniform(0, 1, 1000)

# Plot a histogram of the random samples
plt.hist(random_samples, bins=20, density=True, alpha=0.6, color='b')
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()

