import math

    # 1. Метод середины квадратов
def mid_squares_method(xo1, n):
    mass = [] 
    mass.append(xo1)
    for i in range(n - 1):
        xo1 = xo1 * xo1 * 100000
        xo1 = (xo1 - (xo1 // 1)) * 10000000000 // 1 / 10000000000 
        mass.append(xo1) 
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
        print(f"\nA) Последовательность случайна ({x2} < 16.9)")
    else: print(f"\nA) Последовательность не случайна ({x2} > 16.9)")

# 3. Проверить гипотезу о равномерном распределении
def equal_spread(mass):
    interval = [0] * 10
    for i in mass:
        interval[int(i*10)] += 1
    x22 = pow(interval[0] - 20, 2) / 20 + pow(interval[1] - 20, 2) / 20 + pow(interval[2] - 20, 2) / 20 + pow(interval[3] - 20, 2) / 20 + pow(interval[4] - 20, 2) / 20 + pow(interval[5] - 20, 2) / 20 + pow(interval[6] - 20, 2) / 20 + pow(interval[7] - 20, 2) / 20 + pow(interval[8] - 20, 2) / 20 + pow(interval[9] - 20, 2) / 20
    if x22 < 16.9:
        print(f'\nB) Последовательность равномерно распределенна ({x22} < 16.9)')
    else: print(f'\nB) Последовательность распределенна не равномерно  ({x22} > 16.9)')

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
        print (f'\nC) Последовательность статистически независима (t = {t} < 1.9702)')
    else: (f'\nC) Последовательность не является статистически независимой (t = {t} > 1.9702)')

# 5. Наличие/отсутсвие периода в последовательности
def period(mass):
    c = 0
    for i in mass:
        if mass.count(i) > 1:
            c = 1
    if c == 1:
        print(f'\nD) Числа повторяются, период присутствует')
    else: print(f'\nD) Все числа разные, период отсутствует')



mass = mid_squares_method(0.1080762024, 200)
random_test(mass)
equal_spread(mass)
coefficient(mass)
period(mass)



















# mass2 = [1, 2, 3, 4, 4, 4, 5, 5]
# for i in mass2:
#     if mass2.count(i) > 1:
#         print(f'\nD) Числа повторяются, период присутствует')
#         break
#     print(f'\nD) Все числа разные, период отсутствует')