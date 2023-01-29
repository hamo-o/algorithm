import sys
input = sys.stdin.readline

memo = {}

for i in range(0, 21):
    for j in range(0, 21):
        for k in range(0, 21):
            if i == 0 or j == 0 or k == 0:
                memo[(i, j, k)] = 1

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                memo[(i, j, k)] = memo[(i, j, k-1)] + memo[(i, j-1, k-1)] - memo[(i, j-1, k)]
            else:
                memo[(i, j, k)] = memo[(i-1, j, k)] + memo[(i-1, j-1, k)] \
                                  + memo[(i-1, j, k-1)] - memo[(i-1, j-1, k-1)]


while True:
    line = tuple(map(int, input().split()))
    if line == (-1, -1, -1):
        break

    if line[0] <= 0 or line[1] <= 0 or line[2] <= 0:
        print(f"w({line[0]}, {line[1]}, {line[2]}) = 1")
    elif line[0] > 20 or line[1] > 20 or line[2] > 20:
        print(f"w({line[0]}, {line[1]}, {line[2]}) = {memo[(20, 20, 20)]}")
    else:
        print(f"w({line[0]}, {line[1]}, {line[2]}) = {memo[line]}")
