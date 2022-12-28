def bubble_sort(p):
    for i in range(n-1):
        for j in range(n-i-1):
            if p[j+1] < p[j]:
                p[j+1], p[j] = p[j], p[j+1]


n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

bubble_sort(num_list)

for i in num_list:
    print(i)