n = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

s = 0
i = 0
cheap_cost = costs[0]

for i in range(n-1):
    if cheap_cost > costs[i]:
        cheap_cost = costs[i]
    s += (cheap_cost * dists[i])

print(s)
