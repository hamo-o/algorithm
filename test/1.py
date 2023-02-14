import sys
import heapq
n, k = map(int, input().split())

# 최단거리 저장
INF = sys.maxsize
memo = [INF]*100002

# 최단거리 방문 노드들 저장
heap = []


def dijkstra(start):
    memo[start] = 0
    heapq.heappush(heap, (start, 0))

    while heap:
        cur_node, prev_weigh = heapq.heappop(heap)

        if memo[cur_node] < prev_weigh:
            continue

        for i in range(3):
            if i == 0:
                next_node = cur_node - 1
                cur_weigh = 1
            elif i == 1:
                next_node = cur_node + 1
                cur_weigh = 1
            else:
                next_node = cur_node * 2
                cur_weigh = 1

            if 0 <= next_node <= 100000:
                next_weigh = prev_weigh + cur_weigh

                if next_weigh < memo[next_node]:
                    memo[next_node] = next_weigh
                    heapq.heappush(heap, (next_node, next_weigh))


if k <= n:
    print(n-k)
else:
    dijkstra(n)
    print(memo[k])
