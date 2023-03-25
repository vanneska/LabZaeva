import numpy as np
import matplotlib.pyplot as plt

# Генерация сигнала
signal_amplitude = 1
signal_length = 10000
signal = np.random.normal(0, signal_amplitude, signal_length)
signal -= np.mean(signal)  # Центрирование сигнала

# Генерация шума
SNR = 1  # Соотношение сигнал/шум в дБ
noise_amplitude = signal_amplitude / np.sqrt(10**(SNR/10))  # Амплитуда шума
noise1 = np.random.normal(0, noise_amplitude, signal_length)
noise2 = np.random.normal(0, noise_amplitude/signal_amplitude, signal_length)

# Формирование смеси
mixed_signal1 = signal + noise1
mixed_signal2 = signal + noise2

# Вывод на график фрагмента смеси
start = int(signal_length * 0.05)
end = int(signal_length * 0.1)
fig, axs = plt.subplots(2)
axs[0].plot(mixed_signal1[start:end])
axs[0].set_title(f"Mixed signal with SNR = {SNR} dB (noise amplitude = {noise_amplitude:.3f})")
axs[1].plot(mixed_signal2[start:end])
axs[1].set_title(f"Mixed signal with SNR = {SNR} dB (noise amplitude = {noise_amplitude/signal_amplitude:.3f})")
plt.show()

# Вычисление косинуса угла между векторами сигнала и шума
cos_angle1 = np.dot(signal, noise1) / (np.linalg.norm(signal) * np.linalg.norm(noise1))
cos_angle2 = np.dot(signal, noise2) / (np.linalg.norm(signal) * np.linalg.norm(noise2))
print(f"Cosine angle between signal and noise1: {cos_angle1:.3f}")
print(f"Cosine angle between signal and noise2: {cos_angle2:.3f}")

