import sys
input = sys.stdin.readline

n = int(input())
s = []

for i in range(n):
    s.append(input()[0:-1])

s = list(set(s))
s.sort(key=lambda x: (len(x), x))

for i in s:
    print(i)
