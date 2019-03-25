from bisect import bisect_left

n,x = [int(x) for x in input().split()]

nums = [int(x) for x in input().split()]

nums.sort()
prev = 0
count = 0
for num in nums:
    if prev + num > x:
        print(max(count,1))
        exit()
    count+=1
    prev = num
print(count)

