import sys
input = sys.stdin.readline

n = int(input())
times = []

for i in range(n):
    times.append(tuple(map(int, input().split())))

times.sort()

end = times[0][1]
times.pop(0)
cnt = 0
i = 0
while times:
    if times[i] == times[-1]:
        end = times[0][1]
        times.pop(i)
        i = 0
        cnt += 1
    else:
        if end <= times[i][0]:
            end = times[i][1]
            times.pop(i)
        else:
            i += 1


print(cnt)
