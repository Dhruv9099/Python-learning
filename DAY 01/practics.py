# date 05/3/2024
# 1. Variables and Data Types:


name = "Alice"
age = 25
height = 5.9

print(f"Name: {name}, Age: {age}, Height: {height}")
# Description: Demonstrates the creation of variables with different data types (string, integer, and float) and printing them.

# 2. Lists and Indexing:


fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Outputs: banana
# Description: Introduces lists and shows how to access elements using indexing.
# 3. Conditional Statements:


x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# Description: Illustrates the use of if-else statements for decision-making based on conditions.

# 4. Loops - For and While:

for i in range(5):
    print(i)
# Description: Demonstrates a for loop that iterates over a range of numbers.

# 5. Functions:


def greet(name):
    print("Hello, " + name + "!")


greet("Bob")
# Description: Defines a simple function that takes a parameter and prints a greeting

# 5.tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
 