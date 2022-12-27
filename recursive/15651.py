# DFS를 이용한 중복순열 구현

n, r = map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(i+1)


def comb(pick):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(n):
        pick.append(num_list[i])

        comb(pick)

        pick.pop()


comb([])