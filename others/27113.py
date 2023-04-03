# 발각되지 않는 방법? 최단경로! 되돌아가면 안됨(왼, 위 X)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = []

for i in range(n-1):
    info = list(input().split())
    k = int(info[0])

    if k == 1:
        if info[2] == "R":
            lines.append([int(info[1]), m])
        else:
            lines.append([1, int(info[1])])

    elif k == 2:
        if info[2] == "R":
            left = 0
            right = 0
            # 오른쪽 오른쪽이면 더 작은숫자부터 끝까지
            if info[4] == "R":
                if int(info[1]) > int(info[3]):
                    left = int(info[3])
                else:
                    left = int(info[1])
                lines.append([left, m])
            # 오른쪽 왼쪽이면
            # 만약 오른쪽이 왼쪽보다 더 크면 양쪽으로 두개가 생기고
            # 만약 왼쪽이 오른쪽보다 더 크면 가운데 범위이다
            else:
                if int(info[1]) > int(info[3]):
                    left = int(info[3])
                    right = int(info[1])
                    lines.append([0, left, right, m])
                else:
                    left = int(info[1])
                    right = int(info[3])
                    lines.append([left, right])
        else:
            if info[2] == "L":
                left = 0
                right = 0
                # 왼쪽 왼쪽이면 0부터 더 큰 숫자까지
                if info[4] == "L":
                    if int(info[1]) > int(info[3]):
                        right = int(info[1])
                    else:
                        right = int(info[3])
                    lines.append([0, right])
                # 왼쪽 오른쪽이면
                # 만약 오른쪽이 왼쪽보다 더 크면 양쪽으로 두개가 생기고
                # 만약 왼쪽이 오른쪽보다 더 크면 가운데 범위이다
                else:
                    if int(info[1]) < int(info[3]):
                        left = int(info[1])
                        right = int(info[3])
                        lines.append([0, left, right, m])
                    else:
                        left = int(info[3])
                        right = int(info[1])
                        lines.append([left, right])
    else:
        lines.append([])

x = 1
y = 1
for line in lines:
    if len(line) == 0:
        y += 1
    elif len(line) == 4:
        if line[0] <= x <= line[1]:
            x = line[1] + 1
            y += 1
        elif line[2] <= x <= line[3]:
            break
        else:
            y += 1
    elif line[0] <= x <= line[1]:
        x = line[1]+1
        if x == m+1:
            break
        else:
            y += 1
    else:
        y += 1

if x == m and y == n:
    print("YES")
else:
    print("NO")
