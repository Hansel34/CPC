count = int(input())
days = [0]*365
for _ in range(count):
    start, end = [int(x) for x in input().split()]
    for i in range(start-1,end):
        days[i] = 1
print (days.count(1))