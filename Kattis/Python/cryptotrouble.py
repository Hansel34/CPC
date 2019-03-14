length = int(raw_input())
nums = raw_input()

zeroes, ones, twos, threes = 0, 0, 0, 0

for c in nums:
    if c == '0':
        zeroes+=1
        continue
    num = int(c) % 3
    if num == 0:
        threes+=threes+1
        twos+=twos
        ones+=ones
    elif num == 1:
        threes,twos,ones = threes+twos, twos+ones,ones+threes+1
    else:
        threes,twos,ones = threes+ones, twos+threes+1,ones+twos
            
threes = ( (threes<<zeroes) % (10**9+7))

print(threes)


