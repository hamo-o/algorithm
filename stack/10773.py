import sys
input = sys.stdin.readline

k = int(input())
li = []

for i in range(k):
    v = int(input())
    if v == 0:
        li.pop()
    else:
        li.append(v)

print(sum(li))
