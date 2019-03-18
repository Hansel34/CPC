test_cases = int(input())

for case in range(test_cases):
    octal = input()
    octal_result = 0
    for index, c in enumerate(octal[::-1]):
        octal_result += int(c)* (8**index)
    if octal_result == int(octal):
        print("equivalent")
    else:
        print("not equivalent")


