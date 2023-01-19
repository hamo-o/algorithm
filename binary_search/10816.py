import sys
input = sys.stdin.readline

n = int(input())
my_cards = list(map(int, input().split()))
m = int(input())
origin_cards = list(map(int, input().split()))

cards = {}
for i in range(m):
    cards[origin_cards[i]] = 0
    origin_cards[i] = [origin_cards[i], i]

origin_cards.sort()
cards = dict(sorted(cards.items()))


for my_card in my_cards:
    left = 0
    right = m - 1

    while True:
        mid = (left+right)//2

        if left > right:
            break
        elif my_card == origin_cards[mid][0]:
            cards[my_card] += 1
            break
        elif my_card < origin_cards[mid][0]:
            right = mid - 1
        elif my_card > origin_cards[mid][0]:
            left = mid + 1


origin_cards.sort(key=lambda x: x[1])

for num in origin_cards:
    print(cards[num[0]], end=" ")


