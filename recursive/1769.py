def add(x, count):
    if len(x) > 1:
        result = 0
        for i in x:
            result += int(i)
        add(str(result), count+1)
    else:
        print(count)
        if (int(x) % 3 == 0):
            print("YES")
        else:
            print("NO")

x = input()

add(x, 0)
