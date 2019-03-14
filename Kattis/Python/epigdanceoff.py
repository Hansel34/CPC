rows, col = [int(x) for x in input().split()]
each_column = [0]*col

for i in range(rows):
    line = input()
    for index,c in enumerate(line):
        if c == "$":
            each_column[index] = 1

print(each_column.count(0)+1)
