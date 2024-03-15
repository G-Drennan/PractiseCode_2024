import sys

# Structure for the elements in the
# Implement Priority Queue Using Array:  
class item :
	value = 0
	priority = 0
class GFG :

	# Store the element of a priority queue
	pr = [None] * (100000)
	
	# Pointer to the last index
	size = -1
	
	# Function to insert a new element
	# into priority queue
	@staticmethod
	def enqueue( value, priority) :
	
		# Increase the size
		GFG.size += 1
		
		# Insert the element
		GFG.pr[GFG.size] = item()
		GFG.pr[GFG.size].value = value
		GFG.pr[GFG.size].priority = priority
		
	# Function to check the top element
	@staticmethod
	def peek() :
		highestPriority = -sys.maxsize
		ind = -1
		
		# Check for the element with
		# highest priority
		i = 0
		while (i <= GFG.size) :
		
			# If priority is same choose
			# the element with the
			# highest value
			if (highestPriority == GFG.pr[i].priority and ind > -1 and GFG.pr[ind].value < GFG.pr[i].value) :
				highestPriority = GFG.pr[i].priority
				ind = i
			elif(highestPriority < GFG.pr[i].priority) :
				highestPriority = GFG.pr[i].priority
				ind = i
			i += 1
			
		# Return position of the element
		return ind
	
	# Function to remove the element with
	# the highest priority
	@staticmethod
	def dequeue() :
	
		# Find the position of the element
		# with highest priority
		ind = GFG.peek()
		
		# Shift the element one index before
		# from the position of the element
		# with highest priority is found
		i = ind
		while (i < GFG.size) :
			GFG.pr[i] = GFG.pr[i + 1]
			i += 1
			
		# Decrease the size of the
		# priority queue by one
		GFG.size -= 1
	@staticmethod
	def main( args) :
	
		# Function Call to insert elements
		# as per the priority
		GFG.enqueue(10, 2)
		GFG.enqueue(14, 4)
		GFG.enqueue(16, 4)
		GFG.enqueue(12, 3)
		
		# Stores the top element
		# at the moment
		ind = GFG.peek()
		print(GFG.pr[ind].value)
		
		# Dequeue the top element
		GFG.dequeue()
		
		# Check the top element
		ind = GFG.peek()
		print(GFG.pr[ind].value)
		
		# Dequeue the top element
		GFG.dequeue()
		
		# Check the top element
		ind = GFG.peek()
		print(GFG.pr[ind].value)
	
if __name__=="__main__":
	GFG.main([])

#Implement Priority Queue Using Linked List: 

# Python3 code to implement Priority Queue
# using Singly Linked List

# Class to create new node which includes
# Node Data, and Node Priority
class PriorityQueueNode:

	def _init_(self, value, pr):

		self.data = value
		self.priority = pr
		self.next = None

# Implementation of Priority Queue


class PriorityQueue:

	def _init_(self):

		self.front = None

	# Method to check Priority Queue is Empty
	# or not if Empty then it will return True
	# Otherwise False
	def isEmpty(self):

		return True if self.front == None else False

	# Method to add items in Priority Queue
	# According to their priority value
	def push(self, value, priority):

		# Condition check for checking Priority
		# Queue is empty or not
		if self.isEmpty() == True:

			# Creating a new node and assigning
			# it to class variable
			self.front = PriorityQueueNode(value,
										priority)

			# Returning 1 for successful execution
			return 1

		else:

			# Special condition check to see that
			# first node priority value
			if self.front.priority < priority:

				# Creating a new node
				newNode = PriorityQueueNode(value,
											priority)

				# Updating the new node next value
				newNode.next = self.front

				# Assigning it to self.front
				self.front = newNode

				# Returning 1 for successful execution
				return 1

			else:

				# Traversing through Queue until it
				# finds the next smaller priority node
				temp = self.front

				while temp.next:

					# If same priority node found then current
					# node will come after previous node
					if priority >= temp.next.priority:
						break

					temp = temp.next

				newNode = PriorityQueueNode(value,
											priority)
				newNode.next = temp.next
				temp.next = newNode

				# Returning 1 for successful execution
				return 1

	# Method to remove high priority item
	# from the Priority Queue
	def pop(self):

		# Condition check for checking
		# Priority Queue is empty or not
		if self.isEmpty() == True:
			return

		else:

			# Removing high priority node from
			# Priority Queue, and updating front
			# with next node
			self.front = self.front.next
			return 1

	# Method to return high priority node
	# value Not removing it
	def peek(self):

		# Condition check for checking Priority
		# Queue is empty or not
		if self.isEmpty() == True:
			return
		else:
			return self.front.data

	# Method to Traverse through Priority
	# Queue
	def traverse(self):

		# Condition check for checking Priority
		# Queue is empty or not
		if self.isEmpty() == True:
			return "Queue is Empty!"
		else:
			temp = self.front
			while temp:
				print(temp.data, end=" ")
				temp = temp.next


# Driver code
if __name__ == "_main_":

	# Creating an instance of Priority
	# Queue, and adding values
	# 7 -> 4 -> 5 -> 6
	pq = PriorityQueue()
	pq.push(4, 1)
	pq.push(5, 2)
	pq.push(6, 3)
	pq.push(7, 0)

	# Traversing through Priority Queue
	pq.traverse()

	# Removing highest Priority item
	# for priority queue
	pq.pop()
