
_ = input()

nums = [int(x) for x in input().split()]
nums = nums[::-1]
answer = 0
current_min = nums[0]
for num in nums[1:]:
    if num >= current_min:
        answer += num-current_min+1
        current_min-=1
        if current_min == -1:
            print(1)
            exit()
    else:
        current_min = num
        
print(answer)