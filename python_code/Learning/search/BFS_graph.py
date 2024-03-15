# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.


#of a graph
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s.
			# If an adjacent has not been visited,
			# then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
if __name__ == '__main__':

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)


##for a disconnected graph##
	import queue 
  
def add_edge(edges, f, s): 
    edges[f][s] = 1
  
def print_bfs(edges, V, start, visited): 
    if V == 0: 
        return
    bfs = queue.Queue() 
    bfs.put(start) 
    visited[start] = 1
    while not bfs.empty(): 
        data = bfs.get() 
        print(data, end=' ') 
        for i in range(V): 
            if edges[data][i] == 1: 
                if visited[i] == 0: 
                    bfs.put(i) 
                    visited[i] = 1
  
def bfs_helper(edges, V): 
    if V == 0: 
        return
    visited = [0] * V 
    for i in range(V): 
        if visited[i] == 0: 
            print_bfs(edges, V, i, visited) 
  
if __name__ == "__main__": 
    V = 5
    E = 6
    if E == 0: 
        for i in range(V): 
            print(i, end=' ') 
        exit() 
  
    edges = [[0 for _ in range(V)] for _ in range(V)] 
  
    add_edge(edges, 0, 4) 
    add_edge(edges, 1, 2) 
    add_edge(edges, 1, 3) 
    add_edge(edges, 1, 4) 
    add_edge(edges, 2, 3) 
    add_edge(edges, 3, 4) 
  
    bfs_helper(edges, V) 