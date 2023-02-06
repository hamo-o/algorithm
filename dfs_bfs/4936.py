from collections import deque


def bfs(graph, start):
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    li = []
    key = []
    for i in range(h):
        temp = list(map(int, input().split()))
        for j in range(w):
            if temp[j] == 1:
                key.append((i, j))
        li.append(temp)

    count = len(key)
    matrix = {node: [] for node in key}
    for i in range(count):
        for j in range(count):
            if abs(key[i][0]-key[j][0]) + abs(key[i][1]-key[j][1]) == 1 or \
                    (abs(key[i][0]-key[j][0]) == 1 and abs(key[i][1]-key[j][1]) == 1):
                matrix[key[i]].append(key[j])

    visited = {node: False for node in key}
    count = 0
    for node in key:
        if not visited[node]:
            bfs(matrix, node)
            count += 1

    print(count)
