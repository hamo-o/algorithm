n = int(input())
li = list(map(int, input().split()))
total = int(input())

left = total // n
right = max(li)

while True:
    mid = (left+right) // 2
    s = 0
    for item in li:
        if item >= mid:
            s += mid
        else:
            s += item

    if left > right:
        print(mid)
        break
    elif s > total:
        right = mid - 1
    else:
        left = mid + 1

