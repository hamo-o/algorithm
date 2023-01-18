a, b, c = map(int, input().split())


def divide(size, num):
    if size == 1:
        return num

    temp = divide(size // 2, num) % c
    if size % 2 == 0:
        return temp * temp
    else:
        return temp * temp * num


print(divide(b, a)%c)

# (a * b) % c = (a%c * b%c) % c 이걸 어케알아 ..

