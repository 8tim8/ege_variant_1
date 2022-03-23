def rec(x, n, c):  # начальное число, длина программы, нужное число
    if n == 0:
        if x == c:
            return 1
        return 0
    return rec(x + 1, n - 1, c) + \
           rec(x * 2, n - 1, c) + \
           rec(x + (x % 4), n - 1, c)


a = []
k = 0
for n in range(1, 6):
    for i in range(81):
        if rec(i, n, 80) > 0:
            if not(i in a):
                k += 1
                a.append(i)
print(k)
