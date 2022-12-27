# DFS를 이용한 조합 구현

n, r = map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(i+1)


def comb(pick, first):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(first, n):
        pick.append(num_list[i])

        comb(pick, first + 1)

        pick.pop()
        first = i + 1


comb([], 0)
