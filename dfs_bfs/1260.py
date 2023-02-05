from collections import deque

n, m, v = map(int, input().split())
li = []
for i in range(m):
    temp = list(map(int, input().split()))
    li.append(temp)

matrix = {}
for i in range(1, n+1):
    matrix[i] = []

for item in li:
    matrix[item[0]].append(item[1])
    matrix[item[1]].append(item[0])

for i in range(1, n+1):
    matrix[i].sort()


dfs_answer = []
bfs_answer = []


def dfs(graph, cur, visited):
    visited[cur] = True
    dfs_answer.append(cur)

    for i in graph[cur]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur = queue.popleft()
        bfs_answer.append(cur)

        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(matrix, v, [False]*(n+1))
bfs(matrix, v, [False]*(n+1))

print(" ".join(map(str, dfs_answer)))
print(" ".join(map(str, bfs_answer)))
