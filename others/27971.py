import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())
disappear = []
for _ in range(m):
    disappear.append(list(map(int, input().split())))


def check(num):
    if disappear:
        for d in disappear:
            if (num >= d[0]) and (num <= d[1]):
                return 0
    return 1


memo = [0 for _ in range(n+1)]
if check(a):
    memo[a] = 1
if check(b):
    memo[b] = 1


for i in range(min(a, b)+1, n+1):
    promising = []
    if not memo[i] and check(i):
        if i >= a and memo[i-a] > 0:
            promising.append(memo[i-a]+1)
        if i >= b and memo[i-b] > 0:
            promising.append(memo[i-b]+1)
        if promising:
            memo[i] = min(promising)
        else:
            memo[i] = -1

print(memo[n])