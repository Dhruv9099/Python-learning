# Imperative Programming
# Imperative programming is a paradigm that uses statements to change a program's state. It focuses on describing how a program operates.

# Imperative approach to summing a list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum:", sum_list(numbers))



# Functional Programming
# Functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data.

# Functional approach to summing a list
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum_numbers)