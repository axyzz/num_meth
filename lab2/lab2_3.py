# f(x) = 0.9x^3 + 3.5x^2 - 0.3x - 4
# eps = 1e-13
# найти ВСЕ вещественные корни

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 0.9 * x**3 + 3.5 * x**2 - 0.3 * x - 4

def df(x):
    return 2.7 * x**2 + 7 * x - 0.3

def mpi(f, df, a, b, mi, ma, tol):
    q = 2 / (mi + ma)
    print('q = ', q)
    i = 0
    xk = (a + b) / 2
    while True:
        x_prev = xk
        i += 1
        xk = x_prev - q * f(x_prev)
        print('Итерация: ', i, ' x = ', xk, ' Апостериорная оценка порешности: ', (q / (1 - q)) * abs(xk - x_prev))
        if abs(xk - x_prev) < ((1 - abs(q)) / abs(q) * tol):
            return i, xk
        if i > 10000:
            print('Решение не найдено')
            exit()

x = np.linspace(-5, 2, 100)
plt.plot(x, f(x), label='f(x)')
plt.plot(x, df(x), label='df(x)')
plt.grid(True)
plt.legend()
plt.show()
print('Отрезки локализации: [-4, -3], [-2, -1], [0.5, 1.5]')

print('На отрезке [-4, -3] производная убывает; на отрезке [-2, -1] убывает, потом возрастает; на отрезке [0.5, 1.5] возрастает.')

eps = 1e-13
a = -4 
b = -3
x1 = mpi(f, df, a, b, df(b), df(a), eps)
a = -2 
b = -1
# в точке -35/27 минимум производной
x2 = mpi(f, df, a, b, df(-35/27), df(b), eps)
a = 0.5 
b = 1.5
x3 = mpi(f, df, a, b, df(a), df(b), eps)

print('x1 = ', x1[1], ' Итераций: ', x1[0])
print('x2 = ', x2[1], ' Итераций: ', x2[0])
print('x3 = ', x3[1], ' Итераций: ', x3[0])
