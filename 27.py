f = open("27-96b.txt")
n = int(f.readline())
s, k5, k7, max_sum = 0, 0, 0, 0
min_sum = {0: 0}
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 5 == 0:
        k5 += 1
    if x % 7 == 0:
        k7 += 1
    if not(k5 - k7 in min_sum):
        min_sum[k5 - k7] = s
    else:
        if max_sum == 0 or s - min_sum[k5 - k7] > max_sum:
            max_sum = s - min_sum[k5 - k7]
print(max_sum)
