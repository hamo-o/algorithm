n, r = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()


def dfs(pick):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(n):
        if num_list[i] not in pick:
            pick.append(num_list[i])
            dfs(pick)

            pick.pop()


dfs([])