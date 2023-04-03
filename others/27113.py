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
            if info[4] == "R":
                if int(info[1]) > int(info[3]):
                    left = int(info[3])
                else:
                    left = int(info[1])
                lines.append([left, m])
            else:
                if int(info[1]) > int(info[3]):
                    lines.append([0, int(info[3]), int(info[1]), m])
                else:
                    lines.append([int(info[1]), int(info[3])])
        else:
            if info[2] == "L":
                left = 0
                right = 0
                if info[4] == "L":
                    if int(info[1]) > int(info[3]):
                        right = int(info[1])
                    else:
                        right = int(info[3])
                    lines.append([0, right])
                else:
                    if int(info[1]) < int(info[3]):
                        lines.append([0, int(info[1]), int(info[3]), m])
                    else:
                        lines.append([int(info[3]), int(info[1])])
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

        if line[2] <= x <= line[3]:
            break
        else:
            y += 1
    elif line[0] <= x <= line[1]:
        x = line[1]+1
        if x > m:
            break
        else:
            y += 1
    else:
        y += 1

if y == n:
    print("YES")
else:
    print("NO")
