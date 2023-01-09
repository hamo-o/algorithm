import heapq

n = int(input())
heap = []

for _ in range(n):
    k = list(map(int, input().split()))
    if k[0] == 0:
        if heap:
            print(-heap[0])
            heapq.heappop(heap)
        else:
            print(-1)
    else:
        for i in range(1, k[0]+1):
            heapq.heappush(heap, -k[i])
