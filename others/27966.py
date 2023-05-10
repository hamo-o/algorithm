n = int(input())
answer = n-1 + (n-2)*(n-1)
print(answer)
for i in range(2, n+1):
    print(1, i)
