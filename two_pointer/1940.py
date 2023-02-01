n = int(input())
m = int(input())
li = list(map(int, input().split()))
li.sort()

start = 0
end = n-1
cnt = 0
s = li[start] + li[end]

while start < end:
    if s == m:
        cnt += 1
        start += 1
        end -= 1
        s = li[start] + li[end]

    elif s < m:
        s -= li[start]
        start += 1
        s += li[start]

    else:
        s -= li[end]
        end -= 1
        s += li[end]

print(cnt)
