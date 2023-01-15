import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pwd = {}
to_find = []
ans = []
for i in range(n+m):
    if i < n:
        k, v = input().split()
        pwd[k] = v
    else:
        to_find.append(input()[:-1])

for item in to_find:
    print(pwd[item])