#insert.py
"""
np.insert(array,index,value,asxi=none)
array-original array
index-
value-
axis-
axis=0,row-wise
1colum wise
"""

import numpy as np

arr = np.array([20,3,33,44,55,66,77,11,22])
new_arr = np.insert(arr,3,700,)
print(new_arr)

print()


#insert in 2d

import numpy as np

arr_2d = np.array([[44,55] , [11,22]])
print(arr_2d)

#insert a new row at index 1
new_arr_2d = np.insert(arr_2d , 1 , [66,67] , axis=0)
print(new_arr_2d)

print()


#append----new array add

import numpy as np

arr = np.array ([10,20,30])
new_arr = np.append(arr,[500,300,333])
print(new_arr)

print()

#concatenate-----do ya do se jyada array ko joint

"""
np.concatenate((array1,array2,), axis=0)
axis 0> vertical stacking
axis 1> horizontal stacking
"""

import numpy as np
arr1 = np.array([2,33,44])
arr2 = np.array([55,6])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)

print()

#delete function----remove element

"""
np.delete(array,index,axis=none)
flattern array
"""

import numpy as np
arr=([33,33,44,55,66,77,88,99,11])
new_arr =np.delete(arr,6)
print(new_arr)

print()

#delete 2d array----

import numpy as np

arr_2d = np.array([[88,66,55], [33,44,55]])

new_arr_2d = np.delete(arr_2d, 1, axis=1)
print(new_arr_2d)

print()
#stacking &spliting arrays-----combine karna 
"""
vertically
horizontally

vstack() row wise
hstack() column wise
"""

import numpy as np

arr1 = np.array([333,4444,5555,6666,7777,1111,2222])
arr2 = np.array([44,9000,9999,888,77,55,33])

print(np.vstack((arr1,arr2)))  #vertically stack
print(np.hstack((arr1,arr2))) #horizontally

print()
#spliting array---main array ko mutipall array main divid
"""
np.split()
equal

np.hsplit()
np.vsplit()
"""

import numpy as np
arr =np.array([22,33,44,55,66,77,88,88,90])
print(np.split(arr,3))