import sys
input = sys.stdin.readline

matrix = []

n, b = map(int, input().split())
for i in range(n):
    matrix.append(list(map(int, input().split())))


# 슈트라센 알고리즘
def strassen(a):
    m1 = (a[0][0]+a[1][1]) * (a[0][0]+a[1][1])
    m2 = (a[1][0]+a[1][1]) * a[0][0]
    m3 = a[0][0] * (a[0][1] - a[1][1])
    m4 = a[1][1] * (a[1][0] - a[0][0])
    m5 = (a[0][0]+a[0][1]) * a[1][1]
    m6 = (a[1][0]-a[0][0]) * (a[0][0]+a[0][1])
    m7 = (a[0][1]-a[1][1]) * (a[1][0]+a[1][1])

    c = [[m1+m4-m5+m7, m3+m5], [m2+m4, m1+m3-m2+m6]]

    return c


def divide(size):
    if size == 1:
        return matrix
    elif size == 2:
        return strassen(matrix)

    if size % 2 == 0:
        strassen(divide(size//2))
    else:
        divide(size//2)


if n > 2:
    divide(b)

else:
    print(strassen(matrix))


