up_num = 5
down_num = 11

n, m = map(int, input().split())
stations = []
for _ in range(n):
    stations.append(input())

# n개의 역 중에 m-1개의 변환이 있어야 한다
# 변환 가능 수를 넘으면 그냥 그대로 출력
# 이때, 롤러코스터 구간의 길이는 m이므로 이 구간은 묶어서 하나로 보고,
# 롤러코스터 구간을 언제 시작하냐에 따라 경우의 수가 달라진다.

if m == 1:
    start = 1
else:
    start = n-m+1
flags = [[] for _ in range(start)]

for s in range(start):
    flag = False
    cnt = m-1
    for i in range(n):
        if cnt and s <= i:
            flags[s].append(flag)
            flag = not flag
            cnt -= 1
        else:
            flags[s].append(flag)

answer_down = 0
answer_up = 0
for li in flags:
    temp_down = 1
    temp_up = 1
    for f in li:
        if f:
            temp_down *= 11
            temp_up *= 5
        else:
            temp_down *= 5
            temp_up *= 11
    answer_down += temp_down
    answer_up += temp_up

print(answer_down+answer_up % (1000000000+7))
