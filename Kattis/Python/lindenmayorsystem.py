rules, iterations = [int(x) for x in input().split()]

dic = {}
for _ in range(rules):
    line = input().split()
    dic[line[0]] = line[2]


start = input()


for _ in range(iterations):
    end = ""
    for c in start:
        if c in dic:
            end += dic[c]
        else:
            end += c
    start = end

print(start) 