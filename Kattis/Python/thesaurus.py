from collections import defaultdict
MAXN = 10000
parent = []
n,m = [int(x) for x in input().split()]
def find(x):
    if(parent[x]==x):
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
#make y the parent of x. 
def unite(x,y):
    parent[find(x)] = find(y)

for i in range(MAXN):
    parent.append(i)


inputString = input().split()
sentence = defaultdict(int)
for word in inputString:
    sentence[word] += 1

entrees = {}
findSmallest = {}
counter = 0
for x in range(m):
    first, second = input().split()
    if entrees.get(first) == None:
        findSmallest[counter] = first
        entrees[first] = counter
        counter += 1
    if entrees.get(second) == None:
        findSmallest[counter] = second
        entrees[second] = counter 
        counter += 1
    if len(findSmallest[find(entrees[first])]) < len(findSmallest[find(entrees[second])]):
        unite(entrees[findSmallest[find(entrees[second])]],entrees[findSmallest[find(entrees[first])]])
    else:
        unite(entrees[findSmallest[find(entrees[first])]],entrees[findSmallest[find(entrees[second])]])
count = 0
for key in sentence:
    if entrees.get(key) != None:
        count += len(findSmallest[find(entrees[key])])* sentence[key]
    else:
        count+= len(key)*sentence[key]
print(count)






