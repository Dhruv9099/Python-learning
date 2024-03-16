#In Python, the raise keyword is used to explicitly raise an exception.
# This allows you to indicate that an error or 
#exceptional situation has occurred within your code. 


# a = int(input("Enter any value between 5 and 9: "))
# if (a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")
# else:
#     print("your entered  number is :",a)



a = (input("Enter string dont use quit word: "))
if (a == 'quit'):
    raise ValueError("dont write quit")
else:
    print("your entered  sentance is :", a)

#defining custom Exception

# Defining custom exceptions in Python allows you to 
#create your own exception types to handle specific errors 
#in a more meaningful way. You can do this by creating a 
#new class that inherits from the built-in Exception class 
#or one of its subclasses.

# class CustomError (Exception):
#     pass