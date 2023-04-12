import sys
input = sys.stdin.readline

line = input()
cups = ["s", 0, 0, "b"]


def swap_cup(nums):
    cups[nums[0]], cups[nums[1]] = cups[nums[1]], cups[nums[0]]


for c in line:
    if c == "A":
        swap_cup((0, 1))
    elif c == "B":
        swap_cup((0, 2))
    elif c == "C":
        swap_cup((0, 3))
    elif c == "D":
        swap_cup((1, 2))
    elif c == "E":
        swap_cup((1, 3))
    elif c == "F":
        swap_cup((2, 3))

for i in range(len(cups)):
    if cups[i] == "s":
        s = i+1
    elif cups[i] == "b":
        b = i+1

print(s)
print(b)
