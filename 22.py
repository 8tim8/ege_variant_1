k = 0
for n in range(10, 100):
    i = 0
    x = n
    while n > 0:
        i = i + n % 8
        n = n // 8
    if i % 7 == 0:
        k += 1
print(k)
