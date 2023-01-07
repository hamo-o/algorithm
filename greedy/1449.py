n, l = map(int, input().split())
spot = list(map(int, input().split()))
gap = []

spot.sort()

for i in range(n-1):
    gap.append(spot[i+1]-spot[i])

print(gap)
