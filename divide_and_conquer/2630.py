import sys
input = sys.stdin.readline

n = int(input())


papers = []
for i in range(n):
    line = list(map(int, input().split()))
    papers.append(line)


# [white, blue]
answer = [0, 0]

def divide(size, x, y):
    mid = size // 2

    if size == 1:
        return papers[x][y]

    lt = divide(mid, x, y)
    rt = divide(mid, x+mid, y)
    lb = divide(mid, x, y+mid)
    rb = divide(mid, x+mid, y+mid)
    if lt == rt == lb == rb:
        return lt
    else:
        answer[0] += [lt, rt, lb, rb].count(0)
        answer[1] += [lt, rt, lb, rb].count(1)


if all(0 not in line for line in papers):
    answer[1] = 1
elif all(1 not in line for line in papers):
    answer[0] = 1
else:
    divide(n, 0, 0)

print(answer[0])
print(answer[1])

