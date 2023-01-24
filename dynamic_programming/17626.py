n = int(input())


def memo_square():
    memo = [0]*(n+1)
    squares = []

    for i in range(1, n+1):
        if i**2 <= n:
            memo[i**2] = 1
        if memo[i]:
            squares.append(i)
        else:
            memo[i] = min(memo[i-square] for square in squares) + 1

    return memo[n]


print(memo_square())
