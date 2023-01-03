from collections import deque

queue = deque()
p = []

n, k = map(int, input().split())

for i in range(n):
    queue.appendleft(i+1)

while queue:
    queue.rotate(k-1)
    p.append(queue[-1])
    queue.pop()

print("<"+", ".join(list(map(str, p)))+">")
