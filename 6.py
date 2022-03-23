for s in range(10000):
    x = s
    n = 740
    while s + n < 1200:
        s += 6
        n -= 4
    if n == 68:
        print(x)
        break
