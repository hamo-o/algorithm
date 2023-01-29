# 1일의 최대이익 0, 3일뒤 10
# 2일의 최대이익 0, 5일뒤 20
# 3일의 최대이익 10
# 4일의 최대이익 3(10)+10+20 = 40
# 5일의 최대이익 4(40)
# 6일의 최대이익 5(40) + 15

n = int(input())
li = []
memo = [0]*n

for i in range(n):
    li.append(list(map(int, input().split())))


def memo_time():
    for i in range(n):
        money = 0
        j = 0
        while j < i+1:
            if li[j][0] == i - j + 1 or 1:
                money += li[j][1]
                j += li[j][0]
            else:
                j += 1

        if i == 0:
            memo[i] = money
        else:
            print(i, memo[i-1], money)
            memo[i] = max(memo[i-1], money)

        print(memo)


memo_time()

