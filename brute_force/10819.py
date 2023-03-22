results = []

n = int(input())
num = list(map(int, input().split()))
visited = [False for i in range(n)]
pick = []


def dfs():
    if len(pick) == n:
        s = 0
        for k in range(n-1):
            s += abs(pick[k]-pick[k+1])

        results.append(s)

    for i in range(n):
        if not visited[i]:
            pick.append(num[i])
            visited[i] = True
            dfs()
            pick.pop()
            visited[i] = False


dfs()
print(max(results))
