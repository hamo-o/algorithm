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
    temps = []

    for i in range(n):
        money = 0
        if li[i][0] == 1:
            money += li[i][1]
        else:
            li[i][0] -= 1
            temps.append(li[i])

        if i == 0:
            memo[i] = money

        else:
            for temp in temps:
                if temp[0] == 1:
                    money += temp[1]

            memo[i] = memo[i-1] + money

        print(memo, temps)


memo_time()

