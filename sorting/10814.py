# 나이순
# 나이 같으면 입력순
import sys
input = sys.stdin.readline

n = int(input())
li = []*n

for i in range(n):
    age, name = input().split()
    age = int(age)
    li.append([age, name])

li.sort(key=lambda x: x[0])

for item in li:
    print(item[0], item[1])
