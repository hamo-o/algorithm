x, y = map(int, input().split())
z = (100*y) // x

left = y
right = x
while True:
    mid = (left+right) // 2

    if x == y:
        print(-1)
        break
    elif left > right:
        print(mid-y+1)
        break
    elif (100*mid) // (x+mid-y) == z:
        left = mid + 1
    else:
        right = mid - 1
