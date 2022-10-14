from pickletools import pylist
import numpy as np  

# python list 
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array 
np_array = np.array([1,2,3,4,5,6,7,8,9])
print(type(np_array))
print(type(py_list))

py_multi = [[1,2,3],[4,5,6],[7,8,9]] # 2-dimensional list
np_multi = np_array.reshape(3,3)

print(py_multi) # List 2-dimensional
print(np_multi) # Array 2-dimensional

print(np_array.ndim) # 1-dimensional 
print(np_multi.ndim) # 2-dimensional

print(np_array.shape)
print(np_multi.shape)