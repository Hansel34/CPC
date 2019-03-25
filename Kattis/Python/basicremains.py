BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"

while True:
    vals = [int(x) for x in input().split()]
    if len (vals) == 1:
        break
    
    print(to_base(int(str(vals[1]),vals[0])%int(str(vals[2]),vals[0]),vals[0]))
