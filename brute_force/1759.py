l, c = map(int, input().split())
alp = list(map(str, input().split()))
alp.sort()


def check_alp(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return 1
    else:
        return 0


def dfs(pick, visited, check):
    if len(pick) == l and check[0] >= 1 and check[1] >= 2:
        print("".join(pick))

    for i in range(c):
        if not visited[i] and (not pick or pick[-1] < alp[i]):
            if check_alp(alp[i]):
                check[0] += 1
            else:
                check[1] += 1

            pick.append(alp[i])
            visited[i] = 1
            dfs(pick, visited, check)

            pick.pop()
            visited[i] = 0
            if check_alp(alp[i]):
                check[0] -= 1
            else:
                check[1] -= 1


dfs([], [0]*c, [0, 0])

