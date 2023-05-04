import sys
input = sys.stdin.readline

n = int(input())
flowers = list(map(int, input().split()))

beauty = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
visited[flowers[0]] = 1

for i in range(1, n):
    visited[flowers[i]] = 1
    max_beauty = 0
    for j in range(1, 101):
        if visited[j]:
            max_beauty = max(max_beauty, beauty[j] + (j-flowers[i])**2)
    beauty[flowers[i]] = max_beauty

print(beauty[flowers[n-1]])
