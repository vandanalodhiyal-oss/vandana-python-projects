# 1d---- without vectorization-----small project---work but large project--slow work
#list compretion
list1 =[1,2,3]
list2 = [3,4,5]

result = [x+y for x,y in zip(list1,list2)]
print(result)

print()

#fast vectorization -------large project---fast work--without loops
import numpy as np
arr1 = np.array([2,3,4])
arr2 = np.array([7,8,9])

result = arr1+arr2
print(result)

print()

#fast vectorization----
import numpy as np

arr = np.array([10,30,40])
multiplied = arr*7
print(multiplied)