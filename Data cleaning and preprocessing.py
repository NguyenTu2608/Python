import pandas as pd

customer_df = pd.read_csv('customer_data.csv')
product_detail_df = pd.read_csv('product_detail_data.csv')
market_trend_df = pd.read_csv('market_trend_data.csv')
product_group_df = pd.read_csv('product_group_data.csv')
sales_df = pd.read_csv('sale_data.csv')
website_access_df = pd.read_csv('website_access_data.csv')

#Print the few rows of dataframe
print("customer_df:\n", customer_df.head())
print("product_detail_df:\n", product_detail_df.head())
print("market_trend_df:\n", market_trend_df.head())
print("product_group_df:\n", product_group_df.head())
print("sales_df:\n", sales_df.head())
print("website_access_df:\n", website_access_df.head())


#Check the data type of columns
print("customer_df data types:\n", customer_df.dtypes)
print("product_detail_df data types:\n", product_detail_df.dtypes)
print("market_trend_df data types:\n", market_trend_df.dtypes)
print("product_group_df data types:\n", product_group_df.dtypes)
print("sales_df data types:\n", sales_df.dtypes)
print("website_access_df data types:\n", website_access_df.dtypes)


print('')

#Check for missing values
print("customer_df missing value:\n", customer_df.isnull().sum())
print("product_detail_df missing value:\n", product_detail_df.isnull().sum())
print("market_trend_df missing value:\n", market_trend_df.isnull().sum())
print("product_group_df missing value:\n", product_group_df.isnull().sum())
print("sales_df missing value:\n", sales_df.isnull().sum())
print("website_access_df missing value:\n", website_access_df.isnull().sum())

print('')

#Handle missing values
customer_df = customer_df.dropna()
product_detail_df = product_detail_df.dropna()
market_trend_df = market_trend_df.dropna()
product_group_df = product_group_df.dropna()
sales_df = sales_df.dropna()
website_access_df = website_access_df.dropna()