from math import *

def linear_congruent_method(x, n):
    mass = [x/(pow(2, 31))]

    for _ in range(n - 1):
        x = (48271 * x) % (pow(2, 31) - 1)
        mass.append(x/(pow(2, 31)))

    return mass

def task1(mass):
    newmass = [-4.5 + (8.5 + 4.5) *  i for i in mass] 
    interval = [0] * 10
    x2 = 0

    for i in range(10):
        for j in newmass:
            if (-4.5 + i * (8.5 + 4.5)/10) < j < (-4.5 + (i + 1) * (8.5 + 4.5)/10):
                interval[i] += 1

    for i in range(10):
        x2 += pow(interval[i] - 2, 2) / 2

    print(f'\nПолученные числа на отрезке [-4.5, 8.5]:\n{newmass}')

    if x2 < 16.9: print(f'\nПоследовательность равномерно распределенна ({x2:.1f} < 16.9)')

    else: print(f'\nПоследовательность распределенна не равномерно  ({x2:.1f} > 16.9)')

    print(interval)

def task2(mass):
    # Первый тест
    newmass = [-4260 * log(i) for i in mass]
    c = 0

    for i in newmass:
        if i < 5000:
            c += 1 
    mid = c
    
    print(f'\n1-ый тест: время работ\n{newmass}\nИз них потребуют перезагрузку {c}')
    
    # Второй тест
    newmass = [-4260 * log(i) for i in mass]
    c = 0

    for i in newmass:
        if i < 5000:
            c += 1 
    mid += c

    print(f'\n2-ой тест: время работ\n{newmass}\nИз них потребуют перезагрузку {c}')

    # Третий тест
    newmass = [-4260 * log(i) for i in mass]
    c = 0

    for i in newmass:
        if i < 5000:
            c += 1 
    mid += c
    
    print(f'\n3-ий тест: время работ\n{newmass}\nИз них потребуют перезагрузку {c}')
    print(f'\nВ среднем потребуют перезагрузку: {mid/3}')

def task3(mass):
    newmass = []
    c = 0

    for i in range(0, len(mass)-1, 2):
        newmass.append((8 + 0.8 * (pow((-2 * log(mass[i])), 1/2) * cos(2*pi*mass[i+1]))))
        newmass.append((8 + 0.8 * (pow((-2 * log(mass[i])), 1/2) * sin(2*pi*mass[i+1]))))

    for i in newmass:
        if (6.4 < i < 9.6) == False:
            c += 1

    print(f'\nСредний диаметр = 8 мм\nсреднее квадратичное отклонение = 0.8')
    print(newmass, c)
    
def task4(mass):
    newmass = []
    c = []
    x = 0; n = 0; 

    for i in mass:
        x += i
        n += 1
        if n == 12:
            newmass.append(100 + 10 * (x - 6))
            x = 0
            n = 0

    for i in newmass:
        if i > 120:
            c.append(i)

    print(f'\nОбращений не менее 120 - {len(c)} раз: {c}')


def main():

    # mass1 = linear_congruent_method(1080762024, 20)
    # task1(mass1)
    # task2(mass1)
    # mass2 = linear_congruent_method(1080762024, 100)
    # task3(mass2) 
    mass3 = linear_congruent_method(1080762024, 4380)
    task4(mass3)

if __name__ == "__main__":
    main()