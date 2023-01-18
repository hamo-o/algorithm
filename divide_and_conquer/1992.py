import sys
input = sys.stdin.readline

n = int(input())

videos = []
for i in range(n):
    temp = []
    line = input().strip()
    for item in line:
        temp.append(int(item))
    videos.append(temp)


def divide(size, x, y):
    if size == 1:
        return videos[x][y]

    mid = size // 2

    lt = divide(mid, x, y)
    rt = divide(mid, x+mid, y)
    lb = divide(mid, x, y+mid)
    rb = divide(mid, x+mid, y+mid)

    if lt == rt == lb == rb and type(lt) == int:
        return lt
    else:
        return f"({lt}{lb}{rt}{rb})"


answer = divide(n, 0, 0)
print(answer)
