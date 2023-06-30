import sys
input = sys.stdin.readline

line = input().strip()

if line:
    print(line.count(" ")+1)
else:
    print(0)
