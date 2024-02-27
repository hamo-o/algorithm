import sys
import heapq

input = sys.stdin.readline

times = []
n = int(input())
for i in range(n):
    times.append(list(map(int, input().split())))
times.sort(key = lambda x: (x[0], x[1]))

heap = []
cnt = 0
for i in range(n):
    [start, end] = times[i]
    if not heap or heap[0][0] > start:
        cnt += 1
    else:
        heapq.heappop(heap)
    
    heapq.heappush(heap, [end, start])

print(cnt)
