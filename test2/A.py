a, b = map(int, input().split())
k = abs(a-b)

if a == 1 or b == 1:
    print("1")

else:
    if k == 0:
        if a > b:
            k = b
        else:
            k = a

    if k < 10000001:
        print("1"*k)
