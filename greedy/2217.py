import sys
input = sys.stdin.readline
ropes = []

n = int(input())

for i in range(n):
    ropes.append(int(input()))

ropes.sort()

m = 0
for rope in ropes:
    if rope * n > m:
        m = rope * n
    n -= 1

print(m)
