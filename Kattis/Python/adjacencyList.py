#adjacencylist 
class AdjacencyList:
	def __init__(self):
		self.list = {}
		self.visited = []
	def addConnection(self,x,y):
		if self.list.get(x) == None:
			self.list[x] = []
		self.list[x].extend(y)

		

	def printList(self):
		print(self.list)

	def dfs(self,start):
		for node in self.list[start]:
			if node not in self.visited:
				self.visited.append(node)
				self.dfs(node)
				


