import sys
input = sys.stdin.readline

w, n = input().split()
n = int(n)

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 5:
            matrix[i][j] = "2"
        elif matrix[i][j] == 2:
            matrix[i][j] = "5"
        elif matrix[i][j] == 1 or matrix[i][j] == 8:
            matrix[i][j] = str(matrix[i][j])
        else:
            matrix[i][j] = "?"

if w == "L" or w == "R":
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
else:
    for i in range(n//2):
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

for m in matrix:
    print(" ".join(m))
