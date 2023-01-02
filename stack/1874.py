import sys
input = sys.stdin.readline

n = int(input())
seq = []
num = []
answer = []
flag = 0

for i in range(n):
    seq.append(int(input()))
    num.append(i+1)


def make_seq():
    stack = []

    j = 0
    for i in range(n):
        stack.append(num[i])
        answer.append("+")

        while stack and stack[-1] == seq[j]:
            j += 1
            stack.pop()
            answer.append("-")

        if 0 < j < n and seq[j - 1] > seq[j]:
            return 0

    return 1


if n < seq[0] or make_seq() == 0:
    print("NO")
else:
    for item in answer:
        print(item)

