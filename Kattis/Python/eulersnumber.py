from math import factorial
n = int(input())
if n < 50:
    print(sum([1/factorial(x) for x in range(n+1)]))
else:
    print(sum([1/factorial(x) for x in range(50)]))