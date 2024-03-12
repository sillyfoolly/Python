def linear_congruent_method(x, n):
    mass = [x]

    for _ in range(n - 1):
        x = (48271 * x) % (pow(2, 31) - 1)
        mass.append(x)

    return mass

# def equal_spread(mass):
    interval = [0] * 10
    x2 = 0

    for i in mass:
        interval[int(i*10)] += 1

    for i in range(10):
        x2 = x2 + pow(interval[0] - 20, 2) / 20

    # for i in interval: print(i)

    if x2 < 16.9: print(f'\nB) Последовательность равномерно распределенна ({x2:.1f} < 16.9)')

    else: print(f'\nB) Последовательность распределенна не равномерно  ({x2:.1f} > 16.9)')

    print(interval)


def main():

    print('\n\n---------- Линейный конгруэнтный метод ----------')
    mass1 = linear_congruent_method(1080762024, 20)
    # equal_spread(mass2)
    print(mass1)

if __name__ == "__main__":
    main()