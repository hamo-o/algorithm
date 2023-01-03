import sys
from collections import deque
input = sys.stdin.readline
queue = deque()


def push(q, item):
    q.append(item)


def pop(q):
    if q:
        print(q[0])
        q.popleft()
    else:
        print(-1)


def size(q):
    print(len(q))


def empty(q):
    if not q:
        print(1)
    else:
        print(0)


def front(q):
    if q:
        print(q[0])
    else:
        print(-1)


def back(q):
    if q:
        print(q[-1])
    else:
        print(-1)


n = int(input())

for i in range(n):
    cmd = input().split()

    if len(cmd) > 1:
        globals()[cmd[0]](queue, cmd[1])
    else:
        globals()[cmd[0]](queue)
