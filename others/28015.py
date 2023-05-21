# 0으로 떨어져 있는 서로 다른 숫자의 종류 수
import sys
input = sys.stdin.readline


def cal_count(c1, c2):
    answer = 0
    if c1 and c2:
        # 둘 중 더 적은 구간의 수 + 처음 반대색 칠하는 횟수 1
        answer = min(c1, c2) + 1
    elif c1:
        answer = c1
    elif c2:
        answer = c2

    return answer


n, m = map(int, input().split())
cnt = 0
for _ in range(n):
    draw = list(map(int, input().split()))
    color1 = color2 = 0
    flag = 0

    for i, d in enumerate(draw):
        if flag != d:
            if d == 1:
                color1 += 1
            elif d == 2:
                color2 += 1
            else:
                cnt += cal_count(color1, color2)
                color1 = color2 = 0
        flag = d

    if flag:
        cnt += cal_count(color1, color2)

print(cnt)
