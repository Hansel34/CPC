inp = input()

count = 0
days = 0
for c in inp:
    if count == 0:
        if c != 'P':
            days+=1
    elif count == 1:
        if c != 'E':
            days+=1
    elif count == 2:
        if c != 'R':
            days+=1
    count+=1
    if count == 3:
        count = 0
            


print(days)
