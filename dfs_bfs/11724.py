import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = {}
nodes = set()
for i in range(n):
    matrix[i+1] = []

for i in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)


# def dfs(graph, cur, visited):
#     visited[cur] = True
#     check.add(cur)
#
#     for node in graph[cur]:
#         if not visited[node]:
#             dfs(graph, node, visited)

# check = set()
# count = 0
# while len(check) < n:
#     dfs(matrix, min(list(nodes - check)), [False] * (n+1))
#     count += 1


def bfs(graph, start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur = queue.popleft()

        for node in graph[cur]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


visited = [False]*(n+1)
count = 0
for i in range(n):
    if not visited[i+1]:
        bfs(matrix, i+1)
        count += 1

print(count)

