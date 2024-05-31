# x' = (a-x)*b*x/a - g*x
# y' = y(1-y) - p*y
# y = x/a
# p = g/b
# y(0) = 0.2
# b = 0.4
# g = [0.1, 1.1]
# t = [0, 50]; h = 0.1
# метод РК 3 порядка (вариант 3)
# интеграл центральные прямоугольники с уточнением по Рунге
import numpy as np
import matplotlib.pyplot as plt

beta = 0.4
gamma_values = np.linspace(0.1, 1.1, 11)
y0 = 0.2
T = 50

def f(p, y):
    return y * (1 - y) - p * y


def rk3(h, fun, y0, p):
    t = np.linspace(0, 50, int(50/h) + 1)
    res = [fun(p, y0)]
    for i in range(len(t)-1):
        k1 = h * f(p, res[i])
        k2 = h * f(p, res[i] + k1/2)
        k3 = h * f(p, res[i] - k1 + 2*k2)
        res.append(res[i] + (k1 + 4*k2 +k3) / 6)
    return res


def integr(y, h):
    result = 0
    for i in range(1, len(y)):
        result += (y[i] + y[i-1]) / 2
    result *= h
    return result


v_values = []
y_values = []
h = 0.1
t = np.linspace(0, T, int(T/h) + 1)
for gamma in gamma_values:
    p = gamma / beta
    y = rk3(h, f, y0, p)
    y_values.append(y)
    v = gamma * integr(y, h)
    v_values.append(v)


plt.grid(True)
for i in range(len(y_values)):
    plt.plot(t, y_values[i], label = f'Gamma = {0.1*(i+1)}')
plt.legend()
plt.show()
