class Emp:
    def __init__(self,name,salary) :
        self.name =name
        self.salary =salary

    def getSalary(self):
        return self.salary
    
Emp1 = Emp("Abhi","35499")
print(Emp1.name)
print(Emp1.salary)
print(Emp1.getSalary())

#Inheritance parent class and child  class 