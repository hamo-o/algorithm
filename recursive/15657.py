n, r = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()


def dfs(pick, start):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(start, n):
        pick.append(n_list[i])
        dfs(pick, start)

        pick.pop()
        start = i + 1


dfs([], 0)