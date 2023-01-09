import heapq
import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
else:
    heap = []
    for i in range(n):
        line = map(int, input().split())
        for item in line:
            if len(heap) > n:
                heapq.heappop(heap)
            heapq.heappush(heap, item)

    heapq.heappop(heap)
    heap.sort()

    print(heap[0])

# cols = []
# for i in range(n):
#     temp = []
#     for j in range(n):
#         temp.append(li[j][i])
#     cols.append(temp)

