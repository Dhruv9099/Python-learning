
# ---------------------------------------------------
# light = input("Light Color : ")

# if (light == "Red"):
#     print("Stop")

# elif(light == "Yellow"):
#     print("Slow Down")

# elif (light== "Green"):  # White or Green
#     print("Go ")
# else:
#     print("Light is broken")
# ---------------------------------------------------
# ----print output for
# ----A =5 & G=M , A=2 & G=F

# A= int(input("A : "))
# G= (input("M/F : "))
# if ((A==1 or A== 2) and ( G=="M")):   #AND  Operator
#     print ("A is 1 or 2and G=M")
# elif ((A==3 or A== 4) and ( G=="F")):
#     print("A is 3 or 4 and m=F")
# elif (A==5  and G=="M"):
#     print("A is 5 And G is ME")
# else:
#     print("no match")

# --------------- single line If I Ternary Opreator------------------------------------

# food = input("Food :")
# eat ="yes " if food == "Cake" else "No"
# print(eat)

# foods = input("Food :")
# print("Sweet") if foods == "Cake" or foods=="Jalebi" else print("Not Sweet")

# <var> = (false_val,True_val)[<Condition>]
# age = int(input("Age :"))
# vote =("No you are not eligible for vote","Yes You can Vote") [age>=18]
# print(vote)

# sal= float(input("salary: "))
# tax= sal*(0.1,0.2) [sal>=50000]
# print("Tax amount is ", tax)

# --------------calculates simple interest -------------------------------------

# a = float(input("A : "))
# b = float(input("B : "))
# c = float(input("C : "))
# intrest = (a*b*c)/100
# print("Interst Amount is", intrest)

# ------------converting Currency-------------------------------------

# usd = float(input("Enter USD :"))
# rates = {"INR":76,"EUR":90} 
# currency = input("Enter Country Currency Code :  ") 
# if currency in rates:
#     print(usd * rates[currency])
# else:
#     print("Currency Not Supported") 

# -------------------Relational Operator--------------------------------
# a= 50
# b=20
# c=20
# print(a!=b) #True
# print(b==c) #True
# print(b>=a) #False
# print(b<=a) #True
# print(a>b)  #True
# print(a<b)  #False


# num =10
# num =num +20  # 10+20 = 30
# num += -10   #  30-10 = 20
# print("Num is ",num) #20


# -------------- LOgical operators-------------------------------------
# a =50
# b= 40
# print(not False) # true beacue  not false is True
# print(not (a>b)) #False  because not of False is True and a>b is False. So, not False is True       

#AND  operator

# val1 = True
# Val2 =True # put True then And opertaion will excute True
# print("AND OPERATOR:", val1 and Val2)
# print("OR OPERATOR:", val1 or Val2)

# val3 =33
# Val4 = 52

# print("AND OPERATOR examples:", (val3 ==Val4 and (val3 >= Val4))) # False
# print("AND OPERATOR examples:", (val3 !=Val4 and (val3 >= Val4))) # false
# print("AND OPERATOR examples:", (val3 !=Val4 and (val3 <= Val4))) # True both is satifed
# # --or--
# print("OR OPERATOR:", (val3==Val4 or (val3> Val4))) # False beacue both values are not satified
# print("OR OPERATOR:", (val3!=Val4 or (val3> Val4))) # Truefirst value satfied
# print("OR OPERATOR:", (val3!=Val4 or (val3< Val4))) # True both value satfied


# ----------------Type Conversion-----------------------------------
# a =2    #int
# b=4.25  # float
# sum =a +b # type convision  6.25 answer
# print(sum)
# # Type Conversion string to int
# c =int("2")
# # d =int("Dhrurv") # not possible char to int, float is not working
# e=float("2")     # "2" to float 2.0
# print(type(c),type(e))


# -----------------Stings ----------------------------------

#         #Concatenation
# str1 ="Hello"
# str2 ="World"
# concat_string = str1+ " "+ str2+"!"
# print(concat_string) # output : Hello World!

#         #Multiplication
# repeat_string="Python"*3
# print(repeat_string)  # output : PythonPythonPython

#         #Finding length of a String
# length_of_string = len("Programming")
# print(length_of_string) # output :11 

#         #Checking if substring exists in the main string
# is_present = "I love Python".__contains__("love")
# print(is_present) # output : True

#             #Finding out what character/index at which position it occurs
# find_char = "I love Python".find('o')
# print(find_char) # output : 3

            # index values retun
# indexnum ="I code Python"
# indexnumber =indexnum[3]
# print("indexnum 3",indexnum[3]) #output :  o

#             #Joining strings
# split_string = "This is a sample sentence.".split()
# join_strings = "-".join(split_string)
# print(join_strings) # output : This-is-a-sample-sentence.

            # #Slicing - accseing part of string
# App ="123456789"
# fruit = App [3:8]   # from index 3 to 8 (7 and  8 are included)
# print(fruit)       # output : ru

        # Endswith
# str="hello world I am Coder. How are you?"
# print(str)
# print(str.endswith("o"))    #True or False ans False
# print(str.endswith("?"))    #True or False ans True

#     #Catipalize      1st letter captial
# print(str.capitalize())       #Output : Hello world i am coder

    # #replace repalce all orrcurences of old to new
# print(str.replace("world","Universe"))     # Output : hello Universe I am Coder. How are you?

    # COunt  counts the occurences of substaction
# str1="hello world I am Coder. world How are you?"
# print(str1.count("world"))      # Output 2

    # Check if numeber is mulltiply of 7 or not'

# x = int(input("Enter Number:"))
# if (x% 7 ==0):
#     print(x, " is Multiple of 7")    
# else:
#     print(x, " is Not A Multiple of 7")



#--------------Lists------------------------
# marks =  [56,78,90,65,89]
# print(marks)                    #print list
# print(len(marks))               # lenght of list
# print(marks[1])                 # index 1 value 78
# print(marks[2])                 # index 1 value 90
# print(type(marks))              # type of marks  <class 'list'>
# print ("Maximum value in list is:", max(marks))         #output : Max

# print("print index 1:3",marks[1:3]) # list slicing  from 1 to 3 so out put will be [78,90] 1:3 in 1 count and 3 exclued
# # ex2
# student =["karan", 89,3,"Delhi"]
# print(student)
# print(student[0])                # karan
# student[0]  = "Arjun"      # change value of element
# print(student)

#ex3 list methods
list [2,4,6,5,7]
print(list)

# print(list.append(9))           # add  element at last    -> [2,4,6,5,7,9]
# print("append list",list)

# print(list.sort())                           #  sort elements          -> [5,6,7,9,2,4]
# print("Sorted list",list)

# print(list.sort(reverse=True()))           # reverse order  decensind order       
# print("deseding order list",list)

# print(list.reverse())           # reverse order           -> [9,2,4,7,6,5]

# print(list.insert(1,10))        # insert element at pos   -> [5,10,6,7,9,2,4]

# print(list.remove(9))           # remove element         -> [5,10,6,7,2,4]

# print(list.pop(1))              # pop element from pos -> [5,6,7,2,4]


