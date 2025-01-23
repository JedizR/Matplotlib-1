import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('Values for Histogram.csv', delimiter=',')

plt.hist(data, bins=50)

plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Counts')

plt.show()
