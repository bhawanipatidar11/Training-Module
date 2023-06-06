import numpy as np

a = np.array([1,2,3])
b = np.array(([1,2],[3,4],[5,6]))
c = np.array((([1,2,3],[4,5,6],[7,8,9])))
print(a)

# print(a[1] + a[2])  adding a values

# print(a[1:3])   slicing
# print(b[2:3])

# print(a.dtype)  finding the data types

x = a.copy()   #copy of a array
x[0] = 12
print(x)

# print(b)
# print(c)

# print(np.__version__)  finding the version of numpy