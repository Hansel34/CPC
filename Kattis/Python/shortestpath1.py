from collections import defaultdict
import heapq
import sys
while True:
	n,m,qu,s = [int(x) for x in sys.stdin.readline().split()]
	if n == 0 and m == 0 and qu == 0 and s == 0:
		break

	graph = defaultdict(list)

	for x in range(m):
		u,v,w = [int(x) for x in sys.stdin.readline().split()]
		graph[u].append([v,w])

	#dijkstras 
	distance = [float("inf")]*n
	distance[s] = 0
	visited = set()
	q = [[distance[s],s]]
	while q:
		path_len, u = heapq.heappop(q)
		if u not in visited:
			visited.add(u)
			for v in graph[u]:
				distance[v[0]] = min(distance[v[0]],distance[u]+v[1])
				heapq.heappush(q,[distance[v[0]],v[0]])

	for _ in range(qu):
		q = int(sys.stdin.readline())
		if distance[q]!= float("inf"):
			sys.stdout.write(str(distance[q])+"\n")
		else:
			sys.stdout.write("Impossible"+"\n")
	sys.stdout.write("\n")





	








