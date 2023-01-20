import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    answer = set(map(int, input().split()))

    m = int(input())
    hands = list(map(int, input().split()))

    for hand in hands:
        if hand in answer:
            print(1)
        else:
            print(0)

    # for hand in hands:
    #     left = 0
    #     right = n - 1
    #
    #     while True:
    #         mid = (left+right)//2
    #
    #         if left > right:
    #             print(0)
    #             break
    #         elif hand == answer[mid]:
    #             print(1)
    #             break
    #         elif hand > answer[mid]:
    #             left = mid + 1
    #         elif hand < answer[mid]:
    #             right = mid - 1
