# 사전순으로 정렬
# 현재 문자와 다음 문자가 같으면 현재 문자를 prev 배열 맨 뒤에 넣기
# 다음 문자는 next 배열 맨 앞에 넣기
# 시작 + 2

# 다르면 시작 + 1

# AAABB
# A ABB A
# AB A BA

# AAAABBC
# A AABBC A
# AA BBC AA
# AAB C BAA

from collections import deque

s = list(input())
prev = []
next = deque()

s.sort()

i = 0
while len(s)-1 > i:
    if s[i] == s[i+1]:
        prev.append(s[i])
        next.appendleft(s[i+1])
        s.pop(i)
        s.pop(i)
    else:
        i += 1

if len(s) <= 1:
    print("".join(map(str, prev+s+list(next))))
else:
    print("I'm Sorry Hansoo")