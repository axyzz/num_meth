import numpy as np
import matplotlib.pyplot as plt

# параметры
beta = 0.4
gamma_values = np.linspace(0.1, 1.1, 11)
y0 = 0.2
T = 20
h = 0.1
time_steps = int(T / h)

# метод рунге-кутты 3 порядка
def rk3(y0, p, h, steps):
    y = np.zeros(steps + 1)
    y[0] = y0
    for i in range(steps):
        ti = i * h
        yi = y[i]
        k1 = h * (yi * (1 - yi) - p * yi)
        k2 = h * ((yi + 0.5 * k1) * (1 - (yi + 0.5 * k1)) - p * (yi + 0.5 * k1))
        k3 = h * ((yi + 0.75 * k2) * (1 - (yi + 0.75 * k2)) - p * (yi + 0.75 * k2))
        y[i + 1] = yi + (1 / 9) * (2 * k1 + 3 * k2 + 4 * k3)
    return y

# вычисление интеграла центральными прямоугольниками с уточнением по Рунге
def integr(yh, yq, h):
    I_h = 0
    I_h2 = 0
    for i in range(1, len(yh), 2):
        I_h += yh[i]
    I_h *= h 
    for i in range(1, len(yq), 2):
        I_h2 += yq[i]
    I_h2 *= h / 2
    I_runge = I_h + (I_h - I_h2) / 3
    
    return I_runge

# вычисление результатов и построение графиков
# решение при минимальном gamma
p = gamma_values[0] / beta
y = rk3(y0, p, h, time_steps)
t = np.arange(0, T + h, h)
plt.plot(t, y, label=f'γ={gamma_values[0]:.2f}')
plt.show()

# решение при всех gamma, вычисление интегралов и погрешности по правилу Рунге
V_values = []
tol = 0

t = np.arange(0, T + h, h)
for gamma in gamma_values:
    p = gamma / beta
    y2 = rk3(y0, p, h*2, time_steps // 2)
    y = rk3(y0, p, h, time_steps)
    for i in range(0, time_steps // 2 + 1):
        if abs(y2[i] - y[i*2]) > tol:
            tol = abs(y2[i] - y[i*2])
    yh = rk3(y0, p, h / 2, time_steps * 2)
    yq = rk3(y0, p, h / 4, time_steps * 4)
    V = gamma * integr(yh, yq, h)
    V_values.append(V)
    
    plt.plot(t, y, label=f'γ={gamma:.2f}')
tol = tol / 7

# вычисление gamma при котором V максимально
vmax = 0
gmax = 0
gmax_values = np.arange(0.1, 0.31, 0.01)
for gamma in gmax_values:
    p = gamma / beta
    yh = rk3(y0, p, h/2, time_steps*2)
    yq = rk3(y0, p, h/4, time_steps*4)
    V = gamma * integr(yh, yq, h)
    print(f'gamma = {gamma:.2f} V = {V}')
    if V > vmax:
        vmax = V
        gmax = gamma

# вывод результатов
plt.xlabel('tau')
plt.ylabel('Биомасса')
plt.legend()
plt.title('Изменение биомассы от времени в зависимости от параметра гамма(Интенсивность промысла)')
plt.grid(True)
plt.show()

print(f'Погрешность по правилу Рунге при вычислении решения задачи Коши: {tol}')
print(f'Интенсивность промысла при которой количество выловленной выбы максимально: {gmax:.2f}')

plt.plot(gamma_values, V_values, marker='o')
plt.xlabel('')
plt.ylabel('Количество пойманной рыбы')
plt.title('Количество пойманной рыбы за время T в зависимости от интенсивности промысла')
plt.grid(True)
plt.show()
