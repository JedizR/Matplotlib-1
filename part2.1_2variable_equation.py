import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z1 = X * Y
Z2 = X**2 + Y**2
Z3 = np.sin(3*X)*Y

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].contourf(X, Y, Z1, levels=np.linspace(np.min(Z1), np.max(Z1), 20))
axs[0].set_title('f(x, y) = x*y')
axs[1].contourf(X, Y, Z2, levels=np.linspace(np.min(Z2), np.max(Z2), 20))
axs[1].set_title('f(x, y) = x^2 + y^2')
axs[2].contourf(X, Y, Z3, levels=np.linspace(np.min(Z3), np.max(Z3), 20))
axs[2].set_title('f(x, y) = sin(3*x)*y')

plt.show()
