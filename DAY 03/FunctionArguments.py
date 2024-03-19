def average(a, b):
    print("the average is", (a+b/2))
average(4, 6)


def average(a=9, b=41):
    print("the defulat argements average is", (a+b/2))
average()


def average(a=9, b=41):
    print("the average is", (a+b/2))
average(4, 22)


def name(fname, lname):
    print("hello you are ", fname, " " + lname + ".")
name("John", "Doe")


def name(fname="dhruv", lname="Maisuria"):
    print("hello you are ", fname, " " + lname + ".")
name()

# paas numbers * before the parameter name while defing the function.

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is :", sum / len(numbers))
average(3, 3)


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)


c = average(5, 6, 7, 1)
print(c)


def greetHello():
    print("HELLO")
    print("DHRUV")
    print("MAISURIA")


print("Executing Function")

greetHello()
print("Program  Ends Here.")

# function with arguments


def greetHello(name, lastname):
    print("HELLO " + name + " "+lastname)
    st = f"HII ,\n THIS is your surname {lastname} and first name is {name} "
    print(st)
    print("NIce to meet you")


greetHello("Dhrumil", "Shah")
greetHello("Dhruv", "MAosuria")
greetHello("Krunal", "Rajput")
print("Executing Function")

print("Program  Ends Here.")




def average(a,b):
    return(a+b)/2

print(average(444,222))