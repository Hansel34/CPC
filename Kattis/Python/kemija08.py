line = input()
vowels = set(['a','e','i','o','u'])

i = 0
output = []
while (i < len(line)):
    output.append(line[i])
    if line[i] in vowels:
        i+=2
    i+=1

print("".join(output))
    
