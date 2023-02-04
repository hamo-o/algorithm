# dna 문자열 길이 s
# 비밀번호로 사용할 부분문자열 길이 p
# A C G T의 최소 개수

s, p = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

start = 0
end = 0
length = 1
count = 0

temp = dna[start]
my_num = {"A": 0, "C": 0, "G": 0, "T": 0}
my_num[temp] += 1

while start <= s - p:
    if length == p:
        if my_num["A"] >= a and my_num["C"] >= c \
                and my_num["G"] >= g and my_num["T"] >= t:
            count += 1

        my_num[temp] -= 1
        length -= 1

        start += 1
        if start < s:
            temp = dna[start]
    else:
        end += 1
        my_num[dna[end]] += 1
        length += 1

print(count)

