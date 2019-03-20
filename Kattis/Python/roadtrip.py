#cost[i] = min(cost[j]
import heapq

n, capacity = [int(x) for x in input().split()]

stations = []
best_station = []
for _ in range(n):
    distance, cost = [int(x) for x in input().split()]
    stations.append([cost,distance])

stations.sort(key = lambda x:x[1])
start = 0
current_station = 0
total_cost = 0
current_gas = 10
while True:
    total_range = start+capacity
    while stations[current_station][1] < total_range and current_station<len(stations):
        heapq.heappush(best_station,stations[current_station])
        current_station+=1
    print(best_station)
    while best_station:
        best = heapq.heappop(best_station)
        if best[1] > start:
            break
    if current_gas > best[1]-start:
        current_gas-= best[1]-start
    else:
        total_cost +=  (best[1]-start)*best[0]
        print(best[0],best[1])
    start = best[1]
    if stations[-1][1] < start+capacity:
        break
print(total_cost)
    #find total range
    #put best ranges in best_stations
    #remove 
