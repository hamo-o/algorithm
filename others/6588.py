import sys
input = sys.stdin.readline

n = []
for i in range(1000001):
    if i % 2 == 0 or i == 1:
        n.append(0)
    else:
        n.append(i)

for i in range(2, int(1000001**0.5)+1):
    if n[i]:
        for j in range(2*i, 1000001, i):
            n[j] = 0


def find_num(num):
    start = 3
    end = num-1
    while n[end] == 0:
        end -= 2

    while start <= end:
        if start+end == num:
            return start, end
        elif start+end > num:
            end -= 2
            while n[end] == 0:
                end -= 2
        else:
            start += 2
            while n[start] == 0:
                start += 2

    return 0, 0


while True:
    k = int(input())
    if k == 0:
        break
    else:
        x, y = find_num(k)
        if x and y:
            print(k, "=", x, "+", y)
        else:
            print("Goldbach's conjecture is wrong.")
