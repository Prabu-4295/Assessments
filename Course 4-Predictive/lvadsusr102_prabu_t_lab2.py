# -*- coding: utf-8 -*-
"""LVADSUSR102_prabu_t_LAB2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U_HPdOSK3h295aYc_hwmgiy7bNEh81xM
"""

#2 K means Clustering
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/Mall_Customers.csv')


# EDA
# Handle Missing Values
if data.isna().sum().sum() > 0:
    data.dropna(inplace=True)

# Handling duplicates
data.drop_duplicates(inplace=True)

# encoding character data into numerical data
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])


imputer = SimpleImputer(strategy='mean')
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Feature Engineering
data_imputed['Spending_to_Income_Ratio'] = data_imputed['Spending Score (1-100)'] / data_imputed['Annual Income (k$)']

# Normalization
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_imputed)

# finding Number of Clusters
wcss = []
silhouette_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(data_scaled, kmeans.labels_))

# Elbow Method
plt.plot(range(2, 11), wcss, marker='o',color='blue')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Silhouette Score Analysis
plt.plot(range(2, 11), silhouette_scores, marker='o',color='red')
plt.title('Silhouette Score Analysis')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()


# K-Means Clustering
optimal_num_clusters = 5
kmeans = KMeans(n_clusters=optimal_num_clusters,n_init=10, random_state=42)
kmeans.fit(data_scaled)
clusters = kmeans.predict(data_scaled)

# Cluster Analysis
cluster_df = pd.DataFrame(data_scaled, columns=data_imputed.columns)
cluster_df['Cluster'] = clusters

# Cluster Profiling
cluster_means = cluster_df.groupby('Cluster').mean()
cluster_means

""" **e. Strategy Development Based on Clusters**

 **Targeted Marketing Strategies**

 Develop strategies tailored to the distinct preferences and behaviors of each cluster
 For example, for clusters with high spending scores, offer exclusive deals and promotions

 **Customer Experience Improvement**

 Identify opportunities to enhance the shopping experience for different segments.
 For clusters with younger customers, focus on online shopping features and social media engagement
"""