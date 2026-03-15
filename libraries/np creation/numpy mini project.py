# Project sales data analysis

import numpy as np

# Product names
products = np.array(["Laptop","Mobile","Tablet"])

# Sales data (4 days)      (row-day , colums - productes)
sales = np.array([             
[200,300,250],
[400,350,300],
[500,450,400],
[350,300,200]
])

print("Sales Data:")
print(sales)


# 1 Total Sales
total_sales = np.sum(sales)
print("\nTotal Sales:", total_sales)


# 2 Product wise Sales
product_sales = np.sum(sales,axis=0)
print("\nProduct Wise Sales:")
for i in range(len(products)):
    print(products[i],":",product_sales[i])

  
# 3 Day wise Sales
day_sales = np.sum(sales,axis=1)
print("\nDay Wise Sales:",day_sales)


# 4 Average Sales
avg_sales = np.mean(sales)
print("\nAverage Sales:",avg_sales)


# 5 Highest Sale
max_sale = np.max(sales)
print("\nHighest Sale:",max_sale)


# 6 Lowest Sale
min_sale = np.min(sales)
print("\nLowest Sale:",min_sale)


# 7 Filtering (sales greater than 400)         (high sales value filter)
high_sales = sales[sales>400]
print("\nSales greater than 400:",high_sales)


# 8 Indexing example
print("\nDay1 Mobile Sales:",sales[0,1])


# 9 Slicing 
print("\nFirst 2 days sales:")
print(sales[0:2])


# 10 Broadcasting example (bonus sales +50)
bonus_sales = sales + 50
print("\nSales after bonus added:")
print(bonus_sales)