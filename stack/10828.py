n = int(input())
stack = []
result = []


def push(li, s):
    li.append(s)


def pop(li):
    if not li:
        result.append(-1)
    else:
        result.append(li[-1])
        li.pop()


def size(li):
    result.append(len(li))


def empty(li):
    if not li:
        result.append(1)
    else:
        result.append(0)


def top(li):
    if not li:
        result.append(-1)
    else:
        result.append(li[-1])


for i in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        locals()[cmd[0]](stack, cmd[1])
    else:
        locals()[cmd[0]](stack)


for v in result:
    print(v)