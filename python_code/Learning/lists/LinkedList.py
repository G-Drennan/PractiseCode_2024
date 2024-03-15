

#singly linked list
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): #obj var 
        self.head = None 
        self.last_node = None
  
    # function to add elements to linked list 
    def append(self, data): 
        # if linked list is empty then last_node will be none so in if condition head will be created 
        if self.last_node is None: 
            self.head = Node(data) 
            self.last_node = self.head 
        # adding node to the tail of linked list 
        else: 
            self.last_node.next = Node(data) 
            self.last_node = self.last_node.next
  
# function to print the content of linked list 
    def display(self): 
        current = self.head 
      # traversing the linked list 
        while current is not None: 
          # at each node printing its data 
            print(current.data, end=' ') 
           # giving current next node 
            current = current.next
        print()  

#circular
class CircularLinkedList: 
    def __init__(self): 
        self.head = None
        self.last_node = None
  
    # function to add elements to circular linked list 
    def append(self, data): 
        # is circular linked list is empty then last_node will be none so in if condition head will be created 
        if self.last_node is None: 
            self.head = Node(data) 
            self.last_node = self.head 
        # adding node to the tail of circular linked list 
        else: 
            self.last_node.next = Node(data) 
            self.last_node = self.last_node.next
            self.last_node.next = self.head 
  
    # function to print the content of circular linked list 
    def display(self): 
        current = self.head 
        while current is not None: 
            print(current.data, end=' ') 
            current = current.next
            if current == self.head: 
                break
        print() 

#double link
class Node: 
    def __init__(self, data): 
        self.previous = None
        self.data = data 
        self.next = None

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
        self.start_node = None
        self.last_node = None
  
    # function to add elements to doubly linked list 
    def append(self, data): 
        # is doubly linked list is empty then last_node will be none so in if condition head will be created 
        if self.last_node is None: 
            self.head = Node(data) 
            self.last_node = self.head 
        # adding node to the tail of doubly linked list 
        else: 
            new_node = Node(data) 
            self.last_node.next = new_node 
            new_node.previous = self.last_node 
            new_node.next = None
            self.last_node = new_node 
  
    # function to printing and traversing the content of doubly linked list from left to right and right to left 
    def display(self, Type): 
        if Type == 'Left_To_Right': 
            current = self.head 
            while current is not None: 
                print(current.data, end=' ') 
                current = current.next
            print() 
        else: 
            current = self.last_node 
            while current is not None: 
                print(current.data, end=' ') 
                current = current.previous 
            print() 

class DoublyLinkedListC: 
    def __init__(self): 
        self.head = None
        self.start_node = None
        self.last_node = None
  
    # function to add elements to doubly linked list 
    def append(self, data): 
        # is doubly linked list is empty then last_node will be none so in if condition head will be created 
        if self.last_node is None: 
            self.head = Node(data) 
            self.last_node = self.head 
        # adding node to the tail of doubly linked list 
        else: 
            new_node = Node(data) 
            self.last_node.next = new_node 
            new_node.previous = self.last_node 
            new_node.next = self.head 
            self.head.previous = new_node 
            self.last_node = new_node 
  
    # function to print the content of doubly linked list 
    def display(self, Type='Left_To_Right'): 
        if Type == 'Left_To_Right': 
            current = self.head 
            while current.next is not None: 
                print(current.data, end=' ') 
                current = current.next
                if current == self.head: 
                    break
            print() 
        else: 
            current = self.last_node 
            while current.previous is not None: 
                print(current.data, end=' ') 
                current = current.previous 
                if current == self.last_node.next: 
                    print(self.last_node.next.data, end=' ') 
                    break
            print() 

# Driver code 
if __name__ == '__main__':  
    print("link list single")
    L = LinkedList() 
    # adding elements to the linked list 
    L.append("String very long") 
    L.append("A pararot?") 
    L.append()   
    # displaying elements of linked list 
    L.display() 
    
    del L
    print("link list circular") 
    L = CircularLinkedList() 
    L.append(12) 
    L.append(56) 
    L.append(2) 
    L.append(11) 
          
    # Function call 
    L.display()  

    del L 
    print("link list double") 
    L = DoublyLinkedList() 
    L.append(1) 
    L.append(2) 
    L.append(3) 
    L.append(4) 
    L.display('Left_To_Right') 
    L.display('Right_To_Left') 

    del L
    print("link list double circular") 
    L = DoublyLinkedListC() 
    L.append(1) 
    L.append(2) 
    L.append(3) 
    L.append(4) 
    L.display('Left_To_Right') 
    L.display('Right_To_Left') 