n = list(map(int, input()))

if (sum(n) % 3 == 0) and (0 in n):
    n.sort(key=lambda x: -x)
    print("".join(list(map(str, n))))
else:
    print(-1)
