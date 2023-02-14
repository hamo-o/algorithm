n, m = map(int, input().split())


def dfs(pick):
    if len(pick) == m:
        print(" ".join(map(str, pick)))
        return

    for i in range(1, n+1):
        pick.append(i)
        dfs(pick)
        pick.pop()


dfs([])

