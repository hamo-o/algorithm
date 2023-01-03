coin = [0]*6

rest = 1000 - int(input())

coin[0] = rest//500
rest %= 500
coin[1] = rest//100
rest %= 100
coin[2] = rest//50
rest %= 50
coin[3] = rest//10
rest %= 10
coin[4] = rest//5
rest %= 5
coin[5] = rest//1

print(sum(coin))
