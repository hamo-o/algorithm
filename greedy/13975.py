import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))

    sorted_files = []
    for file in files:
        heapq.heappush(sorted_files, file)

    costs = 0
    while len(sorted_files) > 1:
        cost = heapq.heappop(sorted_files) + heapq.heappop(sorted_files)
        costs += cost
        heapq.heappush(sorted_files, cost)

    print(costs)
