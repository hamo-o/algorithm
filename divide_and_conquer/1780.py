n = int(input())

papers = []
for i in range(n):
    line = list(map(int, input().split()))
    papers.append(line)


def divide(size, x, y):
    if size == 1:
        return papers[x][y]

    mid = size // 3

    lt = divide(mid, x, y)
    mt = divide(mid, x+mid, y)
    rt = divide(mid, x+2*mid, y)
    lm = divide(mid, x, y+mid)
    mm = divide(mid, x+mid, y+mid)
    rm = divide(mid, x+2*mid, y+mid)
    lb = divide(mid, x, y+2*mid)
    mb = divide(mid, x+mid, y+2*mid)
    rb = divide(mid, x+2*mid, y+2*mid)

    paper = [lt, mt, rt, lm, mm, rm, lb, mb, rb]

    for k in range(-1, 2):
        if paper.count(k) == 9:
            if size == n:
                answer[k+1] += 1
                break
            else:
                return lt

    else:
        answer[0] += paper.count(-1)
        answer[1] += paper.count(0)
        answer[2] += paper.count(1)


answer = [0, 0, 0]

divide(n, 0, 0)

for item in answer:
    print(item)
