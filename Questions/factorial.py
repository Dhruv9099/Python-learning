"""The factorial of a non-negative integer n is the product of all positive 
integers less than or equal to n. It is denoted byn! and is defined as:


n!=n×(n−1)×(n−2)×…×1

For 
n=0, the factorial is defined as:
0!=1
"""
# factorial of given number
def factorial(n):
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# Driver Code
num = 5
print("Factorial of",num,"is",factorial(num))