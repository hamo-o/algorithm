# 발각되지 않는 방법? 최단경로! 되돌아가면 안됨(왼, 위 X)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[True for _ in range(m)] for _ in range(n)]

for i in range(n-1):
    info = list(input().split())
    k = int(info[0])

    if k == 1:
        if info[2] == "R":
            for j in range(int(info[1])-1, m):
                matrix[i][j] = False
        else:
            for j in range(0, int(info[1])):
                matrix[i][j] = False

    elif k == 2:
        if info[2] == "R":
            for j in range(int(info[1])-1, int(info[3])):
                matrix[i][j] = False
        else:
            for j in range(int(info[3])-1, int(info[1])):
                matrix[i][j] = False

for m in matrix:
    print(m)