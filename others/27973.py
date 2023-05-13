import sys
input = sys.stdin.readline

# 일반항 = a + (n-1)d
# 계속 같은 수를 더하거나 곱해서 만들어짐. -> 등차수열

# 초항
a = 1
# 공차
d = 1
# 몇번째 항?
n = 1

q = int(input())
for _ in range(q):
    oper = input().strip()
    if int(oper[0]) == 0:
        a += int(oper[2:])
    elif int(oper[0]) == 1:
        a *= int(oper[2:])
        d *= int(oper[2:])
    elif int(oper[0]) == 2:
        n += int(oper[2:])
    else:
        print(a+(n-1)*d)
