a, b = map(int, input().split())
k = abs(a-b)

if k == 0:
    if a > b:
        k = b
    else:
        k = a

print("1"*k)
