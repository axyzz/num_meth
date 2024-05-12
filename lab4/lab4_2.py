#  вариант 16
#  eps  = 1e-6
#  y`   = y + 2ln(t) / t - ln(t) ^ 2 
#  y(1) = 0
#  метод Рунге-Кутты 3-го порядка (вариант 3)
#  t = [1, 2]
import numpy as np
eps = 1e-6


def f(t,y):
    return y + 2*np.log(t) / t - np.log(t)**2


def rk3(h, fun, y0):
    t = np.linspace(1, 2, int(1/h) + 1)
    res = [fun(t[0], y0)]
    for i in range(len(t)-1):
        k1 = h * f(t[i], res[i])
        k2 = h * f(t[i] + h/2, res[i] + k1/2)
        k3 = h * f(t[i] + h, res[i] - k1 + 2*k2)
        res.append(res[i] + (k1 + 4*k2 + k3)/6)
    return res


def euler(h, fun, y0):
    t = np.linspace(1, 2, int(1/h) + 1)
    res = [fun(t[0], y0)]
    for i in range(len(t)-1):
        res.append(res[i] + h * f(t[i], res[i]))
    return res


tole = 1
h = 0.2
while tole > eps:
    res = euler(h, f, 1)
    resh = euler(h/2, f, 1)
    tols = []
    for i in range(1, len(res)):
        tols.append(abs(res[i]-resh[i*2]))
    tole = max(tols)
    h /= 2
print('Полученный шаг для явного метода Эйлера: ', h*2,'\nПогрешность: ', tole)

tole = 1
h = 0.2
while tole > eps:
    res = rk3(h, f, 1)
    resh = rk3(h/2, f, 1)
    tols = []
    for i in range(1, len(res)):
        tols.append(abs(res[i]-resh[i*2])/7)
    tole = max(tols)
    h /= 2
print('Полученный шаг для явного метода Рунге-Кутты 3 порядка: ', h*2,'\nПогрешность: ', tole)


