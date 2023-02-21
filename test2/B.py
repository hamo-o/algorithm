key = input()
pwd = input()

n = len(key)
m = len(pwd) // n

board = [[i, key[i]] for i in range(n)]
board.sort(key=lambda x: x[1])

for i in range(len(pwd)):
    board[i // m].append(pwd[i])

board.sort(key=lambda x: x[0])

answer = []
for i in range(2, m+2):
    for line in board:
        answer.append(line[i])

print("".join(answer))
