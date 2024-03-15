#Deque (Doubly Ended Queue) in Python is implemented using the module “collections“.

from collections import deque 
     
# Declaring deque 
queue = deque(['name','age','DOB'])  
     
print(queue) 

# importing "collections" for deque operations
import collections
 
# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)
 
# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
 
# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)
 
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
 
# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

  
# importing "collections" for deque operations
import collections
 
# initializing deque
de = collections.deque([6, 1, 2, 3, 4])
print("deque: ", de)
 
# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
 
# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)
 
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
 
# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)

# importing "collections" for deque operations
import collections
 
# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])
 
# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))
 
# using insert() to insert the value 3 at 5th position
de.insert(4,3)
 
# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de)
 
# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3))
 
# using remove() to remove the first occurrence of 3
de.remove(3)
 
# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de)

from collections import deque
 
# initializing deque
de = deque([1, 2, 3, 4, 5, 6])
print("Current Deque: ", de)
 
# printing current size of deque
print(f"Size of Deque: {len(de)}")
 
# using pop() to delete element from right end
# deletes 6 from the right end of deque
de.pop()
 
# printing modified deque
print("\nThe deque after deleting from right is: ", end = '')
print(de)
 
# printing current size of deque
print(f"Size of Deque: {len(de)}")

from collections import deque
 
# initializing deque
de = deque([1, 2, 3, 4, 5, 6])
print("Current Deque: ", de)
 
# Accessing the front element of the deque
print("Front element of the deque:", de[0])
 
# Accessing the back element of the deque
print("Back element of the deque:", de[-1])

import collections
 
# initializing deque
de = collections.deque([1, 2, 3,])
 
# using extend() to add numbers to right end 
# adds 4,5,6 to right end
de.extend([4,5,6])
 
# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)
 
# using extendleft() to add numbers to left end 
# adds 7,8,9 to left end
de.extendleft([7,8,9])
 
# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)
 
# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)
 
# printing modified deque
print ("The deque after rotating deque is : ")
print (de)
 
# using reverse() to reverse the deque
de.reverse()
 
# printing modified deque
print ("The deque after reversing deque is : ")
print (de)