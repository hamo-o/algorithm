def divide_sum(start, end):
    if start == end:
        return start

    mid = (start+end) // 2

    return divide_sum(start, mid) + divide_sum(mid+1, end)


n = int(input())
print(divide_sum(1, n))


# 1 2 3 4 5
# start 1 end 5

# 1 2 3
# start 1 end 3 -> 6 return

# 1 2
# start 1 end 2 -> 3 return
# 1 1
# start 1 end 1 -> 1 return
# 2 2
# start 2 end 2 -> 2 return

# 3 3
# start 3 end 3 -> 3 return


# 4 5
# start 4 end 5
