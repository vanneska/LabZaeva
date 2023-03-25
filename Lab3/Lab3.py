import numpy as np
import matplotlib.pyplot as plt

# заданный сигнал
signal = np.sin(2 * np.pi * np.arange(1000) / 100)

# заданное соотношение SNR (в дБ)
snr_db = 1

# вычисляем амплитудный коэффициент шума
snr = 10**(snr_db/20.0)
noise_coef1 = 1 / snr
noise_coef2 = 1 / (snr * np.sqrt(np.mean(signal**2)))

# генерируем шум
noise1 = noise_coef1 * np.random.randn(signal.shape[0])
noise2 = noise_coef2 * np.random.randn(signal.shape[0])

# центрируем сигнал
signal -= np.mean(signal)

# генерируем смесь сигнала и шума
mix1 = signal + noise1
mix2 = signal + noise2

# выводим на графике фрагмент смеси
plt.plot(mix1[:100], label='SNR=1 dB, noise_coef=1/snr')
plt.plot(mix2[:100], label='SNR=1 dB, noise_coef=1/(snr*sqrt(signal^2))')
plt.legend()
plt.show()

# вычисляем косинус угла между вектором сигнала и вектором шума
cos1 = np.dot(signal, noise1) / (np.linalg.norm(signal) * np.linalg.norm(noise1))
cos2 = np.dot(signal, noise2) / (np.linalg.norm(signal) * np.linalg.norm(noise2))

print('cos(angle between signal and noise1) =', cos1)
print('cos(angle between signal and noise2) =', cos2)
