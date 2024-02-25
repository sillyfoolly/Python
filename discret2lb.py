def copy(m):
    new = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    ]
    for i in range(4):
        for j in range(4):
          new[i][j] = m[i][j]
    return new

#   Нахождение транзитивного замыкания первым способом
def FirstMethod(m):
    trn1 = copy(m)
    trn2 = copy(m)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                trn2[i][j] += trn1[i][k] * trn1[k][j]
                
    for i in range(4):
        for j in range(4):
            trn2[i][j] = trn2[i][j] + trn1[i][j]

    for i in range(4):
        for j in range(4):
            if trn2[i][j] > 1:
                trn2[i][j] = 1

    if trn2 == trn1:
        print('\nМатрица симетричного замыкания:')
        for i in range(4): print(trn2[i])
    else : FirstMethod(trn2)

#   Нахождение транзитивного замыкания вторым способом
def SecondMethod(m):
    pwr = 0
    trn = copy(m)
    for i in range(4):
        for j in range(4):
            if i != j and trn[i][j] == 1:
                for k in range(4):
                    trn[i][k] = trn[i][k] + trn[j][k]
    for i in range(4):
        for j in range(4):
            if trn[i][j] > 1:
                trn[i][j] = 1               
    print('\nМатрица симетричного замыкания:')
    for i in range(4): 
        print(trn[i])
        pwr += sum(trn[i])
    return pwr
pwr = 0
matrix = [
    [0, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
print('\nЗаданная матрица:')
for i in range(4): 
    print(matrix[i]), 
    pwr += sum(matrix[i])

#   Нахождение рефлексивного замыкания
ref = copy(matrix)
for i in range(4):
    for j in range(4):
        if i == j:
            ref[i][j] = 1
print('\nМатрица рефлексивного замыкания:')
for i in range(4): 
    print(ref[i])
    pwr += sum(ref[i])

#   Нахождение симметричного замыкания
sym = copy(matrix)
for i in range(4):
    for j in range(4):
        if sym[i][j] == 1:
            sym[j][i] = 1
print('\nМатрица симетричного замыкания:')
for i in range(4): 
    print(sym[i])
    pwr += sum(sym[i])

#   Вызов функций для нахождения транзитивного замыкания
FirstMethod(matrix)
pwr += SecondMethod(matrix)

print('\nСумма мощностей четырех матриц: ',pwr)