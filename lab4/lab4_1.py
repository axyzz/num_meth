#  y(t)    = ln(t) ^ 2
#  y'(t)   = 2*ln(t) / t
#  s(t)    = 2*ln(t) / t - ln(t) ^ 2
#  f(t, y) = y + 2*ln(t) / t - ln(t) ^ 2
#  y` = y + 2*ln(t) / t - ln(t) ^ 2

from scipy.integrate import solve_ivp
from  numpy import log, ndarray, linspace
import matplotlib.pyplot as plt

def f(t,y):
    return y + 2 * log(t) / t - log(t)**2


def solve(x):
    return log(x)**2


res1 = solve_ivp(f, t_span=[1, 2], y0=[0], method='RK45', atol=1e-10, rtol=1e-10)


t = linspace(1, 2, 11)
res2 = solve_ivp(f, t_span=[1, 2], y0=[0], method='RK45', t_eval=t, atol=1e-10, rtol=1e-10) 

print('t: ', res2['t'])
res22 = res2['y'][0]
print('y: ', res22)

# погрешность
r = ndarray(11)
for i in range(11):
    r[i] = abs(res22[i]-solve(t[i]))
print('Погрешность: ', max(r))

# графики
plt.grid(True)
plt.plot(res1['t'], res1['y'][0], color='red', label='PK4', ls='', marker='.', markersize=6)
tt = linspace(1, 2, 100)
plt.plot(tt, solve(tt), color='black', label='точное')
plt.legend()
plt.show()
