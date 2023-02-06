from collections import deque

n = int(input())
li = []
key = []
for i in range(n):
    temp = input()
    for j in range(n):
        if temp[j] == "1":
            key.append((i, j))
    li.append(list(map(int, temp)))

house = len(key)

matrix = {}
for i in range(house):
    matrix[key[i]] = []

for i in range(house):
    for j in range(house):
        if (abs(key[i][0] - key[j][0]) + abs(key[i][1] - key[j][1])) == 1:
            matrix[key[i]].append(key[j])


def bfs(graph, start):
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        houses.append(cur)
        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


visited = {node: False for node in key}
counts = 0
count = []
for node in key:
    houses = []
    if not visited[node]:
        bfs(matrix, node)
        count.append(len(houses))
        counts += 1

print(counts)
count.sort()
for cnt in count:
    print(cnt)
