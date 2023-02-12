import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

# 노드 v 간선 e
v, e = map(int, input().split())

# 시작 노드
k = int(input())

# 최단거리 저장
memo = [INF]*(v+1)

# 최단거리 방문 노드들 저장
heap = []

# graph[시작 노드] = [(가중치, 목적지 노드), (가중치, 목적지 노드)...]
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))


def dijkstra(start):
    # 나자신 가중치 0
    memo[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:

        # 도착한 노드가 다시 출발 하는 현재 노드가 됨
        prev_w, cur = heapq.heappop(heap)

        # 현재 저장 되어 있는 가중치가 더 작으면 걍 냅둬
        if memo[cur] < prev_w:
            continue

        # 출발지에서 도착할 수 있는 노드들 다 돌기
        for w, next in graph[cur]:
            next_w = w + prev_w

            # 다음 노드에 저장되어있는 가중치가 계산한 것보다 크면 갱신
            if next_w < memo[next]:
                memo[next] = next_w
                heapq.heappush(heap, (next_w, next))


dijkstra(k)

for i in range(1, v+1):
    if memo[i] == INF:
        print("INF")
    else:
        print(memo[i])
