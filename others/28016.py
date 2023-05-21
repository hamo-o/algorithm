from collections import deque
import sys
input = sys.stdin.readline
# 공이 못을 만나면 같은 확률로 못 양옆 중 한 곳에 떨어짐
# 공 바로 옆이나 대각선 아래에 있으면 그 방향으로는 못감

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [0]*m
for j in range(m):
    if board[0][j] == 2:
        start = j

queue = deque()
queue.append([0, start])

while queue:
    cur = queue.popleft()
    if cur[0] == n-1:
        visited[cur[1]] += 1
    for i in range(cur[0], n):
        if board[i][cur[1]] == 1:
            if cur[1] > 0 and board[i-1][cur[1]-1] != 1 and board[i][cur[1]-1] != 1:
                queue.append([i, cur[1]-1])
            if cur[1] < n-1 and board[i-1][cur[1]+1] != 1 and board[i][cur[1]+1] != 1:
                queue.append([i, cur[1]+1])
        if cur[0]+1 == i and board[i][cur[1]] == 0:
            queue.append([i, start])


if visited.count(0) == m:
    answer = -1
else:
    for i in range(m):
        max_visited = 0
        answer = 0
        if max_visited < visited[i]:
            max_visited = visited[i]
            answer = i

print(answer)