N = int(input())

p_t,p_v = [float(x) for x in input().split()]

total = 0 
for i in range(N-1):
    t,v = [float(x) for x in input().split()]
    total+= (v+p_v)*(t-p_t)/2 
    p_t, p_v = t,v
print(total/1000)