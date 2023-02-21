import sys
input = sys.stdin.readline
n = int(input())

lines = []
for _ in range(n):
    lines.append(int(input()))

lines.sort()

# 제일 큰거 < 작은거 두개 합
big = n-1
while big >= 2:
    if lines[big] < lines[big-1]+lines[big-2]:
        print(lines[big]+lines[big-1]+lines[big-2])
        break
    else:
        big -= 1

if big == 1:
    print(-1)
