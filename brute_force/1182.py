n, s = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

li = []


def dfs(pick, visited, k, last):
    if len(pick) == k:
        return

    for i in range(n):
        if not visited[i] and (not pick or last < i):
            pick.append(num[i])
            visited[i] = 1

            if sum(pick) == s:
                li.append(tuple(pick))

            dfs(pick, visited, k+1, i)

            pick.pop()
            visited[i] = 0


dfs([], [0] * n, 1, 0)

print(len(li))


# def dfs(pick, visited, k):
#     if len(pick) == k:
#         if sum(pick) == s:
#             li.append(tuple(pick))
#         return
#
#     for i in range(n):
#         if not visited[i] and (not pick or pick[-1] < num[i]):
#             pick.append(num[i])
#             visited[i] = 1
#
#             dfs(pick, visited, k)
#
#             pick.pop()
#             visited[i] = 0
#
#
# cnt = 0
# for i in range(n):
#     li = []
#     dfs([], [0] * n, i+1)
#     cnt += len(li)
#
# print(cnt)