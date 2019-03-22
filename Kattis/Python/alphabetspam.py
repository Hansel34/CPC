line = input()
low = 0
high = 0
white = 0
others = 0

for c in line:
    if c.isalpha():
        if c == c.lower():
            low+=1
        else:
            high+=1
    elif c == '_':
        white+=1
    else:
        others+=1

total = sum([low,high,white,others])

print(white/total)
print(low/total)
print(high/total)
print(others/total)
