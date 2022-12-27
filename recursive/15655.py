n, r = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()


def dfs(pick, start):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(start, n):
        if num_list[i] not in pick:
            pick.append(num_list[i])
            dfs(pick, start)

            pick.pop()
            start = i + 1

dfs([], 0)