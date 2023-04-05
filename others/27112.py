# 최소 시간 외 근무 일수?
# 시작한 이후 d일 후까지 끝내야 함, t일 동안 해야 함
import sys
input = sys.stdin.readline

n = int(input())
works = []
for i in range(n):
    d, t = map(int, input().split())
    works.append([d, t])

works.sort()

time = 0
regular_work = 0
overtime_work = 0

for work in works:
    time = work[0]

    # 주말이 포함되어 있을 경우 주말 통째로 빼주기
    time -= (work[0]//7)*2

    # 토요일로 끝나는 경우 토요일 빼주기
    if work[0] % 7 == 6:
        time -= 1

    regular_work += work[1]

    if time < regular_work:
        overtime_work += (regular_work - time)
        regular_work = time

    if overtime_work > work[0]:
        overtime_work = -1
        break


print(overtime_work)
