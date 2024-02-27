def kruskal():
    n = 7
    used = [0, 0, 0, 0, 0, 0, 0]
    summ = 0

    for i in range(n):
        min = 99    
        a, b = 0, 0 
        for j in range(n - 1):
            if mass[i][j] < min and mass[i][j] != 0 and (used[i] == 0 or used[j] == 0):
                min = mass[i][j]
                a, b = i, j
        used[a] = 1
        used[b] = 1
        summ += mass[a][b]

    print(summ)

def prima():
    n = 7
    used = [1, 0, 1, 0, 0, 0, 0]
    summ = 16
    a, b = 0, 0
    for k in range(5):
        min = 99
        for i in range(n):
            if used[i]:
                for j in range(n):
                    if used[j] == 0:
                        if mass[i][j] < min and mass[i][j] != 0:
                            min = mass[i][j]
                            a, b = i, j
        used[b] = 1
        summ += mass[a][b]
    print(summ)

mass = [
    [0, 21, 16, 0, 0, 0, 22],   
    [21, 0, 15, 0, 0, 0, 0],    
    [16, 15, 0, 27, 13, 0, 17], 
    [0, 0, 27, 0, 19, 0, 0],    
    [0, 0, 13, 19, 0, 24, 0],   
    [0, 0, 0, 0, 24, 0, 29],    
    [22, 0, 17, 0, 0, 29, 0],   
    ]

kruskal()
prima()
