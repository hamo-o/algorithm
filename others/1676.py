n = int(input())


def fac(num):
    if num <= 1:
        return 1

    return num * fac(num-1)


def find_zero(li):
    for k, v in enumerate(li):
        if v != "0":
            return k


fac_str = str(fac(n))
print(find_zero(list(reversed(fac_str))))
