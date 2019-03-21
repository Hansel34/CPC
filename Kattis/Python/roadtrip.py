from collections import deque

n, capacity = [int(x) for x in input().split()]

stations = []
best_station = deque()
best_station.append([0,0])

for _ in range(n):
    distance, cost = [int(x) for x in input().split()]
    stations.append([distance,cost])

stations.sort()
cost = 0
prev_station_d = 0
for station in stations:
    if station[0] - capacity > best_station[-1][0]:
        print("cancel road trip")
        exit()

    while (best_station[0][0]+capacity<=prev_station_d):
        best_station.popleft()

    while best_station[0][0] < station[0]- capacity:
        cost+= (best_station[0][0]+capacity-prev_station_d)*best_station[0][1]
        prev_station_d = best_station[0][0]+capacity
        best_station.popleft()

    cost+= best_station[0][1]*(station[0]-prev_station_d)
    prev_station_d = station[0]

    while(best_station and station[1]<best_station[-1][1]):
        best_station.pop()

    best_station.append(station)


print(cost)
