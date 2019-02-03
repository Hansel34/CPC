def is_white(row,col):
    if row % 2 == 1:
        if col % 2 == 1:
            return False
        else:
            return True
    else:
        if col % 2 == 1:
            return True
        else:
            return False

def convert_to_num(s):
    return ord(s)-ord('A')+1

def convert_to_char(v):
    return chr(v-1+ord('A'))

def find_all_positions(row,col,pos):
    t_r, t_c = row, col
    pos.add((t_r,t_c))

    while True:
        t_r-=1
        t_c-=1
        if not (t_r>=1 and t_r <=8 and t_c>=1 and t_c <=8):
            break
        pos.add((t_r,t_c))
    t_r, t_c = row, col
    while True:
        t_r-=1
        t_c+=1
        if not (t_r>=1 and t_r <=8 and t_c>=1 and t_c <=8):
            break
        pos.add((t_r,t_c))
    t_r, t_c = row, col
    while True:
        t_r+=1
        t_c-=1
        if not (t_r>=1 and t_r <=8 and t_c>=1 and t_c <=8):
            break
        pos.add((t_r,t_c))
    t_r, t_c = row, col
    while True:
        t_r+=1
        t_c+=1
        if not (t_r>=1 and t_r <=8 and t_c>=1 and t_c <=8):
            break
        pos.add((t_r,t_c))

cases = int(input())

for _ in range(cases):
    s_c,s_r,e_c,e_r = input().split()
    s_c = convert_to_num(s_c)
    s_r, e_r = int(s_r), int(e_r)
    e_c = convert_to_num(e_c)

    if is_white(s_r,s_c) != is_white(e_r,e_c):
        print("Impossible")
        continue
    
    moves = 0
    c_c,c_r = s_c,s_r
    output = []

    while True:
        output.append(convert_to_char(c_c))
        output.append(c_r)

        start_position = set()
        find_all_positions(c_r,c_c,start_position)

        if c_c == e_c and c_r == e_r:
            break

        if (e_r,e_c) in start_position:
            output.append(convert_to_char(e_c))
            output.append(e_r)
            moves+=1
            break
        end_position = set()

        find_all_positions(e_r,e_c,end_position)
        middle_pos = list(start_position.intersection(end_position))[0]
        moves = 2
        output.append(convert_to_char(middle_pos[1]))
        output.append(middle_pos[0])
        output.append(convert_to_char(e_c))
        output.append(e_r)
        break


    output.insert(0,moves)
    print(" ".join([str(x) for x in output]))
    

    