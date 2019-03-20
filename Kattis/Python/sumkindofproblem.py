from sys import stdin
test_cases = int(stdin.readline())

for _ in range(test_cases):
    i,n = [int(x) for x in stdin.readline().split()]
    solutions = []
    solutions.append(i)
    total = sum([x for x in range(1,n+1)])
    totalodd = sum([x for x in range(1,n*2+1,2)])
    totaleven = sum([x for x in range(2,n*2+1,2)])
    print("{} {} {} {}".format(i,total,totalodd,totaleven))
