# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class


# Parent Class Person
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def name(self):
        print(self.firstname, self.lastname)

x = Person("DHRUV", "MAISURIA")
x.name()

# Create a Child Class
# Child class Student
class Student(Person):
    pass
x = Student("Dhruv ", "Maisuria")
x.name()


# Add init () Function
# The child class will no longer inherit the parent's init() function.

# The child's init() function overrides the inheritance of the parent's init() function.

# Use __init__() in child cla
# ss 
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Student("Dhruv", "Maisuria")
x.name()



# super() Function
# super() function that will make the child class inherit all the methods and properties from its parent

# Use super() to access parent class Person's all properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Dhruv", "maisuria")
x.name()



# Add Properties
# Add passing year property 
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Dhruv", "Maisuria", 2019)
print(x.graduationyear)

# Add Methods
# Add detail method to print student information
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def detail(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Dhruv", "Maisuria", 2019)
x.detail()