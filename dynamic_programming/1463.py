n = int(input())


def memo_make_n():
    memo = [0]*(n+1)

    memo[2] = 1
    memo[3] = 1
    for i in range(4, n+1):
        temp = []
        if i % 2 == 0:
            temp.append(memo[i//2])
        if i % 3 == 0:
            temp.append(memo[i//3])
        temp.append(memo[i-1])

        memo[i] = min(temp) + 1

    return memo[n]


if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    print(memo_make_n())
