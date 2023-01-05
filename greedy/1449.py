# 갭 배열 저장
# [1 98 1]
# 일단 무지성으로 붙여 맨첨부터 끝까지
# 갭 배열의 합 + 1(양끝) = 101
# 근데 2짜리만 쓸수 있네?
# 그러면 갭중에 최댓값 없애기, cnt + 1
# [1 1]
# 각 요소 + 1(양끝) 한 최댓값이 2랑 같거나 작으면 됨

n, l = map(int, input().split())
spot = list(map(int, input().split()))
gap = []

spot.sort()

for i in range(n-1):
    gap.append(spot[i+1]-spot[i])

gap.sort()

cnt = 1
if sum(gap) + 1 > l:
    gap.pop()
    cnt += 1
    while len(gap) and max(gap) + 1 > l:
        gap.pop()
        cnt += 1

print(cnt)
