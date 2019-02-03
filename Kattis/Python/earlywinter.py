totalyears, currentYear = [int(x) for x in input().split()]

years = [int(x) for x in input().split()]

for count,year in enumerate(years):
    if year <= currentYear:
        print("It hadn't snowed this early in {} years!".format(count))
        exit()
print("It had never snowed this early!")
