# 일단 5짜리가 많을수록 좋긴하다
# 더이상 5 안들어갈때까지 우겨넣기
# 근데 5가 안들어가는데 남은게 3의 배수가 아니다?
# 5 하나 취소, 다시 남은게 3의 배수인지 확인
# 계속 취소해서 3의배수 나올때까지!

n = int(input())
v = n
cnt = 0

while v >= 5:
    v -= 5
    cnt += 1

while v % 3 != 0:
    v += 5
    cnt -= 1

if v > n:
    print(-1)
else:
    cnt += v // 3
    print(cnt)
