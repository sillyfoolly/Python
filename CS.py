def mid_squares_method(xo1, n):

    
    one, two, three, four, five, six, seven, eight, nine, zero = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    print ('Псевдослучайное число', xo1)
    x = xo1 * 10000000
    x = (x - (x // 1)) * 10 // 1
    zero += 1
    print ("%1.0f" %x)
    for i in range(n - 1):
        xo1 = xo1 * xo1 * 100000
        xo1 = (xo1 - (xo1 // 1)) * 10000000000 // 1 / 10000000000 
        print ('Псевдослучайное число', "%0.10f" %xo1)

        x = xo1 * 10000000
        x = (x - (x // 1)) * 10 // 1
        x = int(x) 

        match(x):
            case 1:
                one += 1
            case 2:
                two += 1
            case 3:
                three += 1
            case 4:
                four += 1
            case 5:
                five += 1
            case 6:
                six += 1
            case 7:
                seven += 1
            case 8:
                eight += 1
            case 9:
                nine += 1
            case 0:
                zero += 1
    print(one, two, three, four, five, six, seven, eight, nine, zero)

mid_squares_method(0.1080762024, 199)
