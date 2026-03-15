#problem------without brodcasting

prices=[200,400,600]

discount =10 #10%discount

final_prices=[]

for price in prices:
    final_price = price - (price*discount/100)
    final_prices.append(final_price)

print(final_prices)

print()
#solution-----with brodcasting

import numpy as np

prices = np.array([200,400,600])
discount =10 #scaler single value

final_prices = prices - (prices*discount/100)
print(final_prices)

print()
#single value-----brodcasting

import numpy as np

arr = np.array([200,400,600])
result = arr*9
print(result)

print()
#1d  to 2d array------brodcasting

import numpy as np

matrix = np.array([[23,34,45],[11,22,33]])  #2*3 matrix
vector = np.array([33,44,55]) #1d array

result = matrix + vector
print(result)

print()
#error-----incompalitile shape
import numpy as np

arr1 = np.array([[22,33,44],[44,55,77]]) #shape(2,3)
arr2 = np.array([33,44]) #shape(2,)

result = arr1 + arr2

print(result)

#.reshape----shape change ke liye



