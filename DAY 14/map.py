#// map,filter and reduce in python

#map() function returns a map object(which is an iterator) of the 
# results after applying the given function to each item of a given
# iterable (list, tuple etc.

def square(x):  
    return x * x  
    
numbers = [1,2,3,4,5]  
squared_nums = list(map(square, numbers))  # apply the function to all elements of the list
print("Squared Numbers: ", squared_nums)

# Filtering a List Using filter() Function
# The filter() function returns an iterator containing those items from an iterable which satisfy the condition
# The filter() function takes two arguments -  A function and an iterable. It applies the given function on every element of the iterable and

# The filter() function takes two arguments -
# 1. A function (that defines the condition for filtering).
# 2. An iterable (the list on which we want to perform the operation).

# Let's say we have a list of names and we only want to keep the names that are longer than 6 characters. We can use filter() to do this task.
# Let's say we have a list of names and we want to get the names that    start with 'A'.    
names = ['Adam', 'Bob', 'Charlie', 'David']    
startWithA = list(filter(lambda x : x[0].lower() == 'a', names))      
print("Names starting with 'A':", startWithA)

# Reducing a List Using reduce() Function
from functools import reduce

# The reduce() function applies a function   of two arguments cumulatively to the items of an iterable, from left to right so as
# The reduce() function is used to apply a particular function passed in its argument to all the items of an iterable in a single line.
# The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right so as to reduce the iterable from left to right so as to
add = lambda x, y : x + y          
result = reduce(add, numbers)      # add all the elements of the list
print("Sum of numbers: ", result)


"""
The reduce() function is used to apply a particular function (that is already defined)  
to all the items in an input list (or any other iterable), so as to reduce the    
list to a single output value. It applies the given function by reducing the list to a single value.    

Syntax:
    reduce(function, sequence[, initializer ])
Parameters:
    function: This is the function that will be applied on each element of the list.
    It should take two arguments and return a single value.
    sequence: This is the iterable ( like list or string etc.) over which the function is applied.
    initializer: Optional parameter, this is the value to use if the iterable is empty. If it’s not provided then  it defaults to the first
"""