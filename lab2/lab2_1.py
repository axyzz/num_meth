 f(x) = 0.9x^3 + 3.5x^2 - 0.3x - 4 = 0
# eps = 10^-6

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton

# заданная функция
def func(x):
    return 0.9 * x**3 + 3.5 * x**2 - 0.3 * x - 4

# производная 
def derive(x):
    return 2.7 * x**2 + 7 * x - 0.3

x = np.linspace(-7, 7, 100)
y = func(x)

# построение графика
plt.plot(x,y)
plt.grid(True)

# решение двумя методами
x0 = 1
root1 = newton(func, x0, tol = 1e-6)
root2 = newton(func, x0, tol = 1e-6, fprime=derive, full_output=True)
print('Корень полученный методом секущих: ', root1)
print('Корень полученный методом ньютона: ', root2)

plt.show()
