from collections import deque

queue = deque()

n, m = map(int, input().split())
pick = list(map(int, input().split()))
cnt = 0

for i in range(n):
    queue.appendleft(i+1)

for item in pick:
    idx = queue.index(item)

    if idx < (len(queue)-1)/2:
        queue.rotate(-(idx+1))
        queue.pop()
        cnt += idx+1
    else:
        queue.rotate(len(queue)-idx-1)
        cnt += (len(queue) - idx - 1)
        queue.pop()

print(cnt)
