#isnan-----syntex(np.isnan(array))

import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])

print(np.isnan(arr))

#nan value replace
#nan to numpy------value ko replace krna
#np.nan_to_num(array,nan=value) default-0

import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])

cleaned_arr = np.nan_to_num(arr,nan=100)
print(cleaned_arr)

#infinte function----np.isinf() 10^100
#1/0

import numpy as np

arr= np.array([2,3,np.inf,5,-np.inf,7])
print(np.isinf(arr))