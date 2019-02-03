string1 = raw_input()
string2 = raw_input()
string3 = raw_input()

memory = [[False for x in range(len(string3)+1)] for y in range(len(string2)+1)]


for i in range(len(string2)+1):
    for j in range(len(string3)+1):
        if (i==0 and j==0):
            memory[i][j] = True
        elif i==0:
            memory[i][j] = memory[i][j-1] and string3[j-1] == string1[i+j-1]
        elif j==0:
            memory[i][j] = memory[i-1][j] and string2[i-1] == string1[i+j-1]
        else:
            memory[i][j] = memory[i-1][j] and string2[i-1] == string1[i+j-1] or memory[i][j-1] and string3[j-1] == string1[i+j-1]  

if (memory[len(string2)][len(string3)] == True):
    print("yes")
else:
    print("no")