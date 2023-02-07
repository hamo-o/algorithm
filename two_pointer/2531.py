n, d, k, c = map(int, input().split())
li = []

for i in range(n):
    li.append(int(input()))

start = 0
end = 1
m = 1
length = 1

count = [0 for _ in range(d+1)]
count[li[0]] = 1
total = 1


while start < n and length < k+1:
    if length == k:

        if not count[c]:
            m = max(m, total+1)
        else:
            m = max(m, total)

        if count[li[start]] == 1:
            total -= 1
        count[li[start]] -= 1
        start += 1

        length -= 1
    else:
        count[li[end]] += 1

        if count[li[end]] == 1:
            total += 1

        if end == n-1:
            end = 0
        else:
            end += 1

        length += 1

print(m)
