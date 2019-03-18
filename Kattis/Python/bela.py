worth = {'A':[11,11],
'K':[4,4],
'Q':[3,3],
'J':[20,2],
'T':[10,10],
'9':[14,0],
'8':[0,0],
'7':[0,0]}

hands, dominant = [c for c in input().split()]
total = 0
for _ in range(int(hands)*4):
    card = [c for c in input()]
    if card[1]== dominant:
        total+=worth[card[0]][0]
    else:
        total+=worth[card[0]][1]
print(total)
