import numpy as np    # it is an unofficial standard to use np for numpy
import time
# # NumPy routines which allocate memory and fill arrays with value
# a = np.zeros(4);                print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
# a = np.zeros((4,));             print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
# a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# # NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument
# a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
# a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# # NumPy routines which allocate memory and fill with user specified values
# a = np.array([5,4,3,2]);  print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")
# a = np.array([5.,4,3,2]); print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# #vector indexing operations on 1-D vectors
# a = np.arange(10)
# print(a)

# #access an element
# print(f"a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")

# # access the last element, negative indexes count from the end
# print(f"a[-1] = {a[-1]}")

# #indexs must be within the range of the vector or they will produce and error
# try:
#     c = a[9]
#     print(c)
# except Exception as e:
#     print("The error message you'll see is:")
#     print(e)

# #vector slicing operations
# a = np.arange(10)
# print(f"a         = {a}")

# #access 5 consecutive elements (start:stop:step)
# c = a[2:7:1];     print("a[2:7:1] = ", c)

# # access 3 elements separated by two 
# c = a[2:7:2];     print("a[2:7:2] = ", c)

# # access all elements index 3 and above
# c = a[3:];        print("a[3:]    = ", c)

# # access all elements below index 3
# c = a[:3];        print("a[:3]    = ", c)

# # access all elements
# c = a[:];         print("a[:]     = ", c)

# a = np.array([1,2,3,4])
# print(f"a             : {a}")
# # negate elements of a
# b = -a 
# print(f"b = -a        : {b}")

# # sum all elements of a, returns a scalar
# b = np.sum(a) 
# print(f"b = np.sum(a) : {b}")

# b = np.mean(a)
# print(f"b = np.mean(a): {b}")

# b = a**2
# print(f"b = a**2      : {b}")

# a = np.array([ 1, 2, 3, 4])
# b = np.array([-1,-2, 3, 4])
# print(f"Binary operators work element wise: {a + b}")

# #try a mismatched vector operation
# c = np.array([1, 2])
# print(f"c: {c}")
# try:
#     d = a + c
# except Exception as e:
#     print("The error message you'll see is:")
#     print(e)

# a = np.array([1, 2, 3, 4])

# # multiply a by a scalar
# b = 5 * a 
# print(f"b = 5 * a : {b}")

# test 1-D
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
c = np.dot(a, b)
print(f"NumPy 1-D np.dot(a, b) = {c}, np.dot(a, b).shape = {c.shape} ") 
c = np.dot(b, a)
print(f"NumPy 1-D np.dot(b, a) = {c}, np.dot(a, b).shape = {c.shape} ")