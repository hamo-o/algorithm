n, m = map(int, input().split())
first_list = [[0 for _ in range(m)] for _ in range(n)]
answer_list = [[0 for _ in range(m)] for _ in range(n)]
count = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    temp = input()
    for j in range(m):
        first_list[i][j] = int(temp[j])

for i in range(n):
    temp = input()
    for j in range(m):
        answer_list[i][j] = int(temp[j])

for i in range(n-2):
    for j in range(m-2):
        print(i, j)
        if first_list[i][j] != answer_list[i][j]:
            for k in range(3):
                for l in range(3):
                    count[i+k][j+l] += 1

print(count)
