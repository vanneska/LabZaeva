import numpy as np
import csv

# установка параметров распределения
low = 0
high = 1

# генерация массива отсчетов шума
samples = np.random.uniform(low, high, 10000)

# сохранение массива в файл csv
with open('samples.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Отсчеты шума'])
    writer.writerows(zip(samples))

# вывод на графике фрагмента
import matplotlib.pyplot as plt

plt.plot(samples[:500])
plt.title('Фрагмент массива отсчетов шума')
plt.xlabel('Отсчеты')
plt.ylabel('Значения')
plt.show()

# определение среднего и дисперсии по выборке
mean = np.mean(samples)
variance = np.var(samples)
print('Среднее:', mean)
print('Дисперсия:', variance)

# расчет теоретических значений математического ожидания и дисперсии
theoretical_mean = (low + high) / 2
theoretical_variance = ((high - low) ** 2) / 12
print('Теоретическое среднее:', theoretical_mean)
print('Теоретическая дисперсия:', theoretical_variance)

# построение гистограммы всех шумовых отсчетов
plt.hist(samples, bins=50, density=True, alpha=0.5)
plt.title('Гистограмма всех шумовых отсчетов')
plt.xlabel('Отсчеты')
plt.ylabel('Плотность вероятности')
plt.show()
