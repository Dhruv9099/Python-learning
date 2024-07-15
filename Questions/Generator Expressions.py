# Generator expressions are similar to list comprehensions but use parentheses instead of brackets. They produce items one at a time and are more memory efficient than list comprehensions.

# Generator expression
squares_gen = (x**2 for x in range(10))

# Consuming the generator
for square in squares_gen:
    print(square)

# Creating a list from the generator
squares_list = list(squares_gen)  # Note: the generator is exhausted at this point
print("Squares list from generator:", squares_list)
