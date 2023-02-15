k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

left = 1
right = max(lines)

while True:
    mid = (left+right)//2
    count = 0

    for line in lines:
        count += line//mid

    if left > right:
        print(mid)
        break

    if count < n:
        right = mid - 1

    else:
        left = mid + 1