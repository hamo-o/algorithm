import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    k = int(input())

    if k > 0:
        heapq.heappush(heap, k)
    else:
        if heap:
            print(heap[0])
            heapq.heappop(heap)
        else:
            print(0)

# 직접 힙 구현
# heap = [0]
# for i in range(n):
#     k = int(input())
#
#     if k > 0:
#         heap.append(k)
#         k_idx = len(heap) - 1
#
#         # 부모보다 k가 더 작으면
#         while k < heap[k_idx//2]:
#             heap[k_idx], heap[k_idx//2] = heap[k_idx//2], heap[k_idx]
#             k_idx = k_idx//2
#
#     else:
#         if len(heap) > 1:
#             print(heap[1])
#             heap[-1], heap[1] = heap[1], heap[-1]
#             heap.pop()
#
#             # 자식보다 부모가 더 크면
#             if len(heap) > 3:
#                 item = heap[1]
#                 item_idx = 1
#                 while item > heap[item_idx*2] or item > heap[item_idx*2+1]:
#                     if item > heap[item_idx*2]:
#                         heap[item_idx], heap[item_idx*2] = heap[item_idx*2], heap[item_idx]
#                         item_idx = item_idx*2
#                     elif item > item > heap[item_idx*2+1]:
#                         heap[item_idx], heap[item_idx*2+1] = heap[item_idx*2+1], heap[item_idx]
#                         item_idx = item_idx*2+1
#             elif len(heap) == 3:
#                 item = heap[1]
#                 item_idx = 1
#                 if item > heap[item_idx * 2]:
#                     heap[item_idx], heap[item_idx * 2] = heap[item_idx * 2], heap[item_idx]
#                     item_idx = item_idx * 2
#         else:
#             print(0)

