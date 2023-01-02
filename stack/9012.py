t = int(input())

def checkVPS(l):
    n = len(l)

    while "(" and ")" in l:
        if li[0] == "(":
            i = 0
            while l[i] == "(":
                i += 1
            l.pop(i)
            l.pop(0)
        else:
            break

    if l:
        print("NO")
    else:
        print("YES")


for i in range(t):
    li = list(input())
    checkVPS(li)
