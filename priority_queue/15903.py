# 가장 작은 수부터 합치기!!

import heapq

n, m = map(int, input().split())

cards = list(map(int, input().split()))

heapq.heapify(cards)

for i in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    heapq.heappush(cards, a + b)
    heapq.heappush(cards, a + b)

print(sum(cards))
