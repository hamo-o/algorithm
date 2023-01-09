from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))

    queue = deque()
    for k, v in enumerate(li):
        queue.append([k, v])

    find_num = queue[m]

    cnt = 0
    p = max(li)
    while find_num in queue:
        if queue[0][1] == p:
            queue.popleft()
            cnt += 1
            if queue:
                p = max(queue, key=lambda x: x[1])[1]
        else:
            queue.rotate(-1)

    print(cnt)
