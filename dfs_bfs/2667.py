n = int(input())
li = []
count = 0
for i in range(n):
    temp = input()
    count += temp.count("1")
    li.append(list(map(int, temp)))

matrix = {}
for i in range(count):
    matrix[count] = []

