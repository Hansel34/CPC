import math
p, a, b, c, d, n = [int(x) for x in input().split()]


current_max = float("-inf")
max_decline = float("-inf")

for k in range(1,n+1):
    current = p * (math.sin(a*k+b)+math.cos(c*k+d)+2)
    current_max = max(current,current_max)
    max_decline = max(max_decline,current_max-current)

print(max_decline)