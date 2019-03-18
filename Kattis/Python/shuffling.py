size, type = input().split()
size = int(size)
original_deck = [int(x) for x in range(size)]
new_deck = original_deck
turns = 0

while(True):
    if size % 2 == 0:
        if type == 'out':
            new_deck = [[new_deck[i],new_deck[i+size//2]] for i in range(size//2)]
        else:
            new_deck = [[new_deck[i+size//2],new_deck[i]] for i in range(size//2)]
        new_deck = [item for sub_list in new_deck for item in sub_list]
    else:
        middle_card = new_deck[size//2]
        if type == 'out':
            new_deck = [[new_deck[i],new_deck[i+(size+1)//2]] for i in range(size//2)]
            new_deck = [item for sub_list in new_deck for item in sub_list]
            new_deck.append(middle_card)
        else:
            new_deck = [[new_deck[i],new_deck[i+(size+1)//2]] for i in range(size//2)]
            new_deck = [item for sub_list in new_deck for item in sub_list]
            new_deck.insert(0,middle_card)
    turns+=1
    if new_deck == original_deck:
        break
print(turns)