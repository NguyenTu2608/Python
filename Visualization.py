import pandas as pd
import matplotlib.pyplot as plt

customer_df = pd.read_csv('customer_data.csv')
product_detail_df = pd.read_csv('product_detail_data.csv')
market_trend_df = pd.read_csv('market_trend_data.csv')
product_group_df = pd.read_csv('product_group_data.csv')
sales_df = pd.read_csv('sale_data.csv')
website_access_df = pd.read_csv('website_access_data.csv')

print(sales_df.head())

product_sales = sales_df.groupby('ProductID')['TotalAmount'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(product_sales['ProductID'], product_sales['TotalAmount'])
plt.title('Revenue by product')
plt.xlabel('Product ID')
plt.ylabel('Total Revenue')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


sales_df = pd.read_csv('sale_data.csv')


sales_df['SaleDate'] = pd.to_datetime(sales_df['SaleDate'])


daily_sales = sales_df.groupby('SaleDate')['TotalAmount'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.plot(daily_sales['SaleDate'], daily_sales['TotalAmount'], marker='o', linestyle='-', color='b')
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



df = pd.read_csv('product_group_data.csv')


print(df.head())


group_discounts = df.groupby('GroupName')['DiscountPercentage'].mean().reset_index()

# Tạo biểu đồ cột
plt.figure(figsize=(10, 6))
plt.bar(group_discounts['GroupName'], group_discounts['DiscountPercentage'])
plt.title('Discounts by Product Group')
plt.xlabel('Product Group')
plt.ylabel('Discount Percentage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()