while True:
    spots = list(map(int, input().split()))
    if spots == [0, 0, 0]:
        break
    spots.sort()
    if spots[0]**2 + spots[1]**2 == spots[2]**2:
        print("right")
    else:
        print("wrong")