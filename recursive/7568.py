n = int(input())
p = []

for i in range(n):
    a, b = map(int, input().split())
    p.append([a, b, 1])

for i in p:
    for j in p:
        if (i[0] < j[0] and i[1] < j[1]):
            i[2] += 1

for i in p:
    if(i == p[-1]):
        print(i[2])
    else:
        print(i[2], end=" ")