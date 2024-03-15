#array
class Queue:
        # constructor
    def __init__(self, cap):
        self.cap = cap
        self.front = 0
        self.size = 0
        self.rear = cap - 1
        self.arr = [0] * cap
 
    # Function to create a queue of given capacity
    # It initializes size of queue as 0
    def createQueue(self):
        return Queue(self.cap)

#linked list
class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

#CircularQueue 
class CircularQueue():
 
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
         
        # initializing queue with none
        self.queue = [None for i in range(size)] 
        self.front = self.rear = -1
 
    def enqueue(self, data):
         
        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front): 
            print(" Queue is Full\n")
             
        # condition for empty queue
        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
             
            # next position of rear
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = data
             
    def dequeue(self):
        if (self.front == -1): # condition for empty queue
            print ("Queue is Empty\n")
             
        # condition for only one element
        elif (self.front == self.rear): 
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
 
    def display(self):
     
        # condition for empty queue
        if(self.front == -1): 
            print ("Queue is Empty")
 
        elif (self.rear >= self.front):
            print("Elements in the circular queue are:", 
                                              end = " ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        else:
            print ("Elements in Circular Queue are:", 
                                           end = " ")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

#que functions

# Function to add an item to the queue.
# It changes rear and size       
def EnQueue(self, item):
    if self.isFull():
        print("Full")
        return
    self.rear = (self.rear + 1) % (self.capacity)
    self.Q[self.rear] = item
    self.size = self.size + 1
    print("% s enqueued to queue" % str(item))

 
# Function to remove an item from queue.
# It changes front and size
def DeQueue(self):
    if self.isEmpty():
        print("Queue is empty")
        return
 
    print("% s dequeued from queue" % str(self.Q[self.front]))
    self.front = (self.front + 1) % (self.capacity)
    self.size = self.size - 1

# Function to get front & rear of queue
def que_front(self):
        if self.isempty():
            return "Queue is empty"
        return self.Q[self.front]

def rear(queue):
	if queue.empty():
		print("Queue is empty.")
		return None

	rear_element = None
	while not queue.empty():
		rear_element = queue.get()

	return rear_element

def isEmpty(self):
    return self.size == 0
# Queue is full when size becomes
# equal to the capacity
 
 
def isFull(self):
    return self.size == self.capacity