import sys
from itertools import product
input = sys.stdin.readline

UP_STATIONS = 5
DOWN_STATIONS = 11

# n개의 역 m 길이의 롤러코스터 구간
n, m = map(int, input().split())
for _ in range(n):
    input()


# 0 1
# 2개 중에서 3개를 중복을 허용해서 뽑기
# 중복순열
roads = list(product([0, 1], repeat=n))


def check_len(nums):
    cnt = 1
    max_cnt = 1
    prev = nums[0]
    for num in nums:
        if num != prev:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
        prev = num

    return max_cnt


result = 0
if m == 1:
    result = UP_STATIONS**n + DOWN_STATIONS**n
else:
    for road in roads:
        if check_len(road) == m:
            result += (UP_STATIONS**road.count(1) * DOWN_STATIONS**road.count(0))

print(result % (10**9+7))
