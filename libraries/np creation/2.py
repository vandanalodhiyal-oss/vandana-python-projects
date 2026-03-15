#with default values
#np.zeros(shape) (4) fir 1d, (4,4)2d

import numpy  as np
zeros_array = np.zeros(4)
print(zeros_array)

#ones(shape)

import numpy as np
ones_array = np.ones((4,5))
print(ones_array)

#full(shape,value)

import numpy as np
filled_array = np.full((3,3),9)
print(filled_array)

#creating sequence of numbers in numpy
#arrange()
#arange(start,stop,step)

import numpy as np
arr = np.arange(1,10,4)
print(arr)

#creating identity matrices
#eye(size)

import numpy as np
identity_metrix = np.eye(9)
print(identity_metrix)