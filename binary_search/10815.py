import sys
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
target.sort()
m = int(input())
cards = list(map(int, input().split()))


for card in cards:
    left = 0
    right = n - 1

    while True:
        mid = (left+right)//2
        # left가 right보다 커질 경우 0 출력 (존재X), 종료
        if left > right:
            print(0, end=" ")
            break

        # 왼쪽 탐색
        elif target[mid] > card:
            right = mid - 1

        # 오른쪽 탐색
        elif target[mid] < card:
            left = mid + 1

        # 찾음! 1 출력, 탐색 종료
        elif target[mid] == card:
            print(1, end=" ")
            break

