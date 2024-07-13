# def swap_without_temp(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b

# # Example usage
# x = 5
# y = 10

# x, y = swap_without_temp(x, y)

# print("After swapping: x =", x, ", y =", y)


# swapping variable wihtout using temporary variable

# def s():
#     x=5
#     y=10
#     x=x+y
#     y=x-y
#     x=x-y
#     return x,y

# print(s())

# del keyword 
# x=10
# y=[10,20,30]
# print(x, y)
# del y[0]
# del x
# print(x)
# print(y)


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg2": "Dhruv", "arg1": "Da", "arg3": "MA"}
# print(type(myFun(**kwargs)))
myFun(**kwargs)


print("g"*4)
print("f\n")
print("e \ ")
print("d \\ ")

