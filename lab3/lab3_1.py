from math import e

D = -1.0
I = (-13/e**3) - (-1)

def f(x):
    return e**(-x) * (x**2 - x)

b = 3
a = 0
for k in range(1, 16):
    h = (b - a) / (10**k)
    # вычисление интеграла
    int_sum = (f(a) + f(b)) / 2
    for i in range(1, 10**k):
        int_sum += f(a + i*h)
    int_sum *= h
    # вычисление производной
    dx = (f(a) - f(a-h)) / h
    print('k = ', k, ' | Интеграл: ', int_sum, ' | delta I: ', abs(I - int_sum))
    print( 'Производная: ', dx, ' | delta D: ', abs(D - dx))
