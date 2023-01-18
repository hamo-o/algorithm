n, r, c = map(int, input().split())


def divide(count, size, x, y):
    if size == 0:
        print(count)
        return

    if size <= x:
        if size <= y:
            count += (size**2) * 3
            divide(count, size//2, x-size, y-size)
        else:
            count += (size ** 2)
            divide(count, size//2, x-size, y)
    else:
        if size <= y:
            count += (size**2) * 2
            divide(count, size//2, x, y-size)
        else:
            divide(count, size//2, x, y)


divide(0, (2**n)//2, c, r)

