s = []

while True:
    line = input()

    if line == ".":
        break
    else:
        s.append(line)

for item in s:
    stack = []
    i = 0
    while item[i] != ".":
        if item[i] == "(" or item[i] == "[":
            stack.append(item[i])
        elif stack:
            if stack[-1] == "(" and item[i] == ")":
                stack.pop()
            elif stack[-1] == "[" and item[i] == "]":
                stack.pop()
            elif item[i] == ")" or item[i] == "]":
                stack.append(item[i])
        elif item[i] == ")" or item[i] == "]":
            stack.append(item[i])
            break
        i += 1

    if stack:
        print("no")
    else:
        print("yes")


