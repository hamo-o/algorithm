import sys
input = sys.stdin.readline

n = int(input())
flag = [0]*200001
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())

    if flag[a] == b:
        cnt += 1

    flag[a] = b

for i in range(200001):
    if flag[i]:
        cnt += 1

print(cnt)
