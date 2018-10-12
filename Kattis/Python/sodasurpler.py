e,f,c = [int(x) for x in input().split()]


total = e + f
drinks = 0

while(total>=c):
    total-=c
    total+=1
    drinks +=1

print(drinks)