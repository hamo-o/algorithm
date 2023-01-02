n = int(input())
s = []
cnt = 0

for i in range(n):
    s.append(input())

for item in s:
    stack = []

    for i in range(len(item)):
        if len(stack) > 0 and stack[-1] == item[i]:
            stack.pop()
        else:
            stack.append(item[i])

    if not stack:
        cnt += 1


print(cnt)
