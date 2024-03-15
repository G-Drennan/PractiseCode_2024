class empty_class:
  pass

class Person:
  #Use the __init__() function to assign values to object properties at creation
  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
  #myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2)
  #You can use any other name instead of it
  
  def __init__(self, name, age): 
    self.name = name
    self.age = age
  #__str__() function controls what should be returned when the class object is represented as a string.
  def __str__(self): 
    return f"{self.name}({self.age})"
  
  #Objects can also contain methods. Methods in objects are functions that belong to the object. 
  def myfunc(self):
    print("Hello my name is " + self.name)

class Student(Person):#inheritance 
  def __init__(Student, name, age, year): #self => Student
    Student.name = name
    Student.age = age
    Student.year = year
  def newfunc(Student):
    print("I'm in year", Student.year) 

p1 = Person("John", 36) #obj

print(p1) 
p1.myfunc()

p1.age = 40

print(p1)

del p1 #delets p1

p2 = Student("Kim", 20, 2)
print(p2)
p2.myfunc()
p2.newfunc()

#ste and get 
class Dog:
 
    # Class Variable
    animal = 'dog'
 
    # The init method or constructor
    def __init__(self, breed):
 
        # Instance Variable
        self.breed = breed
 
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
 
    # Retrieves instance variable
    def getColor(self):
        return self.color

Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())

#function call functions with obj as input

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)