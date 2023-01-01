# 돈을 인출 하는 시간은 앞사람 시간 + 내 시간
# 즉 시간이 긴 사람이 뒤에 있을 수록 누적합이 작아짐

n = int(input())
li = list(map(int, input().split()))
s_li = []

li.sort()

for i in range(n):
    s = 0
    for j in range(i+1):
        s += li[j]
    s_li.append(s)

print(sum(s_li))
