n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

while True:
    mid = (left+right) // 2

    s = 0
    for tree in trees:
        if tree > mid:
            s += (tree - mid)

    if left > right:
        print(mid)
        break
    elif s == m:
        print(mid)
        break
    elif s > m:
        left = mid + 1
    else:
        right = mid - 1
