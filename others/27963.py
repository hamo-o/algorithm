# 금속1밀도, 금속2밀도, 밀도가 더 높은 금속이 주화에서 차지하는 질량비
# 기념주화의 밀도는?
# 밀도 = 질량/부피
# 부피 = 질량/밀도
d1, d2, x = map(int, input().split())

big = max(d1, d2)
sml = min(d1, d2)

print(100/(x/big+(100-x)/sml))