from collections import Counter
test_cases = int(input())

for i in range(test_cases):
    input()
    exists = set()
    c = Counter([x for x in input().split()])
    for key in c:
        if c[key] == 1:
            print("Case #{}: {}".format(i+1,key))