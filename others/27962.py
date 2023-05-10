from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
origin_str = input()


def find_str():
    a = []
    b = deque()
    start = 0
    end = n-1

    while (start < n) and (end >= 0):
        a.append(origin_str[start])
        b.appendleft(origin_str[end])

        cnt = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                cnt += 1

        if len(a) >= 1 and cnt == len(a)-1:
            return 1

        start += 1
        end -= 1

    return 0


answer = find_str()
if answer:
    print("YES")
else:
    print("NO")
