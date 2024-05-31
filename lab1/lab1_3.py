# x0 = 0.2
# f(x) = 7 * sqrt(x + 2) / 2    изначальная функция
# N = 10, 20, ... 80 
# x = (4 * y**2 / 49) - 2   обратная функция
from math import sqrt

def f(x):
    return 7 * sqrt(x+2) / 2

def g(x):
    return (4 * x**2 / 49) - 2

N = 10
while N <= 80:
    x0 = 0.2
    s = x0
    for i in range(0, N):
        s = f(s)
    q = s
    for i in range(0, N):
        q = g(q)

    delta = abs(q - x0)
    print("N = ", N, "\nПогрешность: ", delta, ". Вычисленное приближенное значение: ", q)

    digits = 0

    while delta <= 10 ** (-digits):
        digits += 1
    print("Количество верных цифр: ", digits, "\n")
    N += 10
