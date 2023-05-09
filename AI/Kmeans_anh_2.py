import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


img = plt.imread("b.jpg")

height = img.shape[0]
width = img.shape[1]

img = img.reshape(height*width,3)
print(img.shape)

kmeans = KMeans(n_clusters = 12, n_init = "auto").fit(img)
clusters = kmeans.cluster_centers_
labels = kmeans.labels_

img2 = np.zeros((height,width,3), dtype=np.uint8)
index = 0
for i in range(height):
	for j in range(width):
		label_of_pixel = labels[index]
		img2[i][j] = clusters[label_of_pixel]
		index += 1
plt.imshow(img2)
plt.show()