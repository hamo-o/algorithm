import sys
input = sys.stdin.readline

n = int(input())
n_li = list(map(int, input().split()))

m = int(input())
m_li = list(map(int, input().split()))

for i in range(m):
    m_li[i] = [i, m_li[i]]

n_li.sort()
m_li.sort(key=lambda x: x[1])

for i in m_li:
    if i[1] > n_li[-1]:
        i.append(0)
    else:
        if i[1] in n_li:
            i.append(1)
        else:
            i.append(0)

m_li.sort(key=lambda x: x[0])

for i in m_li:
    print(i[2])