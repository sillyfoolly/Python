def linear_congruent_method(x, n):
    mass = [x/(pow(2, 31))]

    for _ in range(n - 1):
        x = (48271 * x) % (pow(2, 31) - 1)
        mass.append(x/(pow(2, 31)))

    return mass

def equal_spread(mass):
    newmass = [] 
    interval = [0] * 10
    x2 = 0

    for i in mass:
        newmass.append(-4.5 + (8.5 + 4.5) *  i)

    for i in range(10):
        for j in newmass:
            if (-4.5 + i * (8.5 + 4.5)/10) < j < (-4.5 + (i + 1) * (8.5 + 4.5)/10):
                interval[i] += 1

    for i in range(10):
        x2 = x2 + pow(interval[i] - 2, 2) / 2

    if x2 < 16.9: print(f'\nB) Последовательность равномерно распределенна ({x2:.1f} < 16.9)')

    else: print(f'\nB) Последовательность распределенна не равномерно  ({x2:.1f} > 16.9)')

    print(interval)


def main():

    print('\n\n---------- Линейный конгруэнтный метод ----------')
    mass1 = linear_congruent_method(1080762024, 20)
    equal_spread(mass1)

if __name__ == "__main__":
    main()