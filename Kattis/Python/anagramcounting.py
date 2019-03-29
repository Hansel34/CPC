from math import factorial
from collections import Counter
while True:
    try:
        word = input()
        count = Counter(word)
        divide_by = 1
        total = factorial(len(word))
        for key,val in count.items():
            if val >= 2:
                divide_by*= factorial(val)
        print(total//divide_by)

    except EOFError:
        break