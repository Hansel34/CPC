ints = input().split()

intOne = int(ints[0][::-1])
intTwo = int(ints[1][::-1])

print(max(intOne,intTwo))