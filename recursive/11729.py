n = int(input())
l_list = []


def move(fr, by, to, num, l):
    if num == 1:
        l.append((fr, to))
        return

    else:
        move(fr, to, by, num - 1, l)
        l.append((fr, to))
        move(by, fr, to, num - 1, l)


move(1, 2, 3, n, l_list)

print(len(l_list))
for i in l_list:
    print(" ".join(map(str, i)))