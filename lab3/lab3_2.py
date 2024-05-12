from math import e

a = 0
b = 3


def f(x):
    return e**(-x) * (x**2 - x)


def simps(a, b, h):
    int_sum = f(a) + f(b)
    for i in range(1, int((b - a) / h), 2):
        int_sum += 4 * f(a + i * h)
    for i in range(2, int((b - a) / h - 1), 2):
        int_sum += 2 * f(a + i * h)
    int_sum *= h/3
    return int_sum




I = (-13/e**3) - (-1)
print(I)
# вычисление с 8 шагами
for k in range(1, 9):
    h = (b - a) / 10**k
    integral = simps(a, b, h)
    print( 'Интеграл: ', integral, ' | delta I: ', abs(I - integral))

# вычисление с заданной точностью
eps = 4e-12
h = 0.3
prevv = simps(a, b, h)
nextt = simps(a, b, h/2)
while abs(nextt - prevv) / 15 > eps:
    h = h/2
    prevv = nextt
    nextt = simps(a, b, h/2)
print( 'Интеграл: ', simps(a, b, h/2), ' | delta I: ', abs(I - simps(a, b, h/2)), ' | h: ', h/2)
