n = int(input())
li = []
memo = [0]*n

for i in range(n):
    li.append(list(map(int, input().split())))


def memo_time():
    temp = [0]
    end = -1
    for i in range(n):
        for j in range(i+1):
            if li[j][0] == 1 and end < j:
                temp.append(li[j][1])
                end = i
            li[j][0] -= 1

        m = max(temp)
        if i == 0:
            memo[i] = m
        else:
            memo[i] = max(memo[i-1], sum(temp))

        print(memo, temp)
        print(li)

        # money = 0
        # j = 0
        # while j < i+1:
        #     if li[j][0] == i - j + 1 or 1:
        #         money += li[j][1]
        #         j += li[j][0]
        #     else:
        #         j += 1
        #
        # if i == 0:
        #     memo[i] = money
        # else:
        #     print(i, memo[i-1], money)
        #     memo[i] = max(memo[i-1], money)
        #
        # print(memo)


memo_time()

