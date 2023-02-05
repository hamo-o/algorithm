from collections import deque

t = int(input())


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


for i in range(t):
    m, n, k = map(int, input().split())
    li = []
    for i in range(k):
        li.append(list(map(int, input().split())))
    li.sort()

    matrix = {i: [] for i in range(1, k+1)}
    for i in range(k):
        for j in range(k):
            if abs(li[i][0] - li[j][0]) + abs(li[i][1] - li[j][1]) == 1:
                matrix[i+1].append(j+1)
    visited = [False]*(k+1)
    count = 0

    for i in range(k):
        if not visited[i+1]:
            bfs(matrix, i+1)
            count += 1

    print(count)
