#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Define the range of x values
x = np.linspace(0, 5, 1000)

# Generate the PDF for the exponential distribution
exponential_pdf = expon.pdf(x, scale= 0.1)

# Create a subplot for the exponential distribution PDF
plt.figure(figsize=(8, 4))
plt.plot(x, exponential_pdf, color='m', label='Exponential PDF')
plt.title('Exponential Distribution PDF')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend(loc='upper right')
plt.grid(True)

# Show the plot
plt.show()


# In[ ]:




