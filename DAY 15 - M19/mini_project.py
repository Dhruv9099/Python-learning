# ---------------------------------------------------------------------
# Guess The Number

# import random
# random.randint(1, 50)

# number = random.randint(1, 50)
# # print(number)

# while True:
#     userChoice = input("Guess the Number or Quit(Q): ")
#     if(userChoice =="Q"):
#         break

#     userChoice=int(userChoice)
#     if (userChoice == number):
#         print("Success: correct Guess.")
#         break
#     elif (userChoice < number):
#         print("Too low!")
#     else:
#         print("Too high!")
# print("----- Game Over! -----")


# ---------------------------------------------------------------------
# Random Password Generator

import random
import string

# print(string.__all__)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
pass_len = 12
keyborad_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(keyborad_values)
    
print("your random password is: ", password)


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

#

# ---------------------------------------------------------------------
