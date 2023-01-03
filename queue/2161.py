from collections import deque

n = int(input())
queue = deque()
trash = []

for i in range(n):
    queue.appendleft(i+1)

while len(queue) > 1:
    trash.append(queue[-1])
    queue.pop()
    queue.rotate(1)

trash.append(queue[0])

print(" ".join(list(map(str, trash))))
