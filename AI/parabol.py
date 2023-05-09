import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.animation as animation

def cost(x):
	m = A.shape[0]
	return 1/2*m * np.linalg.norm(A.dot(x) - b, 2)**2
def grad(x):
	m = A.shape[0]
	return 1/m * A.T.dot(A.dot(x)-b)

def gradient_descent(x_init, learning_rate, iteration):
	x_list = [x_init]
	for i in range(iteration):
		x_new = x_list[-1] - learning_rate*grad(x_list[-1])
		x_list.append(x_new)
	return x_list 

b = np.array([[2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]]).T
A = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]).T
fig1 = plt.figure('Gradient descent for linear regression -- parabol')
ax = plt.axes(xlim=(-10,50), ylim=(-10,50))
plt.plot(A,b,'ro')

A_square = np.array([A[:,0]**2]).T
ones = np.ones(A.shape, dtype= np.int8)
A = np.concatenate((A_square, A), axis=1)
A = np.concatenate((A, ones), axis=1)

lr = linear_model.LinearRegression()
lr.fit(A,b)
print(lr.coef_)
print(lr.intercept_)
x0 = np.linspace(1,46,10000).T
y0 = lr.coef_[0][0]*(x0**2) + lr.coef_[0][1]*x0 + lr.intercept_[0]
plt.plot(x0,y0, color="green")

#
x_init = np.array([[-3],[3],[-2.1]])
y0_init = x_init[0][0]*x0**2 + x_init[1][0]*x0 + x_init[2][0]


iteration = 70
learning_rate = 0.000001
x_list = gradient_descent(x_init, learning_rate, iteration)

line , = ax.plot([],[], color="blue")
def update(i):
	y0_list = x_list[i][0]*(x0**2) +x_list[i][1]*x0 + x_list[i][2]
	line.set_data(x0,y0_list)
	return line,
iters = np.arange(1,len(x_list),1)
line_ani = animation.FuncAnimation(fig1, update, iters, interval=50, blit=True)

for i in range(len(x_list)):
	y0_list = x_list[i][0]*(x0**2) +x_list[i][1]*x0 + x_list[i][2]
	plt.plot(x0,y0_list, color = 'black', alpha = 0.2)

plt.show()
