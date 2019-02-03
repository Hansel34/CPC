total = int(input())
leafs = [int(x) for x in input().split()]

nums = [0]*(2**total)

for i,leaf in enumerate(leafs):
    index = int(bin(i)[2:].zfill(total)[::-1],2)
    nums[index] = leaf


rand = 2
count = 0
while len(nums) > 1:
    new_nums = []
    for i in range(0,len(nums),2):
        if nums[i]==nums[i+1]:
            new_nums.append(nums[i])
        else:
            new_nums.append(rand)
            rand += 1
            count += 2
    nums= new_nums



print(count+1)