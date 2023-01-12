import sys
input = sys.stdin.readline

n = int(input())

li = []*n
for i in range(n):
    line = list(map(int, input().split()))
    li.append(line)


def make_list(raw):
    length = len(raw)
    new = [[0 for _ in range(4)] for _ in range((length//2)**2)]

    for i in range(length):
        if i % 2 == 0:
            for j in range(length//2):
                new[(length//4)*i+j][0] = raw[i][2*j]
                new[(length//4)*i+j][1] = raw[i][2*j+1]
        else:
            for j in range(length//2):
                new[(length//4)*(i-1)+j][2] = raw[i][2*j]
                new[(length//4)*(i-1)+j][3] = raw[i][2*j+1]

    return new


def choose_second(ans, raw):
    temp = []
    for item in raw:
        item.sort()
        temp.append(item[2])
        if len(temp) == 4:
            ans.append(temp)
            temp = []

    if len(ans) == 1:
        print(ans[0][2])
        return

    choose_second([], make_list(ans))


choose_second([], make_list(li))
