import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

li = list(map(int, input().split()))
li.sort()

print(li)

dist = []
for i in range(n - 1):
    dist.append([li[i], li[i + 1] - li[i]])

dist.sort(key=lambda x: (x[1], x[0]))
print(dist)


arrange = 0
i = 0
while len(dist) > k+1:
    if i == len(dist)-1:
        i = 0
    if dist[i+1][0]-dist[i][0] <= 1:
        dist[i+1][1] += dist[i][1]
        dist.pop(i)

    i += 1

    print(dist)


