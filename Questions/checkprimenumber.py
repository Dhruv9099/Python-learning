# -------- check whether number is prime or not --------

"""Prime Number
A prime number is a natural number greater than 1 that has no positive divisors
other than 1 and itself. In other words, it cannot be formed by multiplying two 
smaller natural numbers. Examples of prime numbers include 2, 3, 5, 7, 11, 
and so on. The number 2 is the only even prime number."""

num = int(input("Enter the number to check prime or not: "))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")




# --------Check Prime Numbers Using Recursion --------

from math import sqrt

def Prime(number,itr):  #prime function to check given number prime or not
  if itr == 1:   #base condition
    return True
  if number % itr == 0:  #if given number divided by itr or not
    return False
  if Prime(number,itr-1) == False:   #Recursive function Call
    return False 
    
  return True

num = int(input("enter number chekc prime or not using recursion method: "))

itr = int(sqrt(num)+1)

print(Prime(num,itr))

