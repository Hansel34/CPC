
def kmpPreProcess(pattern):
    aux = [0] * len(pattern)
    i = 1
    m = 0
    while i < len(pattern):
        if pattern[i] == pattern[m]:
            m+=1
            aux[i] = m
            i+=1
        elif pattern[i] != pattern[m] and m!=0:
            m = aux[m-1]
        else:
            aux[i] = 0
            i+=1
    return aux

def kmpSearch(pattern,aux,text):
    i, j = 0, 0
    indexes = []
    while j < len(text):
        if pattern[i] != text[j]:
            if i == 0:
                j+=1
            else:
                i = aux[i-1]
        else:
            i+=1
            j+=1
            if i == len(pattern):
                indexes.append(j-i)
                i = aux[i-1]
    return indexes

while True:
    try:
        pattern = input()
        text = input()

        aux = kmpPreProcess(pattern)
        indexes = kmpSearch(pattern,aux,text)
        print(" ".join([str(c) for c in indexes]))
    except EOFError:
        break