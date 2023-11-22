#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, beta, lognorm

# Set a random seed for reproducibility
np.random.seed(0)

# Define the range of x values
x = np.linspace(-3, 3, 1000)

# Generate PDFs for different continuous distributions
uniform_pdf = np.ones_like(x) / (1 - 0)
normal_pdf = norm.pdf(x, loc=0, scale=1)
exponential_pdf = expon.pdf(x, scale=1)
beta_pdf = beta.pdf(x, a=2, b=5)
lognormal_pdf = lognorm.pdf(x, s=1)

# Create subplots to display the PDFs
fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# Plot Uniform Distribution PDF
axs[0, 0].plot(x, uniform_pdf, color='b', label='Uniform PDF')
axs[0, 0].set_title('Uniform Distribution')

# Plot Normal Distribution PDF
axs[0, 1].plot(x, normal_pdf, color='r', label='Normal PDF')
axs[0, 1].set_title('Normal Distribution')

# Plot Exponential Distribution PDF
axs[0, 2].plot(x, exponential_pdf, color='m', label='Exponential PDF')
axs[0, 2].set_title('Exponential Distribution')

# Plot Beta Distribution PDF
axs[1, 0].plot(x, beta_pdf, color='c', label='Beta PDF')
axs[1, 0].set_title('Beta Distribution')

# Plot Log-Normal Distribution PDF
axs[1, 1].plot(x, lognormal_pdf, color='g', label='Log-Normal PDF')
axs[1, 1].set_title('Log-Normal Distribution')

# Remove x and y axis labels for better readability
for ax in axs.flat:
    ax.set(xlabel='Value', ylabel='Probability')

# Add legends
for ax in axs.flat:
    ax.legend(loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()

