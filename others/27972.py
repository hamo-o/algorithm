# 1 ~ N 정수 중 하나 쓴다
# 직전에 연주한 음이 현재 연주할 음보다 낮으면 직전 수보다 큰 수 쓰기
# 반대면 직전 수보다 작은 수 쓰기
# 같으면 직전에 쓴 수 쓰기

m = int(input())
song = list(map(int, input().split()))

if m == 1:
    print(1)
else:
    n = 1
    max_n = 1
    state = song[0] < song[1]
    for i in range(m-1):
        if not state:
            if song[i] > song[i+1]:
                n += 1
                max_n = max(n, max_n)
            elif song[i] < song[i+1]:
                state = 1
                n = 2
        else:
            if song[i] > song[i+1]:
                state = 0
                n = 2
            elif song[i] < song[i+1]:
                n += 1
                max_n = max(n, max_n)

    print(max_n)



