# 2를 곱한다
# 1을 수의 가장 오른쪽에 추가한다
# 거꾸로 접근.
# B에서 우선 1이 없을때까지 1을 뗀다
# 없으면 2로 나눈다
# 1이 생기면 또 1을 뗀다
# 없으면 2로 나눈다
# A가 나올때까지 계속, A보다 작아지면 종료하고 -1 return

a, b = map(int, input().split())
li_b = list(map(int, str(b)))

cnt = 0
while b > a:
    if li_b[-1] == 1:
        b = b // 10
        li_b.pop()
        cnt += 1
    elif b % 2 == 0:
        b = b // 2
        li_b = list(map(int, str(b)))
        cnt += 1
    else:
        break

if a == b:
    print(cnt+1)
else:
    print(-1)
