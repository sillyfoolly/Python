import matplotlib.pyplot as plt
import sys

sys.set_int_max_str_digits(0)
letters = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}
colours = [
    '#2ee8bb',
    '#77ab56',
    '#fffa86',
    '#1f6357',
    '#ffb07c',
    '#61de2a',
    '#0203e2',
    '#990f4b',
    '#010fcc'
]

def Proth_List(k, n):
    a = 0
    l = []
    for i in range(n):
        a = k * pow(2, i) + 1
        l.append(a)
    return l

list_of_nums = Proth_List(3, 10000)

for n in list_of_nums:
    first_digit = str(n)[0]
    letters[first_digit] += 1
print(letters)
x = list(letters.keys())
y = [round(val / 10000, 4) for val in letters.values()]

plt.title("Benford's Law distribution")
plt.xlabel('First digit')
plt.ylabel('Frequency')
plt.ylim([0, 0.4])
bars = plt.bar(x, y, color = colours)
plt.show()

for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height}',
    xy = (bar.get_x() + bar.get_width() / 2, height),
    xytext = (0, 3),
    textcoords = 'offset points',
    ha = 'center',
    va = 'bottom'
    )
