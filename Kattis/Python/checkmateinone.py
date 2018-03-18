matrix = []
theirKingLocation = []
yourKingLocation = []


for x in range(8):
    line = input()
    for y,char in enumerate(line):
        if char == 'K':
            YOURKING = [x,y]
        if char == 'k':
            THEIRKING = [x,y]
        if char == 'R':
            ROOK = [x,y]
for x in range(-1,2):
    for y in range(-1,2):
        currX = THEIRKING[0]+x
        currY = THEIRKING[1]+y
        kingX= YOURKING[0]+x
        kingY= YOURKING[1]+y
        if currX >= 0 and currX<8 and currY >=0 and currY<8:
            theirKingLocation.append([currX,currY])
        if kingX >= 0 and kingX<8 and kingY >=0 and kingY<8:
            yourKingLocation.append([kingX,kingY])


for value in yourKingLocation:
    if value in theirKingLocation:
        theirKingLocation.remove(value)

Y = True
X = True
lastX = theirKingLocation[0][0]
lastY = theirKingLocation[0][1]
for value in theirKingLocation[1:]:
    if lastX!=value[0]:
        X = False
    if lastY!=value[1]:
        Y = False
if X == True:
    if ROOK[1]==YOURKING[1]:
        print("No")
        exit()
    if ROOK[1]== THEIRKING[1]+1 or ROOK[1]== THEIRKING[1]-1:
        print("No")
        exit()

elif Y == True:
    if ROOK[0]==YOURKING[0]:
        print("No")
        exit()
    if ROOK[0]== THEIRKING[0]+1 or ROOK[0]== THEIRKING[0]-1:
        print("No")
        exit()
else:
    print("No")
    exit()
print("Yes")
