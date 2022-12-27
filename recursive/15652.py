n, r = map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(i+1)


def dfs(pick, start):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(start, n):
        pick.append(num_list[i])
        dfs(pick, start)

        pick.pop()
        start += 1


dfs([], 0)