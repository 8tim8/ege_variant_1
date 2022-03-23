for a in range(1, 1000):
    f = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((y - 40 < a) and (30 - y < a)) or (x * y > 20)) == 0:
                f = False
    if f:
        print(a)
        break

