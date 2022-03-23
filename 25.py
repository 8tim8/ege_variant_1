from math import sqrt

for n in range(135790, 163229):
    k = 0
    s = 0
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            k += 2
            s += j
            s += n // j
    if s > 460000:
        print(k, s)
