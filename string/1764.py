import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_li = set()
m_li = set()

for _ in range(n):
    n_li.add(input().strip())
for _ in range(m):
    m_li.add(input().strip())

answer = list(n_li & m_li)
answer.sort()

print(len(answer))
for a in answer:
    print(a)