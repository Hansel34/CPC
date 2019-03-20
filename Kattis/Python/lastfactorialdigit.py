from math import factorial
test_cases = int(input())

for _ in range(test_cases):
    total = factorial(int(input()))
    print(str(total)[-1])
