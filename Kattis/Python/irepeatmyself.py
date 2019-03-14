times = int(input())

for _ in range(times):
    line = input()
    current = ""
    
    for c in line:
        current = current + c
        multiple = len(line)//len(current)
        if (current*multiple) == line[0:multiple*len(current)]:
            if len(line)//len(current) == len(line)/len(current):
                break
            if current.startswith(line[multiple*len(current):]):
                break
        
    print (len(current))