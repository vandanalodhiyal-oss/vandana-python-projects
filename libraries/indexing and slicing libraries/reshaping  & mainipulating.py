"""
reshap(row,colums) specify new shape
if dimensions match
"""
#reshape.py
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
reshape_arr = arr.reshape(3,3)
print(reshape_arr)

print()

#flattening array-----1-ravel , 2-flatten  (multidime array * 1d (convert))
"""
.ravel() -> viwe return
.flatten()-> copy return
"""
import numpy as np
arr_2d = np.array([[1,2,3] , [4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())


