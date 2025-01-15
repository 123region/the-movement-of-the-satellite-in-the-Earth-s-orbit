import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Константы
G = 6.67408e-11  # Н
M = 5.97237e24   # кг
R = 6371000 + 200e3  # высота спутника в метрах
c = 1e-4

# Начальные условия
x0, y0 = R, 0  # начальная позиция
vx0, vy0 = 0, 8000  # начальная скорость

# Система уравнений
def equations(state, t):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    p = np.exp(1 - (R/r))
    ax = -G*M*x/r**3 - p*c*vx
    ay = -G*M*y/r**3 - p*c*vy
    return [vx, vy, ax, ay]

# Временной интервал и шаг
t = np.linspace(0, 86400, 100000)  # 24 часа с шагом 6 секунд

# Решение системы уравнений
state0 = [x0, y0, vx0, vy0] #задание начальных положений
solution = odeint(equations, state0, t)

# Вычисление высоты и скорости
height = solution[:, 1]
speed = np.sqrt(solution[:, 2]**2 + solution[:, 3]**2)

# Визуализация
plt.figure(figsize=(12, 6))
plt.plot(t/3600, height/1000, label='Высота')
plt.plot(t/3600, speed, label='Скорость')
plt.xlabel('Время (часы)')
plt.ylabel('Значения')
plt.legend()
plt.grid(True)
plt.title('Движение спутника')
plt.show()

print(f'Максимальная высота после 24 часов: {np.max(height)/1000:.2f} км')
print(f'Минимальная высота после 24 часов: {np.min(height)/1000:.2f} км')
print(f'Максимальная скорость после 24 часов: {np.max(speed):.2f} м/с')

# Дополнительные графики
plt.figure(figsize=(10, 6))
plt.plot(solution[:, 0], solution[:, 1])
plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.title('Траектория движения спутника')
plt.grid(True)
plt.show()
