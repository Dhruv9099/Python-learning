# The enumerate () method adds a counter to an iterable and returns it
#  in the form of an enumerating object. This enumerated object can then be
# used directly for loops or converted into a list of tuples 
# using the list() function.

# Syntax: enumerate(iterable, start=0)

# Parameters:

# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
# Return: Returns an iterator with index and element pairs from the original iterable


Marks = [12, 23, 43, 65, 1, 2, 55, 23]
index = 0

for Mark in Marks:
    print(Mark)
    if (index == 3):
        print("Dhruv,Awasome!")
    index += 1



for index, Mark in enumerate(Marks): 
    print(Mark)
    if (index == 3):
        print("Dhruv,Awasome!")
    index += 1