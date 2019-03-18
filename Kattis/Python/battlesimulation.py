line = input()
output = []
for c in line:
    if c == 'R':
        if len(output) >=2:
            if (output[-1]=='H' and output[-2]=='K') or (output[-1]=='K' and output[-2]=='H'):
                output.pop()
                output.pop()
                output.append('C')
            else:
                output.append('S')
        else:
            output.append('S')
    elif c == 'B':
        if len(output) >=2:
            if (output[-1]=='S' and output[-2]=='H') or (output[-1]=='H' and output[-2]=='S'):
                output.pop()
                output.pop()
                output.append('C')
            else:
                output.append('K')
        else:
            output.append('K')
    elif c == 'L':
        if len(output) >=2:
            if (output[-1]=='S' and output[-2]=='K') or (output[-1]=='K' and output[-2]=='S'):
                output.pop()
                output.pop()
                output.append('C')
            else:
                output.append('H')
        else:
            output.append('H')

print("".join(output))