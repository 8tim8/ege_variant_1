f = open('24-s2.txt')
s = f.readline()
a = [0] * 26
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(s)-1):
    if s[i] == 'X':
        for j in range(26):
            if s[i + 1] == alp[j]:
                a[j] += 1
m = max(a)
for i in range(26):
    if a[i] == m:
        print(alp[i])
        print(m)
        break



# with open("24-s2.txt") as F:
#   s = F.readline() # считали строку
#
# d={} # словарь букв
# while "X" in s:
#   n = s.find("X")# индекс "X"
#   key = s[n+1] # создаем ключ = Букве
#   d[key] = d.get(key,0)+1
#   s = s[n+1:]# срез, формируем новую строку
#
# Max = max(d.values())# макс значение ключа
# a = [x[0] for x in d.items() if x[1] == Max]
# a.sort()
# print(a[0]+str(Max))
