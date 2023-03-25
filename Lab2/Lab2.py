import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# генерируем массив отсчетов шума
n = 10000  # количество отсчетов
mu = 0  # математическое ожидание
sigma = 1  # стандартное отклонение
data = np.random.normal(mu, sigma, n)

# сохраняем массив в файл csv
df = pd.DataFrame(data, columns=['Отсчеты'])
df.to_csv('10_noice.csv', index=False)

# выводим на графике фрагмент выборки
plt.plot(data[:int(0.1*n)])  # 5-10% отсчетов
plt.xlabel('Отсчеты')
plt.ylabel('Значение')
plt.title('Фрагмент выборки шума')
plt.show()

# определяем среднее и дисперсию по выборке
mean = np.mean(data)
variance = np.var(data)
print('Среднее:', mean)
print('Дисперсия:', variance)

# рассчитываем теоретические значения математического ожидания и дисперсии
theoretical_mean = mu
theoretical_variance = sigma**2
print('Теоретическое среднее:', theoretical_mean)
print('Теоретическая дисперсия:', theoretical_variance)

# Проверка на равномерное распределение
tolerance = 0.1  # допустимая погрешность
is_uniform = abs(theoretical_mean - mean) < tolerance and abs(theoretical_variance - variance) < tolerance
if is_uniform:
    print('Массив отсчетов шума имеет равномерное распределение')
else:
    print('Массив отсчетов шума не имеет равномерного распределения')


# строим гистограмму всех шумовых отсчетов
plt.hist(data, bins=50)
plt.xlabel('Значение')
plt.ylabel('Отсчёты')
plt.title('Гистограмма всех шумовых отсчетов')
plt.show()