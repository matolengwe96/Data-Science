#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("C:/Users/User/Downloads/housing.csv/housing.csv")
df = pd.DataFrame(data)

# Select features for clustering
features_for_clustering = ['housing_median_age', 'median_income', 'median_house_value']
X = df[features_for_clustering]

# Specify the number of clusters
n_clusters = 3  # You can choose the number of clusters based on your requirements

# Apply K-means clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(df['housing_median_age'], df['median_income'], df['median_house_value'], c='r', marker='o')

# Set labels for each axis
ax.set_xlabel('Housing Median Age')
ax.set_ylabel('Median Income')
ax.set_zlabel('Median House Value')

# Set the title
ax.set_title('3D Scatter Plot of Housing Data')
# Rotate the view
ax.view_init(elev=20, azim=30)  # Adjust the elevation (elev) and azimuth (azim) angles

# Create a pairplot with hue for clusters
sns.set(style="whitegrid")
sns.pairplot(df, vars=features_for_clustering, hue='cluster', palette='viridis', plot_kws={'alpha': 0.5})
plt.suptitle('Pairplot with Clusters', y=1.02)

# Show the plot
plt.show()


# In[ ]:




