import sys
input = sys.stdin.readline


def find(s, t):
    i = 0
    for char in t:
        if char == s[i]:
                i += 1
        if i == len(s):
            return "Yes"
    return "No"


while True:
    try:
        line = input()
        s, t = line.split()
        print(find(s, t))

    except:
        break
