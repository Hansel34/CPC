test_cases = int(input())
for _ in range(test_cases):
    n, *grades = [int(x) for x in input().split()]
    avg = sum(grades)/n
    count = len([i for i in grades if i > avg])
    print("{:.3f}%".format(100*count/n))