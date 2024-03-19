
# class car:
#     color="blue"
#     brand="mercedes"
# car1=car()
# print(car1.color)
# #Output: blue
# print(car.brand)

# ---------__init__ Function-----------------------------------------
# // all classes have a function called __init__(), which is always executed when the class is being initiated.
# ex1///
# class Student:
#     name="Dhruv"
#     def __init__(self):
#         print(self)
#         print("adding new student in Database..")

# s1= Student()
# print(s1)

# // ex2///
# class Student:
#     def __init__(self,fullname,marks):
#         self.name= fullname
#         self.marks= marks
#         print("adding new student in Database..")

# s1= Student("Dhruv Maisuria",99)
# print(s1.name,s1.marks)

# s2= Student("Harry Rack",90)
# print(s2.name,s2.marks)

# --------------------------------------------------
# class and instance attributes
# class.attr
# obj.attr
# instance.__dict__.attribute  (access through this way also possible)


# -------------Methods :- methods are functions  that belong to objects-------------------------------------
# class Student:
#     college_name= "Maliba college"

#     def __init__(self,name,marks):
#         self.name= name
#         self.marks= marks

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks
# s1= Student("Dhruv Maisuria",99)
# s1.welcome()
# print("Your exam marks is",s1.get_marks())


# // create student class that takes name and marks of 3 subjects as arguments in constructor.
# //then create a method to print the average.----------

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hello", self.name, "your avg score is : ", sum/3)


# s1 = Student("tony stark", [99, 98, 97])
# s1.get_avg()

# s1.name="IronMan"
# s1.get_avg()

# --/---- Static method:- methods that dont use the self parameter. work ar class level ----------------------------------
# class Student:
#     @staticmethod   # decorator
#     def test():
#         print('this is static method')
# Student.test()

# ---// Important-----------------------------------------------

# //1. Abstraction:- hiding the implementation details of class and only showing the essential features to the user.
# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def Start(self):
#         self.clutch=True
#         self.acc=True
#         print("Engine start")
# car1=car()
# car1.Start()

# 2. Encapsulation:- wrapping data and functions into a single unit(object).


# ---//create account class with 2 attributes- balance and account no
# ---//create methods for debit , credit and printing the balance.-----------------------------------------------

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "Was Debited.")
#         return self.balance

#     # Credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "Was Credited.")
#         return self.balance

#     def get_balance(self):
#         return self.balance

#     def get_accountno(self):
#         return self.account_no

# acc1 = Account(54000, 20317649403)

# print("Total Balance is : ", acc1.get_balance())
# print("Account number is :",acc1.get_accountno())

# print("Total Balance after debiting 20000:", acc1.debit(20000))
# print("Total Balance after crediting 60000:", acc1.credit(60000))
# print("Total Balance after debiting 35000:", acc1.debit(35000))
# print("Total Balance after crediting 95600:", acc1.credit(95600))


# ------Private (like):- attributes and method--------------------------------------------
# conceptual implementation in python
# private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
# #ex1
# class Account:
#     def __init__(self,accountNo,accountPassword):
#         self.acc_No = accountNo
#         self.__acc_Pass = accountPassword # use __

#     def reset_pass(self):
#         print(self.__acc_Pass)

# account1 =Account("20317649403","Dhruv@9099")

# print(account1.acc_No)
# print(account1.reset_pass())
# #print(account1.__acc_Pass) # error because it is now private


# ex2
# class Employee:
#     def __init__(self,name,id,salary):
#         self.__name = name
#         self.__emp_Id = id
#         self._salary = salary

#     def display_employee(self):
#         print("Name : ",self.__name,"\nID : ",self.__emp_Id,"\nSalary : ",self._salary)

# e1=Employee("John Doe",123456,10000)
# e1.display_employee()

# print("\nTrying to access  private attribute directly:\n Name : ",e1.__name) # error because it is now private
# print("\nName : ",e1.__name) # Error because _ or __ before a attribute

# // 3. Inheritance:- when one class (child/derived) derives the properties and methods of another  class(parent/base).--------------------------------------------------

# ---------Types of inheritance
# 1. Single , 2. Multi-level , 3. Multiple ----

# single

# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__ (self,name):
#         self.name=name
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.start())
# print(car2.stop())
# print(car2.color)

# //  multi level
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__ (self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type

# car1= Fortuner("diesel")
# car1.start()


# ///---multiple inheritance
#
# class A:
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to class B"
# class C(A,B):
#     varC = "Welcome to class C"
# c1 =C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


# //---Super Method:- ----------------------------------
# class Car:
#     def  __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__ (self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1= ToyotaCar("Supra","sport")
# print(car1.name ,"is" ,car1.type,"Car")

# // -------class method:-  it is bound to class and receives the class as an implicit first argument.

# class MyClass:
#     count = 0

#     def myMethod(cls):
#         cls.count += 1

# obj = MyClass()
# obj.myMethod()
# print(MyClass.count)


# //-------Static methods vs Class methods :---------

# # static method
# @staticmethod
# def add(a,b):
#     return a+b

# # class method
# @classmethod
# def mul(cls,a,b):
#     return a*b

# print(add(3,4))
# print(mul.__func__(2,3))   # using function attribute of descriptor type
# print(MyClass.mul(5,6))    # calling class method without object

# ex1
# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         Person.name=name # acces in atrr in class to change class object
# p1= Person()
# p1.changeName("dhruv")
# print(p1.name)
# print(Person.name)

# ex2
# class Person:
#     name = "anonymous"

#     # def changeName(self,name):
#     #     self.name=name
#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1= Person()
# p1.changeName("Maisuria")
# print(p1.name)
# print(Person.name)


# //--- Property:- we use @property decorator on any method in class to use the method as property. -----------------------------------------------
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+'%'

# stu1= Student(85,76,90)
# print(stu1.percentage)

# stu1.phy=70
# print(stu1.percentage)

# // Polymorphism: operator Overloading (a+b,a-b,a*b,a/b,a**b etc.)
# / 19-3-2024/ day-15
# //when the same operator is allowed to have different meaning according
# //to context.

# print(1+3) #4
# print('Hello'+'World') # Hello World # concatenate
# print([1,2,3]+[4,5]) #[1, 2, 3, 4, 5] #merge


# complex number
# class Complex:
#     def __init__(self,real,img) -> None:
#         self.real=real
#         self.img=img


#     def ShowNumber(self):
#         print(self.real,"i +",self.img,"j")

# num1 =Complex(1,3)
# num1.ShowNumber()

# num2 =Complex(52,36)
# num2.ShowNumber()

# /// use dunder function __add__,sub,__mul__,__truediv__,__mod__
# class Complex:
#     def __init__(self, real, img) -> None:
#         self.real = real
#         self.img = img

#     def ShowNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

#     def __mul__(self, num2):
#         newReal = self.real * num2.real
#         newImg = self.img * num2.img
#         return Complex(newReal, newImg)

#     def __truediv__(self, num2):
#         newReal = self.real / num2.real
#         newImg = self.img / num2.img
#         return Complex(newReal, newImg)


# num1 = Complex(100, 200)
# num1.ShowNumber()

# num2 = Complex(50, 100)
# num2.ShowNumber()

# # num3 = num1.add(num2)
# num3 = num1+num2  # usign dunder function use+
# print("Addition of two numbers :  ")
# num3.ShowNumber()

# num3 = num1-num2  # usign dunder function use+
# print("Subtraction of two numbers :  ")
# num3.ShowNumber()

# num3 = num1*num2  # usign dunder function use+
# print("multiplication of two numbers :  ")
# num3.ShowNumber()

# num3 = num1/num2  # usign dunder function use+
# print("division of two numbers :  ")
# num3.ShowNumber()

#---------Practice Questions---------------------------
# Ex1:- 
# // define a circle class to create a circle with radius r using the constructor.
# // define an Area() method of the class which calculates the area of circle.
# // define a perimeter () method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return (22/7) * self.radius **2
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(21)
# print("Area of the circle is ", c1.area())
# print("Perimeter of the circle is", c1.perimeter())



#// Ex2:-
#// define a employee class with attributes role,department and salary.this class also a
#// showDetails() method.
#//Create an Engineer class that inherits properties from Employee and has additional attributes name and age.

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def ShowDetails(self):
#         print("Name:", self.name)
#         print ("Department : ", self.dept)
#         print ("Role : ", self.role)
#         print ("Salary : ", self.salary)

    
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT","90,000")
    
# # e1 = Employee("Manager","HR","50,000")
# # e1.ShowDetails()

# engg1 =Engineer("Dhruv",21)
# engg1.ShowDetails()


#// Ex-3 :-
#// Create a class called Order which stores item and its price.
#// Use Dunder Function __gt__() to convert that:
#// order >1 order2 
#//     if price of order 1 > price of order2


class Order:
    def __init__ (self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,order2):
        return self.price > order2.price

order1 = Order("chips",20)
order2 = Order("tea",10)

print(order1 > order2 )   # True 














#//

#//

# 
# 
# 
# -
# -----------------------------------
# #------------------------------------