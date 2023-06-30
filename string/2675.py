t = int(input())
for _ in range(t):
    r, s = input().split()
    answer = ""

    for alpha in s:
        answer += (alpha*int(r))
    print(answer)
