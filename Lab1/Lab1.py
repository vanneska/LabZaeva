import math

import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры сигнала
amplitude = 1  # амплитуда, В
offset = 0  # постоянное смещение, В
frequency = 23193.35938  # частота, Гц
phase = 90  # начальная фаза, градусы

# Рассчитываем количество отсчетов для моделирования
sampling_frequency = 100000  # частота дискретизации, Гц
simulation_time = 0.1  # время моделирования, с
number_of_samples = int(sampling_frequency * simulation_time)
print(f'количество отсчетов для моделирования: {number_of_samples}')

# вычисление начальной фазы (в радианах)
phase_rad = np.deg2rad(phase)
print(f'начальная фаза: {phase_rad} рад')

# вычисление начальной фазы (в градусах)
phase_deg = math.degrees(phase_rad)
print(f'начальная фаза в градусах: {phase_deg} град')

# Создаем массив временных отсчетов
time = np.arange(number_of_samples) / sampling_frequency

# Рассчитываем массив значений сигнала
signal = amplitude * np.cos(2 * np.pi * frequency * time + phase_rad) + offset

# Сохраняем массив значений сигнала в файл
np.savetxt('signal.csv', signal, delimiter=',')

# Строим график зависимости сигнала от времени
plt.plot(time, signal)
plt.xlabel('Time, s')
plt.ylabel('Signal, V')
plt.title('Signal plot')
plt.show()

# Укрупняем фрагмент графика
plt.plot(time[::10], signal[::10])
plt.xlabel('Time, s')
plt.ylabel('Signal, V')
plt.title('Signal plot (Fragment)')
plt.show()

# Рассчитываем среднее значение сигнала
mean = np.mean(signal)
print(f'среднее значение сигнала: {mean}')
