import sys
input = sys.stdin.readline

n = int(input())

nums = []*n
for i in range(n):
    line = list(map(int, input().split()))
    nums.append(line)


def pooling(size, x, y):
    mid = size // 2

    if size == 2:
        answer = [nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        answer.sort()
        return answer[-2]

    left_top = pooling(mid, x, y)
    right_top = pooling(mid, x+mid, y)
    left_bottom = pooling(mid, x, y+mid)
    right_bottom = pooling(mid, x+mid, y+mid)
    answer = [left_top, right_top, left_bottom, right_bottom]
    answer.sort()
    return answer[-2]


print(pooling(n, 0, 0))





# def make_list(raw):
#     length = len(raw)
#     new = [[0 for _ in range(4)] for _ in range((length//2)**2)]
#
#     for i in range(length):
#         if i % 2 == 0:
#             for j in range(length//2):
#                 new[(length//4)*i+j][0] = raw[i][2*j]
#                 new[(length//4)*i+j][1] = raw[i][2*j+1]
#         else:
#             for j in range(length//2):
#                 new[(length//4)*(i-1)+j][2] = raw[i][2*j]
#                 new[(length//4)*(i-1)+j][3] = raw[i][2*j+1]
#
#     return new
#
#
# def choose_second(ans, raw):
#     temp = []
#     for item in raw:
#         item.sort()
#         temp.append(item[2])
#         if len(temp) == 4:
#             ans.append(temp)
#             temp = []
#
#     if len(ans) == 1:
#         print(ans[0][2])
#         return
#
#     choose_second([], make_list(ans))
#
#
# choose_second([], make_list(li))
