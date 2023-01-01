import sys
input = sys.stdin.readline

n = int(input())

li = [[0]*2 for i in range(n)]

for i in range(n):
    li[i][0], li[i][1] = map(int, input().split())

li.sort()

for i in li:
    print(" ".join(map(str, i)))
