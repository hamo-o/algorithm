# ㅅㅓ류 성적 / 면접 성적
# nlogn

# 1 4 ok
# 2 5 위의 최소 4랑 비교해서 뒤에 숫자가 더 작으면 오키 X
# 3 6 위의 최소 4랑 비교해서 뒤에 숫자가 더 작으면 오키 X
# 4 2 위의 최소 4랑 비교해서 뒤에 숫자가 더 작으면 오키 ok
# 5 7 위의 최소 2랑 비교해서 뒤에 숫자가 더 작으면 오키 X
# 6 1 위의 최소 2랑 비교해서 뒤에 숫자가 더 작으면 오키 ok
# 7 3 위의 최소 1랑 비교해서 뒤에 숫자가 더 작으면 오키 X

# 1 4 4 ok
# 2 7 4 x
# 3 6 4 x
# 4 5 4 x
# 5 3 4 ok
# 6 2 3 ok
# 7 1 2 ok

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    li = []
    cnt = 1
    for i in range(n):
        li.append(tuple(map(int, input().split())))
    li.sort()

    min_num = li[0][1]
    for i in range(n-1):
        if min_num > li[i+1][1]:
            cnt += 1
            min_num = li[i+1][1]

    print(cnt)