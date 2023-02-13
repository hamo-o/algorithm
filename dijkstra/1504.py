import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

u, v = map(int, input().split())


def dij(start, end):
    memo = [INF] * (n + 1)
    heap = []
    memo[start] = 0
    heapq.heappush(heap, (start, 0))

    while heap:
        cur_node, prev_weigh = heapq.heappop(heap)

        if memo[cur_node] < prev_weigh:
            continue

        for next_node, cur_weigh in graph[cur_node]:
            next_weigh = prev_weigh + cur_weigh

            if next_weigh < memo[next_node]:
                memo[next_node] = next_weigh
                heapq.heappush(heap, (next_node, next_weigh))

    return memo[end]


answer = min(dij(1, u)+dij(u, v)+dij(v, n), dij(1, v)+dij(v, u)+dij(u, n))
if answer >= INF:
    print(-1)
else:
    print(answer)
