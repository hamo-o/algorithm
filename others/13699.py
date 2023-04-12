n = int(input())

memo = [0 for _ in range(36)]

memo[0] = 1
memo[1] = 1

for i in range(2, n+1):
    for j in range(i):
        memo[i] += memo[j]*memo[i-j-1]

print(memo[n])

# t(3) = t(0)*t(2) + t(1)*t(1) + t(2)*t(0)
# t(4) = t(0)*t(3) + t(1)*t(2) + t(2)*t(1) + t(3)*t(0)
# t(4) = t(0)*t(3) + t(1)*t(2) + t(2)*t(1) + t(3)*t(0)
