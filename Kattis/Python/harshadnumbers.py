def check_harshad(n):
    return n%sum([int(c) for c in str(n)])==0

n = int(input())

while (check_harshad(n)== False):
    n+=1
print(n)