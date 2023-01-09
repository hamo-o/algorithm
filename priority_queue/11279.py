import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    k = int(input())
    if k > 0:
        heapq.heappush(heap, -k)
    else:
        if heap:
            print(-heap[0])
            heapq.heappop(heap)
        else:
            print(0)
