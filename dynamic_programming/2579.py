n = int(input())
li = []
for i in range(n):
    li.append(int(input()))


def memo_stairs():
    memo = [0]*n

    memo[0] = li[0]
    if n > 1:
        memo[1] = li[0] + li[1]

        for i in range(2, n):
            memo[i] = max(li[i] + li[i-1] + memo[i-3], li[i] + memo[i-2])

    return memo[n-1]


print(memo_stairs())
