# A function is a block of code which only runs when it is called.
# To call a function, use the function name followed by parenthesis
def my_function():
    print("Hello from a function")


my_function()

# Keyword Arguments


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Default Parameter Value
# The following example shows how to use a default parameter value.

def my_function(country="Norway"):
    print("I am from " + country)


my_function()  # default value
my_function("Sweden")
my_function("India")
my_function("Brazil")


# without function
a = 9
b = 8
gmean = (a*b)/(a+b)
print("9 and 8 gmean is " + str(gmean))

c = 5
d = 7
gmean1 = (c*d)/(c+d)
print("8 and 7 gmean is " + str(gmean1))

# with Function


def calculateGmean(a, b):
    Gmean = (a*b)/(a+b)
    print(Gmean)


def isGreater(a, b):
    if (a > b):
        print("First is greater than second")
    else:
        print("Second is greater than First")


isGreater(a, b)
calculateGmean(a, b)

isGreater(c, d)
calculateGmean(c, d)
