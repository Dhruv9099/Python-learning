# Python Modules
# A module is the same as a code library.

# A file containing a set of functions you want to include in your application.module we just created, by using the import statement:
#MATH MODULE

import math

# Calling function from imported module
print("Math factorial: ", math.factorial(5))


lists = [2, 3, 4, 5, 6]
factorial_list = []

for i in lists:
    i += 1
    factorial_list.append(math.factorial(i))

print("lists with factorial: ", factorial_list)

a= math.tan(45.0)
print(a)



lst1 = [15, 14, 13, 12, 11, 10]
lst2 = [10, 11, 12, 13, 14, 15]
x= zip(lst1, lst2)
print(x)
print(set(x))