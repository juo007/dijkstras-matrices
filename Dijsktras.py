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
			
	if not newList:
		return

	newList.sort(key=lambda tup:tup[0])
	return newList[0][1]

'''Dijsktra's with a given 2-D Matrix with weight values
	This will return a vector of the shortest path to the 
	target from every other node'''
def func1(Matrix, target):

	solution = []
	numNodes = len(Matrix[0])
	visited = set()

	#Need to transpose matrix to get INCOMING edges
	matrix = map(list,zip(*Matrix))
	
	#initialize solution array to inifinity
	for x in range(numNodes):
		solution.append(sys.maxint)
	
	#initialize the target node to be visited, and solution to be zero
	visited.add(target)
	solution[target] = matrix[target][target]
	
	#initialize
	for node in range(numNodes):
		weight = matrix[target][node]
		if weight > 0:
			solution[node] = weight;

	frontierNode = minNode(matrix[target],visited)
	
	#loop through each node and check for a smaller path
	while frontierNode is not target and frontierNode is not None:
		for node in range(numNodes):
			weight = matrix[frontierNode][node]
			if weight > 0 and node not in visited and weight + solution[frontierNode] < solution[node]:
				solution[node] = weight + solution[frontierNode];
				
		visited.add(frontierNode)
		frontierNode = minNode(solution,visited)
		
	return solution
				
#Lists out all the given paths 
#Recursively calls a function that will get all the paths
#between two nodes. Call iterarively on that recursive function				
def func2(Matrix,target):
	numNodes = len(Matrix[0])
	paths = []
	solution = []
	graph = {}
	
	#Need to transpose matrix to get OUTGOING
	matrix = map(list,zip(*Matrix))
	
	#Set up graph from matrix
	for x in range(numNodes):
		path = []
		for y in range(numNodes):
			if matrix[x][y] > 0:
				path = path + [y]
		graph[x] = path	
	#Call recursive function for every end node, then
	#compute the costs of each path. Take the minimum
	#cost and append it to our solution
	for node in range(numNodes):
		paths = find_all_paths(graph,target,node)	
		costs = []
		for path in paths:
			cost = 0
			for p in range(len(path)-1):
				cost+= matrix[path[p]][path[p+1]]
			if len(path) is 1:
				cost = matrix[target][target]
			costs.append(cost)
		if costs:
			solution.append(min(costs))
		
	return solution		
	
#Recursive function that will find all paths
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
	
#Given a matrix, its solution vector with all the shortest
#paths to the target, and another node that is NOT the target
#This function will produce the path of the shortest function
#Uses the information of its neighbors to calculate
def func3(matrix, solution, target, othernode):
	path = []
	numNodes = len(matrix[0])
	path.append(othernode)
	visited = set()
	visited.add(othernode)
	
	#loop through each neighbor and pick the cost that is the least
	#cost where the cost includes both the weight to the neighbor 
	#and the neighbor's distance to the target
	while(othernode is not target):
		cost = []
		for node in range(numNodes):
			weight = matrix[othernode][node]
			if weight > 0 and node not in visited:
				if node is target:
					#Need to check if the case is the target
					#If so, we should not add the cost to itself
					tuple= (node,weight)
				else:
					tuple = (node,weight+solution[node])
				cost.append(tuple)
		
		cost.sort(key=lambda tuple:tuple[1])
		path.append(cost[0][0])
		visited.add(cost[0][0])
		othernode = (cost[0][0])
		
	return path	

if __name__ == "__main__":
	from random import randint
	import timeit
	
	N = 8
	Matrix = [[0 for x in range(N)] for y in range(N)]
	
	for x in range(N):
		for y in range(N):
			if randint(0,9) < 7:
				Matrix[x][y] = randint(0,5)
	#print Matrix
	

	#start_time = timeit.default_timer()
	solution = func1(Matrix,0)
	#elapsed = timeit.default_timer() - start_time
	#print(elapsed)

	#start_time2 = timeit.default_timer()
	solution2 = func2(Matrix,0)
	#elapsed2 = timeit.default_timer() - start_time2
	#print(elapsed2)
	
	print "===solution for func1==="
	print solution
	print "===solution for func2==="
	print solution2	
	
	path = func3(Matrix,solution,1,N-1)
	print "===solution for func3==="
	print path	
	
		
	
	
	
	
	
	
	
		
		
	
	
		