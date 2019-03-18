line = input()
line = [line[i:i+3] for i in range(0, len(line), 3)]
dic= {'P':set(), 'K': set(), 'H': set(), 'T': set()}

for card in line:
    if card in dic[card[0]]:
        print("GRESKA")
        exit()
    else:
        dic[card[0]].add(card)

print(13-len(dic['P']),13-len(dic['K']),13-len(dic['H']),13-len(dic['T']))
