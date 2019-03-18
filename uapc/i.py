n,m = [int(x) for x in input().split()]

weight = []
value = []
for _ in range(n):
    food = [int(x) for x in input().split()]
    weight.append(food[0])
    value.append(food[1])

def knapSack(W , wt , val , n): 

    if n == 0 or W == 0 : 
        return 0
  
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 

print (knapSack(m,weight,value,n))