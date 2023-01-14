n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

li = []
for i in range(4):
    op = operator[i]
    for j in range(op):
        li.append(i+1)
l = len(li)


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a < 0:
        ans = -((-a) // b)
    else:
        ans = a // b
    return ans


# [1 2 3 4]
# [1 1 1 1]
# 등등의 배열을 계속 주고..
# 1 add 2 sub 3 mul 4 div 처리


def cal(num_li, op_li):
    result = num_li[0]
    for k, v in enumerate(op_li):
        if v == 1:
            result = add(result, num_li[k+1])
        elif v == 2:
            result = sub(result, num_li[k+1])
        elif v == 3:
            result = mul(result, num_li[k+1])
        else:
            result = div(result, num_li[k+1])
    return result


def dfs(pick, visited):
    if len(pick) == l:
        ans_li.append(tuple(pick))
        return

    for i in range(l):
        if visited[i] == 0:
            pick.append(li[i])
            visited[i] = 1
            dfs(pick, visited)

            pick.pop()
            visited[i] = 0


ans_li = []
dfs([], [0]*l)
ans_li = list(set(ans_li))

result = []
for ans in ans_li:
    result.append(cal(num, ans))

result.sort()
print(result[-1])
print(result[0])