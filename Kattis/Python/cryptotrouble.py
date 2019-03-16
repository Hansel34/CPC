length = int(input())
nums = input()

zeroes, ones, twos, threes, three = 0, 0, 0, 0, 0

for c in nums:
    if c == '0':
        zeroes+=1
        continue
    num = int(c) % 3
    if num == 0:
        three+=1
    elif num == 1:
        threes,twos,ones = threes+twos, twos+ones,ones+threes+1
    elif num == 2:
        threes,twos,ones = threes+ones, twos+threes+1,ones+twos
     
threes = (((1<<three)-1) << zeroes)   + (threes << zeroes) + ((((1<<three)-1) << zeroes)*threes)
threes = threes % (10**9+7)
print(threes)


