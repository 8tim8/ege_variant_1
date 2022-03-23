k = 0
mi = 0
for i in range(201, 400):
    s = '5' * i
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '555', 1)
    if s.count('5') > k:
        k = s.count('5')
        mi = i
print(mi)

