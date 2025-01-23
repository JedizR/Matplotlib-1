import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('Points Data.csv', delimiter=',')
distances = np.genfromtxt('Distances Data.csv', delimiter=',')

plt.scatter(data[:,0], data[:,1], c=distances, cmap=plt.cm.get_cmap('viridis', 5))

plt.show()