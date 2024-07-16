"""# Exception is runtime error that terminates the exceution of
# the program
# Exception Handling generates a message in correspondence 
#5th the occurence of an error ans =d takes the right step to handle it.
"""
#error types -compile ,logical, runtime error

# try : run code
# except: error message or peice of code when there is an Exception
# else: no Exception ? runthis code
# finally: always runs irrespective of whether there was an exception or not?


a =input("Enter the number: ")
print(f"multiplication table of {a} is : ")
try:
    for i in range (1,11):
        print(f"{int(a)} X{i} = {int(a)*i}")
except Exception as e:
    print("you  have entered wrong input, enter string value", e)

print("this is below partif  the error  come beacuse some one add string in integer") 
print("end of the program")



try:
    number =int(input("Enter the integer : "))
    # a =[6,4]
    # print(a[number])
    print(f"your number is {number}")
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")


# you can write try block without any except blocks
    #you can wirte serveral except blocks for single try block
    # you can write multiple except blocks to handle multiple exceptions
    # you can write exception as an object 
    # you can write multiple exception within tuple

# a =10
# b= 0
# c =a/b
# print("a/b is ", c)

# try:
#     a = int(input(  "enter a : "))
#     b = int(input("enter b :"))
#     c = a / b
# except:
#     print("Cant divide with zero")




a = int(input(  "enter a : "))
b = int(input("enter b :"))
try:
    print(a/b)
    print("a/b is: ", a/b)
except:
    print("don't divde by Zero")
print("Completed")



