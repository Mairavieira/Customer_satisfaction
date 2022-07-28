
#Import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import the dataset from github
diretorio = 'https://raw.githubusercontent.com/andressaapio/pythontutorials/main/data/olist/' 

#there are 8 tables in csv, they will be imported one by one
# 1 - information about orders 
orders = pd.read_csv(diretorio + 'olist_orders_dataset.csv')
orders.head()
# 2 - order evaluations
order_reviews = pd.read_csv(diretorio + 'olist_order_reviews_dataset.csv')
order_reviews.head()
# 3 - order payment information
order_payments = pd.read_csv(diretorio + 'olist_order_payments_dataset.csv')
order_payments.head()
# 4 - consumer data
customer = pd.read_csv(diretorio + 'olist_customers_dataset.csv')
customer.head()
# 5 - order items
order_items = pd.read_csv(diretorio + 'olist_order_items_dataset.csv')
order_items.head()
# 6 - product information
products = pd.read_csv(diretorio + 'olist_products_dataset.csv')
products.head()
# 7 - information about sellers
sellers = pd.read_csv(diretorio + 'olist_sellers_dataset.csv')
sellers.head()
# 8 - product translation
product_translation = pd.read_csv(diretorio + 'product_category_name_translation.csv')
product_translation

#Merge all consumer datasets
A = pd.merge(orders, order_reviews, on='order_id')
A = pd.merge(A, order_payments,on='order_id')
A = pd.merge(A, customer,on='customer_id')
A.head()

#Merge all seller datasets 
B = pd.merge(order_items,products,on='product_id')
B = pd.merge(B,sellers,on='seller_id')
B = pd.merge(B,product_translation,on='product_category_name')
B.head()

#Merge consumer and seller datasets
df_ecommerce = pd.merge(A, B, on = 'order_id')
df_ecommerce.head()

#Checking column names from the resulting dataset
df_ecommerce.columns

#Selecting desired columns and renaming
df_ecommerce = df_ecommerce[['order_status','order_purchase_timestamp','order_delivered_customer_date','order_estimated_delivery_date',
                              'shipping_limit_date','payment_sequential','payment_type','payment_installments','payment_value',
                              'price','freight_value','product_category_name_english','product_name_lenght','product_description_lenght',
                               'product_photos_qty','review_score']]


df_ecommerce = df_ecommerce.rename(columns={'product_category_name_english': 'product_category'})

#Checking the number of rows and columns of the resulting dataset
df_ecommerce.shape

#removing columns with NULL value
df_ecommerce.isnull().sum()
df_ecommerce.dropna(how='any',inplace=True)

#Converting data and time columns
cols = ['order_purchase_timestamp', 'order_estimated_delivery_date', 'order_delivered_customer_date', 'shipping_limit_date']
for col in cols:
    df_ecommerce[col] = pd.to_datetime(df_ecommerce[col]).dt.date
