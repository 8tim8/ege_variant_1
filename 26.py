with open('26-68.txt') as f:
    n, t = map(int, f.readline().split())
    a = [list(map(int, f.readline().split())) for _ in range(n)]
    s = 0
    for i in a:
        s += i[0]
    srd = s / n
    sup = []
    usl = []
    for i in a:
        if i[0] > srd:
            sup.append(i[1])
        elif i[0] < srd:
            usl.append(i[1])
    sup.sort()
    usl.sort()
    k = 0
    t_sup = 0
    total = 0
    for i in range(len(usl)):
        if usl[i] + sup[i] + total <= t:
            k += 2
            total += usl[i] + sup[i]
            t_sup += sup[i]
        elif total + usl[i] <= t:
            k += 1
            total += usl[i]
print(k, t_sup)

