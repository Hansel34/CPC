# n time stamps
# p percent speedup
# k is new time


n,p,k = [int(x) for x in input().split()]
p *= 0.01

nums = [int(x) for x in input().split()]

current_num = 0
original_length = 0
mulitplier = 1
nums.append(k)

for num in nums:
    original_length += mulitplier* (num - current_num)
    mulitplier+=p
    current_num = num

print(original_length)
