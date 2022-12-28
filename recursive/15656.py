n, r = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()


def dfs(pick):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(n):
        pick.append(n_list[i])
        dfs(pick)
        pick.pop()


dfs([])
