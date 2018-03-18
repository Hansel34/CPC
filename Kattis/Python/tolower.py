P, T = [int(x) for x in input().split()]
count = 0
for x in range(P):
    fail = False

    for y in range(T):
        line = input()
        for char in line[1:]:
            temp = char
            if temp != (char.lower()):
                fail = True
                continue
    if fail == False:
        count+=1
print(count)