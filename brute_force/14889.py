n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, input().split())))


def dfs(start_cnt, link_cnt):
    if visited.count(1) == n//2:
        print(start_cnt)
        return

    for i in range(n):
        for j in range(n):
            if i != j and not visited[i] and not visited[j]:
                visited[i] = visited[j] = 1
                start_cnt += (li[i][j] + li[j][i])
                dfs(start_cnt, 0)
                visited[i] = 0
                visited[j] = 0
                start_cnt = 0


visited = [0]*n
dfs(0, 0)
