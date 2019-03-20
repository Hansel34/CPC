test_cases = int(input())

for _ in range(test_cases):
    line = input()
    if line == "P=NP":
        print ("skipped")
    else:
        print(eval(line))