l,r = [int(x) for x in input().split()]

if l == r and l != 0:
    print("Even {}".format(l*2))
elif l != r:
    val = max(l,r)
    print("Odd {}".format(val*2))
else:
    print("Not a moose")