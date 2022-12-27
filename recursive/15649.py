# DFS를 이용한 순열 구현

n, r = map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(i+1)

visited = [0] * len(num_list)


def comb(pick, visited):
    if len(pick) == r:
        print(" ".join(map(str, pick)))
        return

    for i in range(n):
        if not visited[i]:
            pick.append(num_list[i])
            visited[i] = 1

            comb(pick, visited)

            visited[i] = 0
            pick.pop()

comb([], visited)