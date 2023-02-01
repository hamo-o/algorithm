n = int(input())
li = list(map(int, input().split()))
x = int(input())

li.sort()

start = 0
end = n-1
s = li[start] + li[end]
cnt = 0

while start < end:
    if s == x:
        cnt += 1
        start += 1
        end -= 1
        s = li[start] + li[end]
    elif s < x:
        s -= li[start]
        start += 1
        s += li[start]
    else:
        s -= li[end]
        end -= 1
        s += li[end]

print(cnt)
