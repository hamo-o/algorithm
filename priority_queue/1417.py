n = int(input())

li = []
for i in range(n):
    temp = int(input())
    if i == 0:
        k = temp
    elif k <= temp:
        li.append(temp)

if li:
    li.sort()
    start = k
    while li[-1] >= k:
        k += 1
        li[-1] -= 1
        li.sort()
    print(k-start)
else:
    print(0)

# 반례
# 3
# 1
# 6
# 6

