import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('Values for Bars.csv', delimiter=',')

grouped_data = {}
for value in data:
    if value in grouped_data:
        grouped_data[value] += 1
    else:
        grouped_data[value] = 1

plt.bar(list(grouped_data.keys()), list(grouped_data.values()))
plt.title('Bar')
plt.xlabel('Values')
plt.ylabel('Counts')

plt.show()