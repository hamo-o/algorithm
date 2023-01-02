n = int(input())

a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

a_li.sort()
b_li.sort(key=lambda x: -x)

s = 0
for i in range(n):
    s += a_li[i] * b_li[i]

print(s)
