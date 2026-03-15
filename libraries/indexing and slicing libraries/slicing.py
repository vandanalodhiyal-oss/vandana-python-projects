"""
slicing

array[start:stop:step]

array[start:end], start to end -1

negative step, -1 revere
"""
import numpy as np
arr=np.array ([20,55,66,33,455,88,55,66,66,44,44,55])

print(arr[1:5]) #index 1to 7
print(arr[1:3]) #index 1to3
print (arr[:8]) #index 0 to8
print(arr[::3]) #every thrid element
print (arr[::-2])