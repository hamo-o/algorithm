# 새로운 x는 x보다 작은 수가 몇 개인가? 그 개수!

import sys
input = sys.stdin.readline

n = int(input())

li = (list(map(int, input().split())))

for i in range(n):
    li[i] = [i, li[i], 0]


sorted_li = sorted(li, key=lambda x: x[1])

sorted_li[0][2] = 0
for i in range(1, n):
    if sorted_li[i][1] == sorted_li[i-1][1]:
        sorted_li[i][2] = sorted_li[i-1][2]
    else:
        sorted_li[i][2] = sorted_li[i-1][2]+1

sorted_li.sort(key=lambda x: x[0])

a = [item[2] for item in li]
a = " ".join(map(str, a))
print(a)
