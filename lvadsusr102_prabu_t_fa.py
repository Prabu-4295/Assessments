# -*- coding: utf-8 -*-
"""LVADSUSR102-Prabu T-FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7SEwdezbvNJdHMh6FP0cORE2FO1z94U

**Python Final Assessment**

Name : Prabu T

Emp ID : 4295

**1. Load dataset**

Examine the basic informations like numerical ,categorical,no of rows and column.
"""

#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')
df=pd.DataFrame(data)
df.info()
print(df.describe())
df.dtypes

#3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')
df=pd.DataFrame(data)
sales_mean=df['Sales'].mean()
sales_median=df['Sales'].median()
sales_std=df['Sales'].std()
sales_variance=df['Sales'].var()

profit_mean=df['Profit'].mean()
profit_median=df['Profit'].median()
profit_std=df['Profit'].std()
profit_variance=df['Profit'].var()

quantity_mean=df['Quantity'].mean()
quantity_median=df['Quantity'].median()
quantity_std=df['Quantity'].std()
quantity_variance=df['Quantity'].var()

print("Mean of Sales : ",sales_mean)
print("Median of Sales : ",sales_median)
print("Standard deviation of Sales : ",sales_std)
print("Variance of Sales : ",sales_variance)
print("---------------------------")
print("Mean of profit : ",profit_mean)
print("Median of profit : ",profit_median)
print("Standard deviation of profit : ",profit_std)
print("Variance of Profit : ",profit_variance)
print("---------------------------")
print("Mean of quantity : ",quantity_mean)
print("Median of quantity : ",quantity_median)
print("Standard deviation of quantity : ",quantity_std)
print("Variance of quantity : ",quantity_variance)

#4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')

# Bar chart: Total sales by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=data)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Line chart: Sales trend over time
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.month
sales_over_time = data.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sales', hue='Year', data=sales_over_time)
plt.title('Sales Trend Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Box plot profits by category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Profit', data=data)
plt.title('Profits by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.show()

# Pie chart sales by geography
plt.figure(figsize=(8, 8))
sales_by_geography = data.groupby('Geography')['Sales'].sum()
sales_by_geography=sales_by_geography.head()
plt.pie(sales_by_geography, labels=sales_by_geography.index, autopct='%1.1f%%')
plt.title('Sales by Geography')
plt.show()

# Histogram Distribution of sales quantities
plt.figure(figsize=(10, 6))
sns.histplot(data['Quantity'], bins=20, kde=True)
plt.title('Distribution of Sales Quantities')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Relationship between sales and profits
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Profit', data=data)
plt.title('Relationship between Sales and Profits')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

#5 identifying relationship
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')

# Compute the correlation matrix
correlation_matrix = data.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

#7(1) Trend Analysis
#(ii)
import pandas as pd

data=pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')

df=pd.DataFrame(data)

data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
category_yearly_sales = df.groupby(['Category', 'Year'])['Sales'].sum().reset_index()
category_yearly_sales['Yearly Growth Rate'] = category_yearly_sales.groupby('Category')['Sales'].pct_change() * 100

highest_growth_category = category_yearly_sales.groupby('Category')['Yearly Growth Rate'].mean().idxmax()

print("Product category with the highest growth rate:", highest_growth_category)

print()
print()

"""#7. Customer Analysis
 We can able to see that these 5 customers are reptatively ordering over the months .
"""

#7(2) Customer Analysis
#(i)
import pandas as pd


data = pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')

customer_orders_sales = data.groupby('EmailID').agg({'Order ID': 'nunique', 'Sales': 'sum'})
customer_orders_sales = customer_orders_sales.rename(columns={'Order ID': 'NumOrders'})
customer_orders_sales = customer_orders_sales.sort_values(by=['NumOrders', 'Sales'], ascending=False)

top_5_customers = customer_orders_sales.head(5)

print("Top 5 Customers based on Number of Orders and Total Sales:")
print(top_5_customers)

for email_id, row in top_5_customers.iterrows():
    print("\nCustomer:", email_id)
    print("Total Orders:", row['NumOrders'])
    print("Total Sales:", row['Sales'])

#2)

#7(2)
#(ii)
import pandas as pd

data=pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')

df=pd.DataFrame(data)
df['Order Date'] = pd.to_datetime(df['Order Date'])

df.sort_values(by=['EmailID', 'Order Date'], inplace=True)


df['TimeDifference'] = df.groupby('EmailID')['Order Date'].diff()


avg_time_between_orders = df.groupby('EmailID')['TimeDifference'].mean()

print("Average time between orders for each customer:")
print(avg_time_between_orders)

"""**Comprehensive Analysis**

1.
Based on insights from sales velocity and order fulfillment data, several strategies can be implemented to optimize the supply chain:

Inventory Management: Utilize sales velocity data to forecast demand accurately and adjust inventory levels accordingly. Implement just-in-time inventory practices to minimize excess stock while ensuring products are available when needed.

Supplier Collaboration: Build strong relationships with suppliers and leverage order fulfillment data to negotiate favorable terms, lead times, and pricing. Implement vendor-managed inventory systems to streamline the replenishment process and reduce stockouts.


2.
Market Segmentation: Analyze sales data to identify key demographic segments and geographic areas with high growth potential. Tailor marketing messages and promotions to resonate with the preferences and needs of these target segments.

Location-based Marketing: Use geolocation data to target consumers with personalized offers, promotions, and advertisements based on their proximity to retail locations or specific geographic regions.

Regional Campaigns: Develop marketing campaigns that highlight local trends, events, or cultural nuances to resonate with consumers in different geographic areas. Customize messaging and imagery to reflect the unique characteristics of each region.
"""