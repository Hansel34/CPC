dice1, dice2 = [int(x) for x in input().split()]


values = [0]*(dice1+dice2+1)

for i in range(dice1):
    for j in range(dice2):
        if i == 0 or j == 0:
            continue
        values[i+j]+=1
max_val = max(values)

for i,val in enumerate(values):
    if val == max_val:
        print(i+1)