import sys
input = sys.stdin.readline

n = int(input())
scores = {}
people = []
min_score = 99
for i in range(n):
    people.append(i+1)
    temp = list(map(int, input().split()))
    for j in range(n):
        if i != j:
            scores[(i+1, j+1)] = temp[j]


def find_score(pick, visited, base, score):
    if len(pick) == 2:
        score.append(scores[tuple(pick)])
        return

    for i in base:
        if not visited[i-1]:
            pick.append(i)
            visited[i-1] = 1
            find_score(pick, visited, base, score)

            pick.pop()
            visited[i-1] = 0


def dfs(pick, visited):
    if len(pick) == n//2:
        start.append(pick)
        start_score = []
        link_score = []
        find_score([], [0]*n, tuple(pick), start_score)
        find_score([], [0] * n, tuple(set(people) - set(pick)), link_score)
        new = sum(start_score) - sum(link_score)

        global min_score
        if abs(new) < min_score:
            min_score = abs(new)
        return

    for i in range(1, n):
        if not visited[i] and pick[-1] < i+1:
            pick.append(i+1)
            visited[i] = 1
            dfs(pick, visited)

            pick.pop()
            visited[i] = 0


start = []
dfs([1], [0]*n)

print(min_score)
