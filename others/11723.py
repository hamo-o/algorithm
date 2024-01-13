import sys
input = sys.stdin.readline

num = int(input())
commands = []
bits = 0

for _ in range(num):
    command = list(input().split(" "))
    com = command[0].strip()
    if com == 'add':
      bits = bits | (1 << int(command[1]))
    elif com == 'remove':
      bits = bits & ~(1 << int(command[1]))
    elif com == 'check':
      if bits & (1 << int(command[1])):
          print(1)
      else:
          print(0)
    elif com == 'toggle':
        bits = bits ^ (1 << int(command[1]))
    elif com == 'all':
        bits = bits | ((1 << 21) - 1)
    elif com == 'empty':
        bits = 0