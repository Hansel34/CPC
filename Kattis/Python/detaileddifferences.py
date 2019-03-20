test_cases = int(input())

for _ in range(test_cases):
    line1 = input()
    line2 = input()
    print(line1)
    print(line2)
    for i,c in enumerate(line1):
        if c == line2[i]:
            print(".",end="")
        else:
            print("*",end="")
    print()
    print()