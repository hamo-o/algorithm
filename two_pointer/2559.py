n, k = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = 0
s = li[start]

while start <= n-k:
    if end - start + 1 == k:
        if start == 0:
            m = s
        else:
            m = max(s, m)
        s -= li[start]
        start += 1

    else:
        end += 1
        s += li[end]

print(m)

