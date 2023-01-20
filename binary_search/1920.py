n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
hands = list(map(int, input().split()))

for hand in hands:
    left = 0
    right = n - 1

    while True:
        mid = (left+right)//2

        if left > right:
            print(0)
            break
        elif hand == cards[mid]:
            print(1)
            break
        elif hand > cards[mid]:
            left = mid + 1
        elif hand < cards[mid]:
            right = mid - 1
