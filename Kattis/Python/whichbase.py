cases = int(input())

for _ in range(cases):
    n, num = [int(x) for x in input().split()]
    if '9' in str(num) or '8' in str(num):
        oct_num = 0 
    else: 
        oct_num = num
    print("{} {} {} {}".format(n,int(str(oct_num),8),num,int(str(num),16)))