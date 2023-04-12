import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cups = []
for _ in range(n):
    cups.append(int(input()))

left = 0
if cups and sum(cups) >= k:
    right = max(cups)*2
else:
    right = 0

while True:
    mid = (left+right)//2
    if mid <= 0:
        print(0)
        break

    count = 0
    for cup in cups:
        count += cup//mid

    if left > right:
        print(mid)
        break
    elif count >= k:
        left = mid + 1
    else:
        right = mid - 1
