k, n = map(int, input().split())
li = []
for i in range(k):
    li.append(int(input()))

left = 0
right = max(li)*2

while True:
    mid = (left+right) // 2
    count = 0
    for item in li:
        count += item//mid

    if left > right:
        print(mid)
        break
    elif count >= n:
        left = mid + 1
    elif count < n:
        right = mid - 1
