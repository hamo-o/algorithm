n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p_a = 0
p_b = 0
answer = []

while len(answer) < n+m:
    if p_a == n:
        answer.append(b[p_b])
        p_b += 1
    elif p_b == m:
        answer.append(a[p_a])
        p_a += 1
    elif a[p_a] < b[p_b]:
        answer.append(a[p_a])
        p_a += 1
    else:
        answer.append(b[p_b])
        p_b += 1


print(" ".join(map(str, answer)))

