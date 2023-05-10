# 서로 다른 네 종류의 치즈가 토핑으로 들어가야 함 (Cheese로 끝나야함)
import sys
input = sys.stdin.readline

n = int(input())
toppings = list(input().split(" "))

cheese = set()
for topping in toppings:
    if topping.strip()[-6:] == "Cheese":
        cheese.add(topping.strip()[:len(topping.strip())-6])

if len(cheese) >= 4:
    print("yummy")
else:
    print("sad")