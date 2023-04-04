c, h = map(int, input().split())
total_time = 60*60*24
train_time_up = []
train_time_down = []

for _ in range(c):
    hh, mm, ss = map(int, input().split(":"))
    time_cnt = 0
    time_cnt += (hh - 5) * 3600
    time_cnt += mm * 60
    time_cnt += ss
    train_time_up.append(time_cnt)

for _ in range(h):
    hh, mm, ss = map(int, input().split(":"))
    time_cnt = 0
    time_cnt += (hh - 5) * 3600
    time_cnt += mm * 60
    time_cnt += ss
    train_time_down.append(time_cnt)

total_time -= (c+h)*40

for i in range(c):
    for j in range(h):
        same_time = train_time_up[i]-train_time_down[j]
        if abs(same_time) < 40:
            total_time += (40-abs(same_time))

print(total_time)
