f = open('17-3.txt')
a = [int(x) for x in f]
k = 0
s = 0
for i in range(1, len(a)):
    x = a[i]
    y = a[i - 1]
    if (x % 2 == 0 and y % 2 != 0 and x % 4 == 0 and y % 11 == 0) or (x % 2 != 0 and y % 2 == 0 and x % 11 == 0 and y % 4 == 0):
        k += 1
        s = max(s, x + y)
print(k, s)
