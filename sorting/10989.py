import sys
input = sys.stdin.readline

n = int(input())
li = []
cnt = [0] * 10000

for i in range(n):
    cnt[int(input()) - 1] += 1

for k, v in enumerate(cnt):
    if v != 0:
        for i in range(v):
            print(k+1)
