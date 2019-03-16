test_cases = int(input())

for _ in range(test_cases):
    __ = input()
    __ = input()
    God = [int(x) for x in input().split()]
    Mech = [int(x) for x in input().split()]

    god_max= 0
    mech_max = 0
    for num in God:
        if num > god_max:
            god_max = num
    
    for num in Mech:
        if num > mech_max:
            mech_max = num
    if god_max>=mech_max:
        print("Godzilla")
    else:
        print("MechaGodzilla")