x, y = map(int, input().split())
z = (100*y) // x

left = y
right = 2000000000
while True:
    mid = (left+right) // 2

    if z >= 99:
        print(-1)
        break
    elif left > right:
        print(mid-y+1)
        break
    elif (100*mid) // (x+mid-y) == z:
        left = mid + 1
    else:
        right = mid - 1
