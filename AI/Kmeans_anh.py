import matplotlib.pyplot
from sklearn.cluster import KMeans
import numpy as np


img = matplotlib.pyplot.imread("b.jpg")

height = img.shape[0]
width = img.shape[1]

img = img.reshape(height*width,3)
print(img.shape)

kmeans = KMeans(n_clusters = 12, n_init = "auto").fit(img)
clusters = kmeans.cluster_centers_
labels = kmeans.labels_

print(len(labels))

img2 = np.zeros_like(img)

for i in range(len(img2)):
	img2[i] = clusters[labels[i]]

img2 = img2.reshape(height, width,3)
matplotlib.pyplot.imshow(img2)
matplotlib.pyplot.show()

