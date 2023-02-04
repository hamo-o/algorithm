n, x = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = 0
s = li[start]
m = []

while start <= n - x:
    if end - start + 1 == x:
        m.append(s)
        s -= li[start]
        start += 1
    else:
        end += 1
        s += li[end]

m.sort()
if m[-1] == 0:
    print("SAD")
else:
    print(m[-1])
    print(m.count(m[-1]))
