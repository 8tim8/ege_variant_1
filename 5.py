for n in range(1, 1000):
    b = bin(n)[2:]
    x = b.count('1')
    b += b[-1]
    if x % 2 == 0:
        b += '0'
    else:
        b += '1'
    x = b.count('1')
    if x % 2 == 0:
        b += '0'
    else:
        b += '1'
    if int(b, 2) > 80:
        print(int(b, 2))
        break
