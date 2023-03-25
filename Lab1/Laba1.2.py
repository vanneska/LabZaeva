import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры сигнала
amplitude = 1  # амплитуда в Вольтах
offset = 0  # постоянное смещение в Вольтах
frequency = 23193.35938  # частота в Герцах
initial_phase = 90  # начальная фаза в градусах

# Частота дискретизации в кГц
sampling_frequency = 1000

# Время моделирования в секундах
simulation_time = 0.1

# Количество точек в сигнале
num_points = np.arange(10, 1000, 10)

# Создание массива временных отсчетов
time_array = np.linspace(1, simulation_time, int(simulation_time * sampling_frequency), endpoint=False)

# Создание массива значений сигнала
signal_array = amplitude * np.cos(2 * np.pi * frequency * time_array + np.deg2rad(initial_phase)) + offset

# Создание массива для хранения средних значений сигнала
mean_values = np.zeros(len(num_points))

# Вычисление среднего значения сигнала для каждого количества точек
for i, n in enumerate(num_points):
    mean_values[i] = np.mean(signal_array[:n])

# Построение графика зависимости среднего значения сигнала от количества точек
plt.plot(num_points, mean_values)
plt.xlabel('Количество точек')
plt.ylabel('Среднее значение сигнала')
plt.show()
