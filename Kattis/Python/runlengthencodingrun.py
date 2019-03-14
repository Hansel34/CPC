line = input().split()

if line[0] == 'E':
    total = 0
    prev = None
    out = ""
    for c in line[1]:
        if prev != None and c!= prev:
            out = out + prev + str(total)
            total = 1
        else:
            total+=1
        prev = c
    if total != 0:
        out = out + prev + str(total)
    print(out)

else:
    out = ""
    for num in range(0,len(line[1]),2):
        out = out + line[1][num]*int(line[1][num+1])
    print(out)
