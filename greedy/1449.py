n, l = map(int, input().split())
spot = list(map(int, input().split()))
gap = []

spot.sort()

for i in range(n-1):
    gap.append(spot[i+1]-spot[i])

cnt = 0
temp = 0
for i in range(n-1):
    temp += gap[i]
    if temp + 1 > l:
        cnt += 1
        temp = 0

cnt += 1

print(cnt)
