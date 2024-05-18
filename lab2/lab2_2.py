from scipy.optimize import root
from numpy import sin, arcsin, linspace
import matplotlib.pyplot as plt 
# eps = 1e-10
# f(x) = (sinx)^2 + 5/6 * sinx + 1/6
# g(x) = (sinx)^2 + 2/3 * sinx + 1/9
# [a,b] = [-1,0]

def f(x):
    return sin(x)**2 + (5 * sin(x)) / 6 + 1 / 6

def g(x):
    return sin(x)**2 + (2 * sin(x)) / 3 + 1 / 9

def bisection(f, a, b, eps):
    c = 0
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

# f(x)
print('\n------ Решение f(x) = 0 ------\n')
print('Аналитическое решение.\nx1 = arcsin(-1/3) = ', arcsin(-1/3), '\nx2 = arcsin(-1/2) = ', arcsin(-1/2))
print('\nДва отрезка локализации. [-0.6, -0.5] и [-0.4, -0.3]')

a1 = -0.6
b1 = -0.5
a2 = -0.4
b2 = -0.3
eps = 1e-10

print('Решение методом бисекции.\nx1 = ', bisection(f, a1, b2, eps), '\nx2 = ', bisection(f, a2, b2, eps))
print('\nРешение при помощи scipy.optimize.root')
print('x1 = ', root(f, -0.5, tol=eps).x[0])
print('x2 = ', root(f, -0.3, tol=eps).x[0])
print('\n')

# g(x)
print('------ Решение g(x) = 0 ------\n')
print('Аналитическое решение.\nx = arcsin(-1/3) = ', arcsin(-1/3))
print('\nОдин отрезок локализации. [-0.4, -0.3]')
print('Решение методом бисекции. \nx = ', bisection(g, -0.4, -0.3, eps))
print('\nРешение при помощи scipy.optimize.root')
print('x = ', root(g, -0.3, tol=eps).x[0])
x = linspace(-1, 0, 100)
plt.plot(x, f(x), label='f(x)')
plt.grid(True)
plt.legend()
plt.show()

x = linspace(-1, 0, 100)
plt.plot(x, g(x), label='g(x)')
plt.grid(True)
plt.legend()
plt.show()
