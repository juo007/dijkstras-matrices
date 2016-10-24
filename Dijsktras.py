import sys

#return the index of the minimal weight that is not visited
#in the given list
def minNode(list,visited):
	unvisited = []
	newList = []
	for x in range(len(list)):
		if x not in visited:
			unvisited.append(x)
			
	if not unvisited:
		return

	for x in unvisited:
		if list[x] > 0:
			tup = (list[x],x)
			newList.append(tup)

	newList.sort(key=lambda tup:tup[0])
	return newList[0][1]

def func1(Matrix, target):

	solution = []
	numNodes = len(Matrix[0])
	visited = set()

	matrix = map(list,zip(*Matrix))
	
	#initialize solution array to inifinity
	for x in range(numNodes):
		solution.append(sys.maxint)
	
	#initialize the target node to be visited, and solution to be zero
	visited.add(target)
	solution[target] = matrix[target][target]
	
	for node in range(numNodes):
		weight = matrix[target][node]
		if weight > 0 and weight < solution[node]:
			solution[node] = weight;
	
	frontierNode = minNode(matrix[target],visited)
	
	while frontierNode:
		for node in range(numNodes):
			weight = matrix[frontierNode][node]
			if weight > 0 and node not in visited and weight + solution[frontierNode] < solution[node]:
				solution[node] = weight + solution[frontierNode];
				
		visited.add(frontierNode)
		frontierNode = minNode(solution,visited)
		
	return solution
					
def func2(Matrix,target):
	numNodes = len(Matrix[0])
	paths = []
	solution = []
	graph = {}
	
	matrix = map(list,zip(*Matrix))
	
	for x in range(numNodes):
		path = []
		for y in range(numNodes):
			if matrix[x][y] > 0:
				path = path + [y]
		graph[x] = path	

	for node in range(numNodes):
		paths = find_all_paths(graph,target,node)		
		costs = []
		for path in paths:
			cost = 0
			for p in range(len(path)-1):
				cost+= matrix[path[p]][path[p+1]]
			if len(path) is 1:
				cost = matrix[0][0]
			costs.append(cost)
		if costs:
			solution.append(min(costs))
		
	return solution		
	
def find_all_paths(graph, target, end, path=[]):
	path = path + [target]
	if target == end:
		return [path]
	if not graph.has_key(target):
		return
	paths = []
	for node in graph[target]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
				
	return paths
	
def func3(matrix, solution, target, othernode):
	path = []
	numNodes = len(matrix[0])
	path.append(target)
	
	while(othernode is not target):
		cost = []
		for node in range(numNodes):
			weight = matrix[target][node]
			if weight > 0:
				tuple = (node,weight+solution[node])
				cost.append(tuple)
		
		#print "cost ", cost
		cost.sort(key=lambda tuple:tuple[1])
		path.append(cost[0][0])
		othernode = (cost[0][0])
	
	return path	

if __name__ == "__main__":
	from random import randint
	
	Matrix = [[0 for x in range(8)] for y in range(8)]
	
	for x in range(8):
		for y in range(8):
			if randint(0,9) < 7:
				Matrix[x][y] = randint(0,5)
	
	print Matrix
	#newMatrix = map(list,zip(*Matrix))
	#print newMatrix
	'''Matrix[0] = [0, 4, 0, 0, 0, 0, 0, 8, 0]
	Matrix[1] = [4, 0, 8, 0, 0, 0, 0, 11 ,0]
	Matrix[2] = [0, 8, 0, 7, 0, 4, 0, 0, 2]
	Matrix[3] = [0, 0, 7, 0, 9, 14, 0, 0, 0]
	Matrix[4] = [0, 0, 0, 9, 0, 10, 0, 0, 0]
	Matrix[5] = [0, 0, 4, 14, 10, 0, 2, 0, 0]
	Matrix[6] = [0, 0, 0, 0, 0, 2, 0, 1, 6]
	Matrix[7] = [8, 11, 0, 0, 0, 0, 1, 0, 7]
	Matrix[8] = [0, 0, 2, 0, 0, 0, 6, 7, 0]'''
	
	solution = func1(Matrix,0)	

	solution2 = func2(Matrix,0)
	print solution
	print solution2	
	
	path = func3(Matrix,solution,0,7)
	
	print path	
	
		
	
	
	
	
	
	
	
		
		
	
	
		