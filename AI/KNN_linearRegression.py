import numpy as np
import math
from sklearn import neighbors
import matplotlib.pyplot as plt

# X_train = np.array([[2,5,7,9,11,16,19,23,22,29,31,35,37,40,46]]).T
# y_train = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T

y_train = np.array([[2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]]).T
X_train = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]).T
X_test = np.linspace(2,25,10000).T

knn = neighbors.KNeighborsRegressor(n_neighbors = 3)
knn.fit(X_train,y_train)

y_predict = knn.predict(X_test.reshape(-1,1))
print(X_test)
plt.plot(X_train,y_train, 'ro')
plt.plot(X_test,y_predict)
plt.show()

