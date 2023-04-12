from itertools import product

k, n = map(int, input().split())
li = list(product([-1, 1], repeat=n))

result = len(li)
for nums in li:
    height = -k
    for num in nums:
        height += num
        if height >= 0:
            result -= 1
            break

print(result)
