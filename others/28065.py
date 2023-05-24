# SW 수열이란?
# 1~N 사이의 서로 다른 정수로 이루어짐
# |현재항 - 이전항| > |다음항 - 현재항|
# 점점 갈수록 차이가 줄어들어야 함
# 가장 큰 숫자 - 가장 작은 숫자 - 가장 큰 숫자 - 가장 작은 숫자 ...
from collections import deque

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

answer = []
while queue:
    answer.append(queue[-1])
    queue.pop()
    if queue:
        answer.append(queue[0])
        queue.popleft()

print(" ".join(map(str, answer)))
