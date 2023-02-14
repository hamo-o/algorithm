import sys
input = sys.stdin.readline

n = int(input())
# 이름 국어 영어 수학
scores = []
for i in range(n):
    name, k, e, m = input().split()
    temp = [name, int(k), int(e), int(m)]
    scores.append(temp)

# 국어 점수 감소
# 영어 점수 증가
# 수학 점수 감소
# 이름 사전순 증가

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for score in scores:
    print(score[0])
