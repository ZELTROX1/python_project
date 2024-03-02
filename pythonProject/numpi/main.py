import numpy as np
import random

a = np.array([[4.0, 5.0, 6.0], [4.0, 2.0, 3.0]])
# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.data)
# print(a.itemsize)
# b = np.ones((2, 2), dtype='float32')
# print(b)
# c = np.full((1, 4, 4), 99, dtype="float64")
# d = np.full_like(a, 4)
# f = np.random.randint(-4,8, size=(3, 3))
# print(f)
# print(d)
# print(c)
# g=np.array([[1,2,3]])
# print(np.repeat(g,3,axis=0))

#question
# output= np.ones((5,5))
# z=np.zeros((3,3))
# z[1,1]=9
# output[1:4,1:4]=z
# print(output)



# h=np.identity(5)
# print(h)


#coping the arry
# a=np.array([1,2,3])
# b=a.copy()
# print(b)

#Linear algebra

# a= np.ones((2,3))
# print(a)
# b= np.full((3,2),2)
# print(b)
# # print(np.matmul(a,b))
# print(np.linalg.det(np.matmul(a,b)))

#staeistic

# stats = np.array([[1,2,3],[4,5,6]])
# print(np.min(stats))
# print(np.max(stats,axis=1))
# print(np.sum(stats))


#reorganizing array

# before= np.array([[1,2,3,4],[5,6,7,8]])
# print(before.reshape(2,2,2))

#vertical stacking vectors
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
#
# print(np.vstack([v1,v2,v2,v2]))


#genform text
