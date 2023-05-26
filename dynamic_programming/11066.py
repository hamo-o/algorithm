# 파일 합치기 3과 다른 점은 연속이어야함!! -> Chained Matrix
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    sum_files = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(i, n):
            sum_files[i+1][j+1] = sum_files[i+1][j] + files[j]

    M = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for diagonal in range(1, n+1):
        for i in range(1, n-diagonal+1):
            # diagonal은 몇개의 파일의 합을 구할건지 나타냄 (합의 길이)
            j = i + diagonal
            min_sum = float("inf")
            for k in range(i, j):
                min_sum = min(min_sum, M[i][k] + M[k+1][j] + sum_files[i][k] + sum_files[k+1][j])

            M[i][j] = min_sum

    print(M[1][n])
