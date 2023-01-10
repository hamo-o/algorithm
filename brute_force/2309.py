li = []
for i in range(9):
    li.append(int(input()))

total = sum(li)


def main():
    for i in range(9):
        a = li[i]
        for j in range(i+1, 9):
            b = li[j]
            result = total - a - b
            if result == 100:
                li.remove(a)
                li.remove(b)
                return li


ans = main()
ans.sort()

for item in ans:
    print(item)

