
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

#Generating graphics of review'score with seaborn
sns.histplot(x='review_score', data=df_ecommerce)

#Generating graphics of estimated days of delivered with seaborn
sns.histplot(x='estimated_days', data=df_ecommerce)

#Generating graphics of payment values with seaborn
sns.histplot(x='payment_value', data=df_ecommerce)
plt.xlim([0,2000])

#Generating graphics of payment types with seaborn
sns.histplot( x='payment_type', data=df_ecommerce)

#Bar graph definition of "The 10 most purchased products by customers"
fig = plt.figure(figsize = fig_size)

sns.barplot(x = df_ecommerce.product_category.value_counts().index[:10], 
            y = df_ecommerce.product_category.value_counts()[:10])

#"The 10 most purchased products by customers"
plt.xlabel('Product category', fontsize = font_size)
plt.ylabel('Order quantity', fontsize = font_size)
plt.title("The 10 most purchased products by customers", fontsize = title_font_size)

plt.show()

#Bar graph definition for graphs
def bar_plot_df(x_var, y_var, title):
  fig = plt.figure(figsize = fig_size)
  sns.barplot(x = x_var, 
              y = y_var, data=df_ecommerce)
 
  plt.xlabel(x_var, fontsize = font_size)
  plt.ylabel(y_var, fontsize = font_size)
  plt.title(title, fontsize = title_font_size)
  plt.show()
  
  #Payment amount per customer based on payment type
  bar_plot_df('payment_type', 'payment_value', 'Payment amount per customer based on payment type')
  
  #Customer rating based on transaction value
  bar_plot_df('review_score', 'payment_value', 'Customer rating based on transaction value')
  
  #Customer rating based on the value of each item
  bar_plot_df('review_score', 'price', 'Customer rating based on the value of each item')
  
  #Customer rating based on shipping cost
  bar_plot_df('review_score', 'freight_value', 'Customer rating based on shipping cost')
