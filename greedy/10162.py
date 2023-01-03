# A 5분 == 300초
# B 1분 == 60초
# C 10초

# A는 B, C의 배수이고 B는 C의 배수이기 때문에 큰 거 우선!

t = int(input())
cnt = [0]*3

while t >= 300:
    t -= 300
    cnt[0] += 1

while t >= 60:
    t -= 60
    cnt[1] += 1

while t >= 10:
    t -= 10
    cnt[2] += 1

if t:
    print(-1)
else:
    print(" ".join(map(str, cnt)))
