while True:

    x, y = [int(x) for x in input().split()]

    if x == 0 and y == 0:
        break
    
    if x + y == 13:
        print("Never speak again.")
        continue
    
    if x == y:
        print("Undecided.")
        continue

    if x > y:
        print("To the convention.")
        continue
    
    if x < y:
        print("Left beehind.")
        continue