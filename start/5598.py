str = input()

for i in str:
    if ord(i) > ord('C'):
        print(chr(ord(i)-3), end="")
    else:
        print(chr(ord(i)+23), end="")