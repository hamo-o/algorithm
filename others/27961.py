# 생성 마법 - 고양이 1마리를 집에 생성
# 복제 마법 - k마리 존재한다면 0~k마리 고양이 추가 가능
# 정확히 n마리 고양이?!

n = int(input())

if n == 0:
    print(0)
else:
    cats = 1
    answer = 1
    while cats < n:
        cats += min(cats, n-cats)
        answer += 1

    print(answer)
