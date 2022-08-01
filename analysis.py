
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



