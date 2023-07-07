import numpy as np

list1 = [[10,20,30], [40,50,60], [70,80,90]]

arr = np.array(list1)
print(arr)

print(type(arr))  # <class 'numpy.ndarray'>


arr = np.array(list1,ndmin=4)
print(arr)

print(arr.size)  # 9
print(np.size(arr,0)) # 1
print(np.size(arr,1)) # 1

print(arr.shape)  # (1, 1, 3, 3)

print(arr.dtype)
print(arr.ndim)  # 4

arr0 = np.zeros((2,3))
print(arr0)

arr1 = np.ones((3,3))
print(arr1)

# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

ar = np.random.random((3,3))
print(ar)

# Arange Function

print(np.arange(1,11,3))  # [ 1  4  7 10]
print(np.linspace(1,11,3))

np.reshape(arr1, (3,3))
print(arr1)


print(arr1.flatten())

print(arr1.max(axis=1)) # 1.0
print(arr1.std()) # 0.0

arr1 = arr1 // 2
print(arr1)