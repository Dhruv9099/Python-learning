# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:
# The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")
#output An exception occurred

# x=23
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# Example
# In this example, the try block does not generate any error:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


#   Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# x="dhruv"
# Example
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")



# Raise an exception, You can define what kind of error to raise, and the text to print to the user.


x = -1

if x > 0:
    raise Exception("Sorry, no numbers below zero")



x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")