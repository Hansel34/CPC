while True:
    commands = int(input())
    if commands == 0:
        break
    bits = ['?']*32
    for _ in range(commands):
        line = input().split()
        if line[0] == 'SET':
            bits[int(line[1])] = '1'
        if line[0] == 'CLEAR':
            bits[int(line[1])] = '0'
        if line[0] == 'OR':
            if bits[int(line[1])] == '1' or bits[int(line[2])] == '1':
                bits[int(line[1])] = '1'
            elif bits[int(line[1])] == '0' and bits[int(line[2])] == '0':
                bits[int(line[1])] = '0'
            else:
                bits[int(line[1])] = '?'
        if line[0] == 'AND':
            if bits[int(line[1])] == '0' or bits[int(line[2])] == '0':
                bits[int(line[1])] = '0'
            elif bits[int(line[1])] == '1' and bits[int(line[2])] == '1':
                bits[int(line[1])] = '1'
            else:
                bits[int(line[1])] = '?'
        
    print("".join(bits[::-1]))