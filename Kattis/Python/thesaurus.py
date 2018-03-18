from collections import defaultdict
N, M = map(int,input().split())
inputString = input().split(" ")

sentence = defaultdict(int)
thesaurus = defaultdict(dict)

for word in inputString:
    sentence[word] += 1

one, two = input().split(" ")
if len(one) > len(two):
    shorter = two
    longer = one
else:
    shorter = one
    longer = two
thesaurus[shorter][longer] = 0
thesaurus[shorter][shorter] = 0
for y in range(1,M):
    one, two = input().split(" ")
    if len(one) > len(two):
        shorter = two
        longer = one
    else:
        shorter = one
        longer = two
    add = True
    replace = False
    for x in thesaurus:
        if thesaurus.get(x).get(one)!= None:
            add = False
            if thesaurus.get(x).get(two)== None:
                thesaurus.get(x)[two]=0
            if len(shorter) < len(x):
                replace = True
                currX = x
                break
        elif thesaurus.get(x).get(two)!= None:
            add = False
            if thesaurus.get(x).get(one)== None:
                thesaurus.get(x)[one]=0
            if len(shorter) < len(x):
                replace = True
                currX = x
                break

    if add == True:
        thesaurus[shorter][longer]=0
        thesaurus[shorter][shorter]=0
    if replace == True:
        thesaurus[shorter]=thesaurus[currX]
        thesaurus.pop(currX)
count = 0

for key in sentence:
    exists = False
    for x in thesaurus:
        if key in thesaurus[x]:
            exists = True
            count+= len(x)*sentence[key]
            break
    if exists == False:
        count+= len(key)*sentence[key]

print(count)