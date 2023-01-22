n = int(input())


# def recursive_fibo(num):
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return recursive_fibo(num-1)+recursive_fibo(num-2)


def memo_fibo(num):
    memo = [0] * n

    memo[0] = 1
    memo[1] = 1

    count = 0
    for i in range(2, num):
        memo[i] = memo[i-2] + memo[i-1]
        count += 1

    return f"{memo[num-1]} {count}"


print(memo_fibo(n))


