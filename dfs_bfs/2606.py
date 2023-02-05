n = int(input())
line = int(input())

matrix = {}
for i in range(n):
    matrix[i+1] = []

for i in range(line):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

for i in range(n):
    matrix[i+1].sort()

answer = []


def dfs(graph, cur, visited):
    visited[cur] = True
    answer.append(cur)

    for node in graph[cur]:
        if not visited[node]:
            dfs(graph, node, visited)


dfs(matrix, 1, [False]*(n+1))

print(len(answer)-1)
