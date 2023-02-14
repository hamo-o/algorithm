import sys
input = sys.stdin.readline

while True:
    try:
        line = input()
        if line == "\n":
            break
        s, t = line.split()
        start = t.find(s[0])

        if start != -1:
            i = 1
            for char in t:
                if char == s[i]:
                    i += 1
                if i == len(s):
                    break
            if i == len(s):
                print("Yes")
            else:
                print("No")

        else:
            print("No")
    except EOFError:
        break
