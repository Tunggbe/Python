import numpy as numpy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

A = np.array([[2,5,7,9,11,16,19,23,22,29,31,35,37,40,46]]).T
b = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T
ones = np.ones(A.shape, dtype=np.int8)
plt.plot(A,b,'ro')
A = np.concatenate((A, ones), axis=1)
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
print(x)
x0 = np.array([1,46]).T
y0 = x[0][0]*x0 + x[1][0]

plt.plot(x0,y0)


plt.show()