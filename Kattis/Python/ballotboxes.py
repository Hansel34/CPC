#Heap Method 
#Too Slow... 

# import heapq
# import math

# while True:

#     N, B = map(int, raw_input().split())

#     if N == -1 and B == -1:
#         break
    
#     cities = []
#     for _ in range(N):
#         population = int(raw_input())
#         cities.append([-population,population,1])
#     _ = raw_input()
#     heapq.heapify(cities)

#     for _ in range(B-N):
#         maxNum = heapq.heappop(cities)
#         maxNum[2]+=1
#         maxNum[0]=(-maxNum[1]//(maxNum[2]))
#         heapq.heappush(cities,maxNum)
        
#     print(-cities[0][0])

#Binary Search

while True:
    N, B = [int(x) for x in input().split()]
    if N == -1 and B == -1:
        break
    
    cities = []
    for _ in range(N):
        pop = int(input())
        cities.append(pop)

    low = 0
    high = 5000000
    currentUsedboxes = 0

    while low<high:
        mid = (low + high)//2
        currentUsedboxes = 0
        for city in cities:
            if city < mid:
                currentUsedboxes += 1
            else:
                currentUsedboxes += city//mid

        if currentUsedboxes == B:
            print(mid)
            break
        elif currentUsedboxes > B:
            low = mid+1
        else:
            high = mid-1
    
    print(mid)

    #Binary Search for max Population
    #Put boxes for max pop
    #If boxes run out, repeat
    #If too many boxes, repeat 
    #If perfect amount of boxes, GOOD 



#small funny world