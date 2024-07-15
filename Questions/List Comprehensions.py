"""
List comprehensions provide a concise way to create lists in Python. 
They consist of brackets containing an expression followed by a for clause,
and they can include optional if clauses.
"""


# Basic list comprehension
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# List comprehension with a condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [elem for row in matrix for elem in row]
print("Flattened matrix:", flattened)
