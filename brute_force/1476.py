answer = list(map(int, input().split()))

num = 0
e = s = m = 0
while [e, s, m] != answer:
    num += 1
    e = num % 15
    s = num % 28
    m = num % 19
    if e == 0:
        e = 15
    if s == 0:
        s = 28
    if m == 0:
        m = 19

print(num)