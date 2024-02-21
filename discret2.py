def copy(m):
    return [row[:] for row in m]

def printmat(m):
    print(*list(map(lambda col: [int(i != 0) for i in col], m)), sep='\n')

def flat(m):
    return sum(m, [])

def power(m):
    return sum(e != 0 for e in flat(m))

def equal(a, b):
    return all(a == b for a, b in zip(flat(a), flat(b)))

def to_bool(m):
    rows, cols = len(m), len(m[0])
    b = [[0 for row in range(rows)] for col in range(cols)]
    for row in range(rows):
        for col in range(cols):
            b[row][col] = m[row][col] != 0
    return b

def matmul(a, b):
    rows_a = len(a)
    rows_b, cols_b = len(b), len(b[0])
    c = [[0 for row in range(rows_a)] for col in range(cols_b)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(rows_b):
                c[i][j] += a[i][k]*b[k][j]
    return c

def matadd(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    c = [[0 for row in range(rows_a)] for col in range(cols_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            c[i][j] = a[i][j] + b[i][j]
    return c

def transpose(m):
    rows, cols = len(m), len(m[0])
    t = [[0 for j in range(rows)] for i in range(cols)]
    t = [[m[j][i] for j in range(cols)] for i in range(rows)]
    return t

matrix = [
 [0, 1, 1, 1],
 [1, 1, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
]
printmat(matrix)
print()

ref = copy(matrix)
for i in range(len(ref)):
    for j in range(len(ref[0])):
        if i == j:
            ref[i][j] = 1
printmat(ref)
print()

sym = to_bool(matadd(matrix, transpose(matrix)))
printmat(sym)
print()

tmp = copy(matrix)
pwr = power(matrix)
while True:
    trn = matadd(matmul(tmp, tmp), tmp)
    pwr += power(trn)
    if equal(to_bool(tmp), to_bool(trn)):
        break
    tmp = trn
print()
printmat(trn)
print()
print(pwr)
