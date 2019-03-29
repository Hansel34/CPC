BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"

test_cases = int(input())
for _ in range(test_cases):
    k,b,n = [int(x) for x in input().split()]
    num = to_base(n,b)
    nums = []
    for c in num:
        if c.isdigit():
            nums.append(int(c))
        else:
            nums.append(ord(c)-ord('A')+10)
    num = sum([x*x for x in nums])
    print("{} {}".format(k,num))    
