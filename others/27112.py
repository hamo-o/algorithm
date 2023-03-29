# 최소 시간 외 근무 일수?
# 시작한 이후 d일 후까지 끝내야 함, t일 동안 해야 함
import sys
input = sys.stdin.readline

n = int(input())
works = []
for i in range(n):
    d, t = map(int, input().split())
    works.append([d, t])

works.sort(key=lambda x: (x[0], -x[1]))

weekend_num = (works[-1][0] // 7)*2
day_num = 0
work_num = 0
cnt = 0

for work in works:
    day_num = work[0] - work_num

    if day_num >= work[1]:
        work_num += work[1]
    else:
        cnt += (work[1]-day_num)
        work_num += day_num

    # print(day_num, work[1], work_num, cnt)

if work_num > works[-1][0] - weekend_num:
    cnt += weekend_num

if cnt > works[-1][0]:
    print(-1)
else:
    print(cnt)
