from sklearn import datasets
import numpy as np

def calculate_distance(p1,p2):
	distance = 0
	for i in range(p1.shape[0]):
		distance += (p1[i] - p2[i])**2
	distance = distance**1/2
	return distance
	
def get_k_neighbors(training_X, label_y, point, k):
	distances = []
	for i in range(training_X.shape[0]):
		distance = calculate_distance(training_X[i], point)
		distances.append(distance)	
	neighbors = []
	for i in range(k):
		index_labels = distances.index(min(distances))
		neighbor = label_y[index_labels]
		neighbors.append(neighbor)
		distances.pop(index_labels)
	return neighbors

def highest_votes(labels):
	final_labels = min(set(labels), key=labels.count)
	return final_labels

def predict(training_X, label_y, point, k):
	neighbors_labels = get_k_neighbors(training_X, label_y, point, k)
	return highest_votes(neighbors_labels)

def accuracy_score(predict, labels):
	accuracy = 0
	for i in range(len(labels)):
		if predict[i] == labels[i]:
			accuracy += 1
	return accuracy/len(predict)*100



iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

randIndex = np.arange(iris_X.shape[0])
np.random.shuffle(randIndex)

iris_X = iris_X[randIndex]
iris_y = iris_y[randIndex]

X_train = iris_X[:100,:]
X_test = iris_X[100:,:]
y_train = iris_y[:100]
y_test = iris_y[100:]
print(y_train)
k = 5
# y_predict = []
# for p in X_test:
# 	label = predict(X_train, y_train, p, 5)
# 	y_predict.append(label)

# acc = accuracy_score(y_predict,y_test)
# print(acc)
print(X_test[0])
print(get_k_neighbors(X_train, y_train, X_test[0], 5))
