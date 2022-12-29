import sys
input = sys.stdin.readline

n = int(input())
li = []
cnt = [0]*8001
m_cnt = 0
m_li = []
s = 0

for i in range(n):
    li.append(int(input()))
    s += li[i]

li.sort()

s = round(s/n)
m = li[n//2]
r = li[n - 1] - li[0]


for v in li:
    cnt[v+4000] += 1

m_cnt = max(cnt)

for k, v in enumerate(cnt):
    if m_cnt == v:
        m_li.append(k-4000)
    if len(m_li) == 2:
        break

# -2 1 2 2 3 8 8 8
# 현재 탐색하고 있는 수
# 수가 몇번 나왔는가??

# 산술평균
print(s)

# 중앙값
print(m)

# 최빈값
if len(m_li) == 1:
    print(m_li[0])
else:
    print(m_li[1])

# 범위
print(r)
