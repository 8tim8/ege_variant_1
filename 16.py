def f(n):
    if n <= 5:
        return n
    if n > 5:
        if n % 3 == 0:
            return n + f(n // 3 + 1)
        else:
            return n + f(n + 3)


n = 1
while True:
    try:
        r = f(n)
    except:
        pass
    else:
        print(n, r)
        if r > 1000:
            break
    n += 1

