# 6이 적어도 3개이상 연속으로 들어가는 수 == 종말의 숫자

n = int(input())

num = 666
six = []
while len(six) != n:
    s_num = str(num)
    if "666" in s_num:
        six.append(s_num)
    num += 1

print(int(six[-1]))
