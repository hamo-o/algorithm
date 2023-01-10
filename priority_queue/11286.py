import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    k = int(input())

    if k == 0:
        if heap:
            num = heapq.heappop(heap)
            print(num[1])
        else:
            print(0)
    else:
        if k > 0:
            heapq.heappush(heap, (k, k))
        else:
            heapq.heappush(heap, (-k, k))

