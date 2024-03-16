# date 10/3/2024 SUNDAY
# --------------Loop in python-------------------------------------

# loop are used to repeat instuctions.
# There are two types of loops:
# 1. while loop : It will execute the block of code as long as the condition remains true.
#                If the condition becomes false, it  will stop executing the code inside the loop.

# 2. for loop   : It is an another way of looping through a sequence (that can be changed into iterable).
#               In Python, sequences are data types that can be iterated upon like strings and tuples. Examples include lists, dictionaries,
#               A for loop has three parts separated by colons(:)
#                    i) An initialization statement (which is executed once before the execution of the loop’s body portion.)
#                    i) An initialization expression (which is executed once before the execution of the loop): This is where we initialize our counter variable.
#                   1. The variable that you want to iterate over.
#                      This variable represents each element from the given iterable one by one.
#                   2. The iterator object or the sequence that you want to iterate over.
#                   3. The optional statement that executes on each iteration.

# Let's see both type of loops using examples:

# Example of While Loop
# i = 0
# while i < 5:     # As long as i is less than 5, keep executing this block of code.
#     print(i)
#     i += 1       # Incrementing value of 'i' by 1 after each execution.
# print("Outside the loop")

# Output:
# 0
# 1
# 2
# 3
# 4
# Outside the loop

# i=1
# while i<=3:
#     print("Hello World!",i)
# i +=1

# ex1 # print number from 1 to 100

# i=1
# while i<=100:       # stopping condition
#     print(i)
#     i+=1

# ex 2 print numver from 100 to 1
# i =100
# while i>=1:
#     print(i)
#     i-=1

# ex 3  Print the Multiplication table of number n
# n=int(input("Enter a multiplication table Number :"))
# i=1
# while i<=10:
#     print(n*i)
#     i=i+1

# ex 4  Print the elements ofthe follwoing list using a loop
# [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# # print(len(nums))
# indx = 0
# while indx < len(nums):
#     print(nums[indx])
#     indx += 1

# ex 5  search for a number x in this tuple using loop

# [1,4,9,16,25,36,49,64,81,100]

# @sol1
# numbers = (1, 4, 9, 16, 25, 36, 49,36, 64, 81, 100)
# x = 36
# i =0
# while i <  len(numbers):
#     if numbers[i] == x:
#         print("Number is found at position",i)
#         break
#     else:
#         i += 1

# #sol2
# y=9
# i = 0
# while i < len(numbers):
#     if (numbers[i] == y):
#         print("Found at index", i)
#     i += 1



# -------------------Continue and break --------------------------------

# i =0
# while i<=5:
#     if (i==3):
#         i+=1
#         continue #skip 3
#     print(i)
#     i+=1
# print("out of the loop")

# i =0
# while i<=5:
#     if (i==3):
#         i+=1
#         break # brack  to exit from the loop at 3 rd iteration.
#     print(i)
#     i+=1
# print("out of the loop")


# -----date 13/3/2024--goto day 9-------------Loop are used for sequential traversal.for traversing list,string, tuples etc.-----------------------------------

nums =[1,2,3,4,5]
for val in nums:
    print(val*2) 
print("Out of for loop")












# ---------------------------------------------------

# ---------------------------------------------------
# ---------------------------------------------------

















# #Example of For Loop
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:         # Variable 'fruit' will take each value of list 'fruits' one by one.
#     print(fruit)             # Printing each fruit name.

# Output:
# apple
# banana
# cherry

# Nested Loops
# Sometimes we need to run a loop inside another loop. That's called nested loops.

# Example of Nested Loops Using  While Loop




# ---------------------------------------------------

# ---------------------------------------------------

# ---------------------------------------------------
# ---------------------------------------------------

# ---------------------------------------------------

# ---------------------------------------------------

# ---------------------------------------------------
