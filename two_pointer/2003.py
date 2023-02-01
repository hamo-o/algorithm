n, m = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
s = li[start]

while start < n:
    if s == m:
        s -= li[start]
        start += 1
        cnt += 1

    elif s < m:
        end += 1
        if end > n-1:
            break
        s += li[end]

    else:
        s -= li[start]
        start += 1

print(cnt)

# s = li[start]
# end = start
# while s <= m:
#     if s == m:
#         cnt += 1
#         break
#     if end == n-1:
#         break
#     end += 1
#     s += li[end]
#
# start += 1
