test_case = int(input())

for _ in range(test_case):
    new = 0
    years = [int(x) for x in input().split()]
    prev = years[0]
    for year in years[1:]:
        new += max(0,year-2*prev)
        prev = year

    print(new)