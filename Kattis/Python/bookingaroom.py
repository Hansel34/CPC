r, n = [int(x) for x in input().split()]

rooms = [0]*r

for _ in range(n):
    rooms[int(input())-1]=1
for i,room in enumerate(rooms):
    if room == 0:
        print(i+1)
        exit()
print("too late")