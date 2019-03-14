A, B, C = [int(x) for x in input().split()]

I, J, K = [int(x) for x in input().split()]


total = sum([I,J,K])


#Check for I:
smallest = 0

if J/I*A < B and K/I*A < C:
    smallest = 1
if I/J*B < A and K/J*B < C:
    smallest = 2
if I/K*C < A and J/K*C < B:
    smallest = 3

if smallest == 0:
    one = 0
    two = 0
    three = 0
elif smallest == 1:
    one = 0
    two = B - J/I*A 
    three = C - K/I*A
elif smallest == 2:
    one = A - I/J*B 
    two = 0
    three = C - K/J*B
elif smallest == 3:
    one = A - I/K*C
    two = B - J/K*C
    three = 0

print ('{} {} {}'.format(one,two,three))
