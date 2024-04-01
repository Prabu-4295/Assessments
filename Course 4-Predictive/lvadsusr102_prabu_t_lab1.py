# -*- coding: utf-8 -*-
"""LVADSUSR102_prabu_t_LAB1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eyCE82XRUuJSJJHkqBwixg__dRX7RMqW
"""

#1 Random Forest Classfier to find the Wine Quality
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/winequality-red.csv')

# Handling missing values
if data.isna().sum().sum() > 0:
    data.dropna(inplace=True)

# Handling duplicates
data.drop_duplicates(inplace=True)

# Create a new column 'wine_quality' based on 'quality'
data['wine_quality'] = np.where((data['quality'] >= 3) & (data['quality'] <= 6), 'Bad', 'Good')

# Split features and labels
features = data.drop(['quality', 'wine_quality'], axis=1)
labels = data['wine_quality']

# Plotting boxplots before managing outliers
plt.figure(figsize=(9, 5))
sns.boxplot(data=features)
plt.title("Before managing Outliers")
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

# Function to manage outliers
def manage_outliers(data, columns):
    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        median = data[col].median()
        data[col] = np.where((data[col] < lower_bound) | (data[col] > upper_bound), median, data[col])
    return data

# Manage outliers
features = manage_outliers(features, features.columns)

# Plotting boxplots after managing outliers
plt.figure(figsize=(9, 5))
sns.boxplot(data=features)
plt.title("After managing Outliers")
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

# Assigning Test and Training variables
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Execute Random Forest Classification
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# Print predicted values
print("-----predictions-------")
print(predictions)

# Calculate performance metrics
print("----------performance matrices------------")
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')


# Print the performance metrics
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)