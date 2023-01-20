import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
temp.sort()

hands = {}
hands[temp[0]] = 1
start = temp[0]
i = 1
for i in range(1, n):
    if temp[i-1] == temp[i]:
        hands[start] += 1
    else:
        hands[temp[i]] = 1
        start = temp[i]


m = int(input())
cards = list(map(int, input().split()))


for card in cards:
    if card in hands:
        print(hands[card], end=" ")
    else:
        print(0, end=" ")



# 2

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# temp = list(map(int, input().split()))
# temp.sort()
#
# hands = [[temp[0], 1]]
# i = 1
# start = i - 1
# for i in range(1, n):
#     if temp[i-1] == temp[i]:
#         hands[start][1] += 1
#     else:
#         hands.append([temp[i], 1])
#         start += 1
#
#
# m = int(input())
# cards = list(map(int, input().split()))
#
#
# for card in cards:
#     left = 0
#     right = len(hands) - 1
#
#     while True:
#         mid = (left+right)//2
#
#         if left > right:
#             print(0, end=" ")
#             break
#         elif card == hands[mid][0]:
#             print(hands[mid][1], end=" ")
#             break
#         elif card > hands[mid][0]:
#             left = mid + 1
#         elif card < hands[mid][0]:
#             right = mid - 1



# 1

# cards = {}
# for i in range(m):
#     cards[origin_cards[i]] = 0
#     origin_cards[i] = [origin_cards[i], i]
#
# origin_cards.sort()
# cards = dict(sorted(cards.items()))
#
#
# for my_card in my_cards:
#     left = 0
#     right = m - 1
#
#     while True:
#         mid = (left+right)//2
#
#         if left > right:
#             break
#         elif my_card == origin_cards[mid][0]:
#             cards[my_card] += 1
#             break
#         elif my_card < origin_cards[mid][0]:
#             right = mid - 1
#         elif my_card > origin_cards[mid][0]:
#             left = mid + 1
#
#
# origin_cards.sort(key=lambda x: x[1])
#
# for num in origin_cards:
#     print(cards[num[0]], end=" ")
#
#
