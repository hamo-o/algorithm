lines = input()

s = 0
num = []
minus = 1

for line in lines:
    if line == "-":
        s += int("".join(num))*minus
        num = []
        minus = -1
    elif line == "+":
        s += int("".join(num))*minus
        num = []
    else:
        num.append(line)

s += int("".join(num))*minus

print(s)
