import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras

(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

print(X_train[0])
