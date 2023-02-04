# 라이언 인형 1
# 어피치 인형 2
# 1이 k개 이상 있는 가장 작은 연속된 집합

n, k = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = 0
length = 1

if li[start] == 1:
    count = 1
else:
    count = 0

while end < n:
    if count >= k:
        if start == 0:
            min_length = length
        else:
            min_length = min(length, min_length)

        if li[start] == 1:
            count -= 1

        start += 1
        length -= 1
    else:
        if start == 0 and end == n-1:
            print(-1)
            break
        else:
            end += 1
            if end < n and li[end] == 1:
                count += 1

            length += 1


print(min_length)
