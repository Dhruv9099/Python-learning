# -------- palindrome Number --------
"""Palindrome
A palindrome is a sequence of characters 
(such as a word, phrase, number, or other sequences) 
that reads the same forward and backward, ignoring spaces, punctuation, 
and capitalization. Examples include "madam," "racecar," and "121"."""


# Method 1: Palindrome Program in Python using While Loop

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(f"The number {temp} is a palindrome!")
else:
    print(f"The number {temp} isn't a palindrome!")


# Method 2: Palindrome in Python using Built-in Function

def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))
 
# Get the number from the user
n = int(input("Enter number: "))
 
# Check if the number is a palindrome
if is_palindrome(n):
  print("The number is a palindrome!")
else:
  print("The number is not a palindrome.")
  
  
  
# Method 3: Palindrome in Python using Recursion
def is_palindrome(n, temp, rev=0):
    if n == 0:
        if temp == rev:
            return "The number is a palindrome!"
        else:
            return "The number isn't a palindrome!"
    else:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
        return is_palindrome(n, temp, rev)
 
n = int(input("Enter number:"))
result = is_palindrome(n, n)
print(result)


# Method 4: Palindrome in Python using Slicing
def is_palindrome(n):
    # Convert the number to a string
    num_str = str(n)
 
    # Use slicing to reverse the string
    reversed_str = num_str[::-1]
 
    # Compare the original string with the reversed string
    return num_str == reversed_str
 
n = int(input("Enter a number:"))
 
if is_palindrome(n):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")
