# Jessica Petty
# CSCI 3202
# Assignment 1
# September 4, 2015

import Queue

# Question 1: Implement a queue using the python queue module. Your queue should handle integers only
class IntQueue:
	def __init__(self):
		self.q = Queue.Queue()
	
	def put(self, value):
		if (isinstance(value, int)):
			self.q.put(value)
		else: 
			print("This queue only takes integers")
	
	def get(self):
		return self.q.get()
#for x in range(0, 5):
#	q.put(x)
#for x in range(0, 5):
#	item = q.get()
#	print(item)

# Question 2: Implement a stack using a list to store the stack data. The stack should be implemented as a class with
# at least three methods:
	# a. push(integer)
	# b. pop()
	# c. checkSize()
class MyStack:
	_stack = []
	def __init__(self):
		self.stack = []
		self.size = 0
	
	def push(self, value):
		self.stack.append(value)
		self.size = self.size + 1
	
	def pop(self):
		if self.size == 0:
			return "Empty stack"
		else:
			self.size = self.size - 1
			return self.stack[self.size]
	
	def checkSize(self):
		return self.size

# Question 3: Implement a binary tree class. The tree should be made up of nodes, which are also implemented as a class.
# The tree should have a root node. Each node in the tree has four properties:
	# a. integer key
	# b. left child
	# c. right child
	# d. parent
# Your tree class should have methods to add a node, delete a node, and print the key values of the nodes. The specific
# add, delete, and print functionality is as follows:
	# e. add(value, parentValue)
	# f. delete(value)
	# g. print()

class BinaryTree:
	def __init__(self, value):
		self.root = TreeNode(value, None)	
		
	def findNode(self, value, start, queue):
		if start.key == value:
			return start
		else:
			if start.rightChild != None:
				queue.put(start.rightChild)
				
			if start.leftChild != None:
				return self.findNode(value, start.leftChild, queue)
			else:
				if queue.empty() == True:
					return None
				else:
					start = queue.get()
					return self.findNode(value, start, queue)			
	
	def addValue(self, value, parentValue):
		q = Queue.Queue()
		node = self.findNode(parentValue, self.root, q)
		if (node == None):
			print("Parent not found")
		elif (node.leftChild != None and node.rightChild == None):
			newNode = TreeNode(value, node)
			node.rightChild = newNode
		elif (node.leftChild == None):
			newNode = TreeNode(value, node)
			node.leftChild = newNode
		elif (node.leftChild != None and node.rightChild != None):
			print("Parent has two children, node not added")
	
	def delete(self, value):
		q = Queue.Queue()
		node = self.findNode(value, self.root, q)
		if node == None:
			print("Node not found")
		elif (node.leftChild != None or node.rightChild != None):
			print("Node not deleted, has children")
		else:
			parent = node.parent
			if (parent.leftChild == node):
				parent.leftChild = None
			else:
				parent.rightChild = None
	
	def printTree(self):
		q = Queue.Queue()
		q.put(self.root)
		while (q.empty() == False):
			node = q.get()
			print(node.key)
			if node.leftChild != None:
				q.put(node.leftChild)
			if node.rightChild != None:
				q.put(node.rightChild)
	
class TreeNode:
	def __init__(self, value, parent):
		self.key = value
		self.leftChild = None
		self.rightChild = None
		self.parent = parent

# Question 4: Implement a graph class for an unweighted graph using a dictionary to store the graph data. Each vertex in
# the graph has an integer key value and a list of adjacent vertices. Your class should include the following methods:
	# a. addVertex(value)
	# b. addEdge(value1, value2)
	# c. findVertex(value)
class Graph:
	def __init__(self):
		self.vertices = {}
	
	def addVertex(self, value):
		if value in self.vertices:
			print("Vertex already exists")
		else:
			self.vertices[value] = []
	
	def addEdge(self, value1, value2):
		if (value1 not in self.vertices or value2 not in self.vertices):
			print("One or more vertices not found")
		elif value1 in self.vertices[value2]:
			print("Edge already exists")
		else:
			self.vertices[value1].append(value2)
			self.vertices[value2].append(value1)
	
	def findVertex(self, value):
		if value not in self.vertices:
			print("Value not in graph")
		else:
			adjacent = self.vertices[value]
			if len(adjacent) == 0:
				print("No adjacent edges")
			else:
				for item in adjacent:
					print(item)

# Question 5: Write the code to test your data structures. 
	# a. Testing the queue
print("Testing the queue: ")
# Create an Integer Queue
q = IntQueue()
# Add 15 items to the queue
for x in range(0, 15):
	q.put(x)
# Remove the items from the queue and print them
for x in range(0, 15):
	item = q.get()
	print(item)
# Try to put a bad value (not an integer) into the queue
q.put("jessica")

	# b. Testing the stack
print("Testing the stack: ")
# Create a new stack instance
newStack = MyStack()
# Add 15 elements to the stack
for x in range(0,15):
	newStack.push(x)
# Remove these 15 elements and print them
while (newStack.size != 0):
	item = newStack.pop()
	print(item)
# Try to pop from an empty stack
item = newStack.pop()
print(item)
	
	# c. Testing the tree
print("Testing adding to the binary tree: ")
# Initialize the new binary tree
tree = BinaryTree(12)
# Add 10 items to the binary tree
tree.addValue(8, 12)
tree.addValue(6, 8)
tree.addValue(9, 8)
tree.addValue(20, 12)
tree.addValue(16, 20)
tree.addValue(4, 6)
tree.addValue(15, 16)
tree.addValue(13, 15)
tree.addValue(2, 4)
tree.addValue(7, 6)
# Try to add an item with incorrect parent
tree.addValue(11, 21)
# Try to add an item to a full parent
tree.addValue(11, 12)
# Print binary tree
tree.printTree()
print("Testing deleting from the binary tree: ")
# Delete two items
tree.delete(7)
tree.delete(2)
# Try to delete a node not in the tree
tree.delete(21)
# Try to delete a node that has children
tree.delete(8)
# Print the tree
tree.printTree()

	# d. Testing the graph
# Create the new graph variable
print("Testing the graph")
myGraph = Graph()
# Add 15 items to the graph
myGraph.addVertex(17)
myGraph.addVertex(4)
myGraph.addVertex(11)
myGraph.addVertex(23)
myGraph.addVertex(42)
myGraph.addVertex(88)
myGraph.addVertex(53)
myGraph.addVertex(21)
myGraph.addVertex(47)
myGraph.addVertex(102)
myGraph.addVertex(3)
myGraph.addVertex(9)
myGraph.addVertex(62)
myGraph.addVertex(43)
myGraph.addVertex(31)
# Try to add an item already in the graph
myGraph.addVertex(9)
# Add 20 edges
myGraph.addEdge(3,9)
myGraph.addEdge(17, 42)
myGraph.addEdge(21, 102)
myGraph.addEdge(31, 17)
myGraph.addEdge(4, 53)
myGraph.addEdge(88, 23)
myGraph.addEdge(11, 47)
myGraph.addEdge(62, 43)
myGraph.addEdge(53, 42)
myGraph.addEdge(9, 102)
myGraph.addEdge(88, 3)
myGraph.addEdge(23, 62)
myGraph.addEdge(11, 4)
myGraph.addEdge(47, 42)
myGraph.addEdge(3, 4)
myGraph.addEdge(23, 11)
myGraph.addEdge(21, 4)
myGraph.addEdge(53, 43)
myGraph.addEdge(88, 102)
myGraph.addEdge(17, 62)
# Try to add an edge that already exists
myGraph.addEdge(88, 3)
# Try to add an edge with not every value in graph
myGraph.addEdge(7, 11)
# Find 5 vertices
myGraph.findVertex(11)
myGraph.findVertex(42)
myGraph.findVertex(4)
myGraph.findVertex(102)
myGraph.findVertex(21)
# Try to find a vertex that doesn't exist
myGraph.findVertex(12)
# Find a vertex with no adjacent edges
myGraph.addVertex(72)
myGraph.findVertex(72)
