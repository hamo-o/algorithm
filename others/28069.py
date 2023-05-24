# k번 행동해서 n번째 계단에 도달해야 함
# 계단 한 칸 오르기
# i + i//2 으로 오르기

# 5개의 계단을 2번만에 오르자
from collections import deque

n, k = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i].append(i+1)
    if i+i//2 <= n and i+i//2 != i+1:
        graph[i].append(i+i//2)

queue = deque()
visited = [0]*(n+1)

start = 1
queue.append(start)
visited[start] = 1
while queue:
    cur = queue.popleft()
    if cur == n:
        break
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = visited[cur] + 1
            queue.append(node)

if visited[-1] <= k:
    print("minigimbob")
else:
    print("water")
