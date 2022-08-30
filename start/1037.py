num = int(input())
a = list(map(int, input().split()))
max = 1
min = a[0]

for i in a:
    if i > max:
        max = i
    if i < min:
        min = i

print(max * min)