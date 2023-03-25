import math

# заданные параметры
amplitude = 1  # амплитуда в В
offset = 0  # постоянное смещение в В
frequency = 23193.35938  # частота в Гц
initial_phase = 90  # начальная фаза в градусах
sampling_frequency = 1000  # частота дискретизации в кГц
duration = 100  # время моделирования в мс

# перевод начальной фазы в радианы
initial_phase_rad = math.radians(initial_phase)

# перевод частоты и частоты дискретизации в радианы/мс
omega = 2 * math.pi * frequency / 1000
sampling_omega = 2 * math.pi * sampling_frequency

# вычисление значения сигнала на 5 мс
time = 5  # время в мс
samples = int(sampling_frequency * duration)  # общее число отсчетов
sample_time = 1 / sampling_frequency  # длительность одного отсчета в мс

sample_index = int(time / sample_time)  # индекс отсчета для 5 мс
cosine = amplitude * math.cos(omega * time + initial_phase_rad)  # значение косинуса на 5 мс
signal = offset + cosine  # значение сигнала на 5 мс

print(f"Значение сигнала на {time} мс: {signal} В")