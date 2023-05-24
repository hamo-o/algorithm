from collections import deque

n, k = map(int, input().split())
queue = deque()

for i in range(n):
    queue.append(i+1)

for i in range(n):
    if len(queue) == 1:
        break
    queue.rotate(-1)
    for j in range(min(len(queue)-1, k-1)):
        queue.popleft()

print(queue[0])
