n = int(input())
li = []
cnt = []
s = 0

for i in range(n):
    li.append(int(input()))

li.sort()

for i, item in enumerate(li):
    s += item
    cnt.append(li.count(item))

# 산술평균
print(round(s/n))

# 중앙값
print(li[n//2])

# 최빈값
m_idx = [k for k, v in enumerate(cnt) if max(cnt) == v]
m_li = [li[i] for i in m_idx]
m_li = list(set(m_li))
m_li.sort()

if len(m_li) == 1:
    print(m_li[0])
else:
    print(m_li[1])

# 범위
print(li[n - 1] - li[0])