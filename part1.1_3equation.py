import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)

y1 = x**2
y2 = x * np.sin(2 * x)
y3 = np.arctan(x)

plt.plot(x, y1, label='x^2', color='green')
plt.plot(x, y2, label='x * sin(2x)', color='red', linestyle='dashed')
SUNSET_BOULEVARD_COLOR = (247/255,148/255,107/255)
plt.plot(x, y3, label='arctan(x)' , color=SUNSET_BOULEVARD_COLOR, linestyle='dotted')

plt.legend(loc='upper left')
plt.title('Function Graphs')
plt.xlabel('x')
plt.ylabel('y')

plt.show()