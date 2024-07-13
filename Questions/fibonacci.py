#  --------Fibonacci number --------
"""Fibonacci Number
A Fibonacci number is part of a sequence where each number
is the sum of the two preceding ones, usually starting with 0 and 1.
The sequence commonly starts as 0, 1, 1, 2, 3, 5, 8, and so on. 
Mathematically, it is defined as:
F(n)=F(n−1)+F(n−2)
F(0)=0
F(1)=1
"""
# 
# Python Program for How to check if a given number is Fibonacci number?
# python program to check if x is a perfect square
import math

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x
# Returns true if n is a Fibonacci Number, else false

def isFibonacci(n):
	# n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
	# is a perfect square
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

# A utility function to test above functions
for i in range(1, 11):
	if (isFibonacci(i) == True): 
		print(i, "is a Fibonacci Number")
	else:
		print(i, "is a not Fibonacci Number ")



# Iterative Method

def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

n = int(input("Enter the position of the Fibonacci number: "))
print(f"The {n}th Fibonacci number (iterative) is: {fibonacci_iterative(n)}")


# Recursive Method

def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter the position of the Fibonacci number: "))
print(f"The {n}th Fibonacci number (recursive) is: {fibonacci_recursive(n)}")


# Using Memoization

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

n = int(input("Enter the position of the Fibonacci number: "))
print(f"The {n}th Fibonacci number (with memoization) is: {fibonacci_memo(n)}")
