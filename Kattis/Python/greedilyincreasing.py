input()

nums = [int(x) for x in input().split()]

prev = 0
output = []
for num in nums:
    if num > prev:
        output.append(num)
        prev = num

print(len(output))
print(" ".join([str(c) for c in output]))