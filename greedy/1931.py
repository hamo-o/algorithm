import sys
input = sys.stdin.readline

n = int(input())
times = []

for i in range(n):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

end = times[0][1]
cnt = 1
times.pop(0)

for time in times:
    if end <= time[0]:
        cnt += 1
        end = time[1]

print(cnt)
