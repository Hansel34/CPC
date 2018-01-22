#adjacencylist 
class AdjacencyList:
	def __init__(self):
		self.list = {}
		self.visited = []
		self.path = []
		self.pathReached = False
	def addConnection(self,x,y):
		if self.list.get(x) == None:
			self.list[x] = set()
		self.list[x].add(y)
		for z in y:
			if self.list.get(z) == None:
				self.list[z] = []
			self.list[z].add(x)

	def dfs(self,start,end):
		if self.list.get(start) != None:
			for node in self.list[start]:
				if node not in self.visited:
					self.visited.append(node)
					if node == end:
						self.pathReached = True
					self.dfs(node,end)
					if self.pathReached == True:
							self.path.append(node)
							return
				

#creating graph 

numberOfRoutes = int(input())
stationRoute = AdjacencyList()


for x in range(numberOfRoutes):
	stations = input().split()
	stationRoute.addConnection(stations[0],stations[1:])

start, end = input().split()
stationRoute.visited.append(start)
stationRoute.dfs(start,end)

if end in stationRoute.path:
	print(start+' ',end ='')
	for x in reversed(stationRoute.path):
		print(x+' ',end='')
else:
	print("no route found")




