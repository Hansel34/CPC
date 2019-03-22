from collections import defaultdict

while True:
    test_cases = int(input())
    food = defaultdict(list)
    if test_cases == 0:
        break
    for name in range(test_cases):
        order = input().split()
        for item in order[1:]:
            food[item].append(order[0])
    food_orders = sorted(list(food))
    for item in food_orders:
        print("{} {}".format(item," ".join(sorted(food[item]))))
    print()