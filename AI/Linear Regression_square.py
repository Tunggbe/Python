import numpy as numpy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

b = np.array([[2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]]).T
A = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]).T
plt.plot(A,b,'ro')

A_square = np.array([A[:,0]**2]).T
ones = np.ones(A.shape, dtype=np.int8)

A = np.concatenate((A_square, A), axis=1)
A = np.concatenate((A, ones), axis=1)
print(A)

x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
print(x)
x0 = np.linspace(1,25,10000).T
y0 = x[0][0]*(x0**2) + x[1][0]*x0 + x[2][0]
print(y0)
plt.plot(x0,y0)

	


plt.show()