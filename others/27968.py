import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candy = list(map(int, input().split()))
candies = []
s = 0
for c in candy:
    s += c
    candies.append(s)

for i in range(n):
    k = int(input())

    if k > candies[m-1]:
        print("Go away!")
    else:
        left = 0
        right = m-1
        while True:
            mid = (left+right)//2
            outs = candies[mid]

            if left > right:
                print(mid+2)
                break
            if outs == k:
                print(mid+1)
                break
            elif outs < k:
                left = mid + 1
            else:
                right = mid - 1

