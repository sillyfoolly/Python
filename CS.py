import math
import random

# 1. Метод середины квадратов
def mid_squares_method(x, n):
    mass = [] 
    mass.append(x)
    for i in range(n - 1):
        x = x * x * 100000
        x = (x - (x // 1)) * 10000000000 // 1 / 10000000000 
        mass.append(x) 
    return mass

# 2. Проверить полученную последовательность на случайность
def random_test(mass):
    number = [0] * 10
    for i in mass:
        x = i * 10000000
        x = (x - (x // 1)) * 10 // 1
        x = int(x) 
        number[x] += 1
    x2 = pow(number[0] - 20, 2) / 20 + pow(number[1] - 20, 2) / 20 + pow(number[2] - 20, 2) / 20 + pow(number[3] - 20, 2) / 20 + pow(number[4] - 20, 2) / 20 + pow(number[5] - 20, 2) / 20 + pow(number[6] - 20, 2) / 20 + pow(number[7] - 20, 2) / 20 + pow(number[8] - 20, 2) / 20 + pow(number[9] - 20, 2) / 20
    if x2 < 16.9:
        print(f"\nA) Последовательность случайна ({x2:.1f} < 16.9)")
    else: print(f"\nA) Последовательность не случайна ({x2:.1f} > 16.9)")

# 3. Проверить гипотезу о равномерном распределении
def equal_spread(mass):
    interval = [0] * 10
    for i in mass:
        interval[int(i*10)] += 1
    x22 = pow(interval[0] - 20, 2) / 20 + pow(interval[1] - 20, 2) / 20 + pow(interval[2] - 20, 2) / 20 + pow(interval[3] - 20, 2) / 20 + pow(interval[4] - 20, 2) / 20 + pow(interval[5] - 20, 2) / 20 + pow(interval[6] - 20, 2) / 20 + pow(interval[7] - 20, 2) / 20 + pow(interval[8] - 20, 2) / 20 + pow(interval[9] - 20, 2) / 20
    if x22 < 16.9:
        print(f'\nB) Последовательность равномерно распределенна ({x22:.1f} < 16.9)')
    else: print(f'\nB) Последовательность распределенна не равномерно  ({x22:.1f} > 16.9)')

# 4. Коэффициент автокорреляции 1-го порядка
def coefficient(mass):
    medium, up, down = 0, 0, 0
    for i in mass:
        medium += i
    medium = medium/len(mass)
    for i in range(2, len(mass)): 
        up += (mass[i] - medium) * (mass[i-1] - medium)
        down += pow(mass[i] - medium, 2)
    r = up/down
    t = abs(r * math.sqrt((len(mass)-2)/(1-r*r)))
    if t < 1.9702:
        print (f'\nC) Последовательность статистически независима (t = {t:.4f} < 1.9702)')
    else: (f'\nC) Последовательность не является статистически независимой (t = {t:.4f} > 1.9702)')

# 5. Наличие/отсутсвие периода в последовательности
def period(mass):
    c = 0
    for i in mass:
        if mass.count(i) > 1:
            c = 1
    if c == 1:
        print(f'\nD) Числа повторяются, период присутствует')
    else: print(f'\nD) Все числа разные, период отсутствует')

# 6. Линейный конгруэнтный метод
def linear_congruent_method(x, n):
    mass = []
    mass.append(x/(pow(2,31)))
    for i in range(n - 1):
        x = (48271 * x) % (pow(2, 31)-1)
        mass.append(x/(pow(2,31)))
    return mass

# 7. Метод Фибоначчи с запаздыванием
def fibonacci_method_with_a_delay(n):
    mass = linear_congruent_method(1080762024, 17)
    for i in range (17, n):
        mass.append((mass[i - 5] + mass[i - 17]) % (pow(2, 0)))
    return mass

print('\n---------- Метод середины квадратов ----------')
mass1 = mid_squares_method(0.1080762024, 200)
random_test(mass1)
equal_spread(mass1)
coefficient(mass1)
period(mass1)

print('\n\n---------- Линейный конгруэнтный метод ----------')
mass2 = linear_congruent_method(1080762024, 200)
random_test(mass2)
equal_spread(mass2)
coefficient(mass2)
period(mass2)

print('\n\n---------- Метод Фибоначчи с запаздыванием ----------')
mass3 = fibonacci_method_with_a_delay(200)
random_test(mass3)
equal_spread(mass3)
coefficient(mass3)
period(mass3)

print('\n\n---------- Модуль random ----------')
mass4 =[random.random() for i in range(200)]
random_test(mass4)
equal_spread(mass4)
coefficient(mass4)
period(mass4)