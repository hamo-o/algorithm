import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(list(input()))

cnt = 0
start = 0
end = n - 1
for line in chess:
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            cnt += 1
