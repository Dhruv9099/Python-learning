class Person:
    def __init__(self,name,Occupation):
        print("HEy i am person")
        self.name= name
        self.occupation = Occupation
        
def info(self):
    print(f"{self.name} is a  {self.Occupation}")

a = Person("Dhruv","Developer")
b = Person("Divya","HR")
print(a.name,a.occupation)
print(b.name,b.occupation)

