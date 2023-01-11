import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(input()[:-1])

# 1이면 뒤집 0이면 안뒤집
min_cnt = 64
for i in range(n-7):
    new = chess[i:8+i]
    for j in range(m-7):
        start = 1
        black_li = []
        for line in new:
            line = line[j:8+j]
            flag = start
            for word in line:
                # 그 전이 W였다면
                if flag == 1:
                    if word == "B":
                        black_li.append(0)
                    else:
                        black_li.append(1)
                    flag = 0
                # 그 전이 B였다면
                else:
                    if word == "B":
                        black_li.append(1)
                    else:
                        black_li.append(0)
                    flag = 1

            start = not start

        cnt = min(black_li.count(1), black_li.count(0))
        if min_cnt > cnt:
            min_cnt = cnt

print(min_cnt)
