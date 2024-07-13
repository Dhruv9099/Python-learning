

# Write a program to check if a number is even or odd. 

n=10
if n%2==0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")
    
# Write a program to find the sum of all numbers in a list. 

l=[1,2,3,4,5]
sum=0
for i in l:
    sum+=i
print(sum) 

# Write a program to find the largest number in a list. 

l=[17,25,13,34,59,20]
for i in l:
    max_num = max(l)
    print("max num in l : ", max_num)
    break

# Write a program to reverse a string.

string1 ="DHRUV MAISURIA"

string2=""

for i in string1:
    string2=i+string2
print(string2)


# Write a program to check if a string is a palindrome. 
# method 1
n= 454
# n=int(input("Enter number:"))
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


# method 2
def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))
 
# Get the number from the user
# n = int(input("Enter number: "))
n = 45
 
# Check if the number is a palindrome
if is_palindrome(n):
  print(f"The number {n} is a palindrome!")
else:
  print(f"The number {n} is not a palindrome.")

# Write a program to convert Celsius to Fahrenheit.
# I would use the conversion formula:
# Fahrenheit = Celsius * 9/5 + 32,
# to calculate the equivalent temperature in Fahrenheit.  

# celsius = int(input("Enter celsius: "))
celsius = 20
Fahrenheit = celsius * 9/5 +32 
print(f"fehrenheit of celsius {celsius} is {Fahrenheit} fehrenheit.")



# datetime standard library 
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)
# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print(formatted_datetime)






# sys library

import sys

# Check the number of command-line arguments
num_arguments = len(sys.argv)

# Display the script name and command-line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]

print(f"Script: {script_name}")
print(f"Number of arguments: {num_arguments - 1}")
print(f"Arguments: {arguments}")



# math library

import math

# Input a number
input_number = 25

# Calculate the square root using the math module
square_root = math.sqrt(input_number)

# Display the result
print(f"The square root of {input_number} is: {square_root}")







































# # Implement an LRU (Least Recently Used) Cache.
# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         else:
#             # Move the accessed key to the end to show that it was recently used
#             self.cache.move_to_end(key)
#             return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             # Move the existing key to the end to show that it was recently used
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             # Pop the first item from the OrderedDict (the least recently used element)
#             self.cache.popitem(last=False)

# # Example usage
# lru_cache = LRUCache(2)
# lru_cache.put(1, 1)
# lru_cache.put(2, 2)
# print(lru_cache.get(1))    # returns 1
# lru_cache.put(3, 3)        # evicts key 2
# print(lru_cache.get(2))    # returns -1 (not found)
# lru_cache.put(4, 4)        # evicts key 1
# print(lru_cache.get(1))    # returns -1 (not found)
# print(lru_cache.get(3))    # returns 3
# print(lru_cache.get(4))    # returns 4
