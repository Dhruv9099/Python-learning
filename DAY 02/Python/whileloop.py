#while loops: With the while loop we can execute a set of statements as long as a condition is true.
#Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
  
# Exit the loop when i is 3:
print("Break  in while loop if i == 3: ---")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Continue to the next iteration if i is 3:
print("Continue statement below:  if i == 3:continue")
i = 0
while i < 6:
  i += 1
  if i == 3:
    
    continue
  print(i)
  

  # Do while loop
  
  
  # Example usage of the id() function
my_list = [1, 2, 3]

# Get the identity of the list
list_id = id(my_list)

# Print the result
print("Identity of my_list:", list_id)



# Swapping variables without using a temporary variable
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage
x = 5
y = 10
print(" witout swapping x: ",x ,"; y: ",y)
x, y = swap_without_temp(x, y)

print("After swapping: x =", x, ", y =", y)

# method 2

def swp(a,b):
  a,b =b,a
  return a,b

swp(5,10)