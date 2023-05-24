from collections import deque
import sys
input = sys.stdin.readline

n, W = map(int, input().split())
visited = [0]*(n+1)
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))


def promising(idx, weight, profit, max_profit):
    total_weight = weight
    b = profit

    if weight >= W:
        return False
    else:
        j = idx+1
        while j < n and total_weight + items[j][0] <= W:
            total_weight += items[j][0]
            b += items[j][1]
            j += 1
        if j < n:
            b += (W-total_weight)*items[j][1]/items[j][0]

        return b > max_profit


def dfs(i, p, w, max_p):
    if w <= W and p > max_p:
        max_p = p
        results.append(max_p)

    if promising(i, w, p, max_p):
        visited[i+1] = 1
        dfs(i+1, p+items[i+1][1], w+items[i+1][0], max_p)
        visited[i+1] = 0
        dfs(i+1, p, w, max_p)


def bound(i, weight, profit):
    total_weight = weight
    b = profit
    if weight >= W:
        return 0
    else:
        j = i+1
        while j < n and total_weight + items[j][0] <= W:
            total_weight += items[j][0]
            b += items[j][1]
            j += 1
        if j < n:
            b += (W-total_weight)*items[j][1]/items[j][0]

        return b


def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    max_p = 0
    while queue:
        cur = queue.popleft()
        idx = cur[0] + 1
        weight = cur[1] + items[idx][0]
        profit = cur[2] + items[idx][1]
        if weight <= W and profit > max_p:
            max_p = profit
        if bound(idx, weight, profit) > max_p:
            queue.append([idx, weight, profit])
        weight = cur[1]
        profit = cur[2]
        if bound(idx, weight, profit) > max_p:
            queue.append([idx, weight, profit])

    return max_p


results = []
dfs(0, 0, 0, 0)
print(max(results))
print(bfs())
