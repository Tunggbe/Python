import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
import random

def cost(x):
	m = A.shape[0]
	return 0.5/m * np.linalg.norm(A.dot(x) - b, 2)**2

def grad(x):
	m = A.shape[0]
	return 1/m * A.T.dot(A.dot(x)-b)

def gradient_descent(x_init, learning_rate, iteration):
	x_list = [x_init]
	m = A.shape[0]
	for i in range(iteration):
		x_new = x_list[-1] - learning_rate*grad(x_list[-1])
		if np.linalg.norm(grad(x_new))/m < 0.5:
			break
		x_list.append(x_new)
	return x_list

A = np.array([[2,5,7,9,11,16,19,23,22,29,31,35,37,40,46]]).T
b = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T

ones = np.ones(A.shape,dtype=np.int8)
fig1 = plt.figure('Gradient descent for linear regression')
ax = plt.axes(xlim=(-10,60), ylim=(-1,20))
plt.plot(A,b, 'ro')


lr = linear_model.LinearRegression()
lr.fit(A,b)
x0_gd = np.linspace(1,46,2)
y0_sklearn =lr.coef_[0][0]*x0_gd + lr.intercept_[0]
plt.plot(x0_gd, y0_sklearn, color="green")
A = np.concatenate((ones, A), axis = 1)
#
x_init = np.array([[1.],[2.]])
y0_init = x_init[0][0]*x0_gd + x_init[1][0] 
plt.plot(x0_gd,y0_init)

iteration = 1000
learning_rate = 0.0001
x_list = gradient_descent(x_init,learning_rate,iteration)

for i in range(len(x_list)):
	y0_x_list = x_list[i][0] + x_list[i][1]*x0_gd
	plt.plot(x0_gd, y0_x_list, color="black")

plt.show()

cost_value = []
interation_value = []
for i in range(len(x_list)):
	interation_value.append(i)
	cost_value.append(cost(x_list[i]))

plt.plot(interation_value, cost_value)

plt.show()