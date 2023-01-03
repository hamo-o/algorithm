from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.appendleft(i+1)

while len(queue) > 1:
    queue.pop()
    queue.rotate(1)

print(queue[0])
