import bisect

N , H = [int(x) for x in input().split()]
floor = []
ceiling = []
for i in range(N):
    if i % 2 == 0:
        floor.append((int(input())))
    else:
        ceiling.append(int(input()))
floor.sort()
ceiling.sort()

min_count = float("inf")
min_i = 0
for i in range(0,H):
    floor_count = len(floor) - bisect.bisect_left(floor,i+1)
    ceiling_count = len(ceiling) - bisect.bisect_left(ceiling,H-i)

    if min_count > floor_count+ceiling_count:
        min_count = floor_count+ceiling_count
        min_i = 1
    elif min_count == floor_count+ceiling_count:
        min_i+=1

print("{} {}".format(min_count,min_i))

