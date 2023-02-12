import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

# 출발, 도착, 비용
for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

memo = [INF]*(n+1)
heap = []


def dij(first):
    memo[first] = 0
    heapq.heappush(heap, (first, 0))

    while heap:
        cur_node, prev_weigh = heapq.heappop(heap)

        if memo[cur_node] < prev_weigh:
            continue

        for next_node, cur_weigh in graph[cur_node]:
            next_weigh = prev_weigh + cur_weigh

            if next_weigh < memo[next_node]:
                memo[next_node] = next_weigh
                heapq.heappush(heap, (next_node, next_weigh))


dij(start)

print(memo[end])

