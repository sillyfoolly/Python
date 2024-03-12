import math
import random

# 1. Метод середины квадратов
def mid_squares_method(x, n):
    mass = [] 
    mass.append(x)

    for _ in range(n - 1):
        x = float('0.' + f'{(x * x):.20f}'[7:17])
        mass.append(x) 

    return mass

# 2. Проверить полученную последовательность на случайность
def random_test(mass):
    number = [0] * 10
    x2 = 0

    for i in mass:
        x = int(str(i)[9]) 
        number[x] += 1

    for i in range(10):
        x2 = x2 + pow(number[i] - 20, 2) / 20

    if x2 < 16.9: print(f"\nA) Последовательность случайна ({x2:.1f} < 16.9)")

    else: print(f"\nA) Последовательность не случайна ({x2:.1f} > 16.9)")

# 3. Проверить гипотезу о равномерном распределении
def equal_spread(mass):
    interval = [0] * 10
    x2 = 0

    for i in mass:
        interval[int(i*10)] += 1

    for i in range(10):
        x2 = x2 + pow(interval[i] - 20, 2) / 20

    # for i in interval: print(i)

    if x2 < 16.9: print(f'\nB) Последовательность равномерно распределенна ({x2:.1f} < 16.9)')

    else: print(f'\nB) Последовательность распределенна не равномерно  ({x2:.1f} > 16.9)')

    print(f'{interval}')

# 4. Коэффициент автокорреляции 1-го порядка
def coefficient(mass):
    up, down = 0, 0

    medium = sum(mass) / len(mass)

    for i in range(2, len(mass)): 
        up += (mass[i] - medium) * (mass[i-1] - medium)
        down += pow(mass[i] - medium, 2)

    r = up/down
    t = abs(r * math.sqrt((len(mass)-2)/(1-r*r)))
    tc = abs((200-2) * math.sqrt((0.05-2)/(1-(200-2)*(200-2))))

    if t < tc: print (f'\nC) Последовательность статистически независима (r = {r:.4f}, t = {t:.4f} < {tc:.4f})')

    else: print (f'\nC) Последовательность не является статистически независимой (r = {r:.4f}, t = {t:.4f} > {tc:.4f})')

# 5. Наличие/отсутсвие периода в    
def period(mass):
    c = False

    for i in mass:
        if mass.count(i) > 1:
            c = True
    
    if c: print(f'\nD) Числа повторяются, период присутствует')

    else: print(f'\nD) Все числа разные, период отсутствует')

# 6. Линейный конгруэнтный метод
def linear_congruent_method(x, n):
    mass = []
    mass.append(x/(pow(2,31)))

    for _ in range(n - 1):
        x = (48271 * x) % (pow(2, 31)-1)
        mass.append(x/(pow(2,31)))

    return mass

# 7. Метод Фибоначчи с запаздыванием
def fibonacci_method_with_a_delay(n):
    mass = linear_congruent_method(1080762024, 17)

    for i in range (17, n):
        if mass[i - 5] < mass[i - 17]:
            mass.append((mass[i - 5] - mass[i - 17]) + 1)
        else: mass.append((mass[i - 5] - mass[i - 17]))

    return mass


def main():
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


if __name__ == "__main__":
    main()