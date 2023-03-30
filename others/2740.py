import sys
input = sys.stdin.readline
a = []
b = []

n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for i in range(m):
    b.append(list(map(int, input().split())))


# 일반적인 3중 반복문 행렬 곱셈
answer = [[0 for _ in range(k)] for _ in range(n)]
for f in range(n):
    for s in range(k):
        for j in range(m):
            answer[f][s] += a[f][j] * b[j][s]

for ans in answer:
    print((" ").join(map(str, ans)))

