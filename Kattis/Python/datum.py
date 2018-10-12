from datetime import date

D, M = [int(x) for x in input().split()]

date = date(2009, M, D)

print(date.strftime("%A"))