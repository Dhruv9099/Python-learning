# -----date 13/3/2024--in  day 9------------

# -Loop are used for sequential traversal.
# for traversing list,string, tuples etc.-----------------------------------


# list=[1,2,3,4,5,6]
# for val in list:
#     print(val)

# string =["apple","banana","cherry"]
# for val in string:
#     print(val)
    

# tup= (1,2,3,4,5,6,7,8,9)
# for num in tup:
#     print(num)

# str ="Dhruv Maisuria"
# for char in str:
#     if(char == 'x'):
#         print('x found')
#         break
#     print(char)
# else:
#     print("END not found")


# numbers = (1, 4, 9, 16, 25, 36, 49,36, 64, 81, 100)
# x=49
# idx=0
# for el in numbers:
#     if(el==x):
#         print("49 number found at index: ", idx)
#         break
#     idx+=1
# else:
#     print("49 Number is not present in the sequence.")


#--------------RANGE---------------------------------------------------------
#-------Range function return a sequence of number , starting from 0 by default,
# and increments by 1 (by default, and stops before a specified number.)--------------------------------------------------
# range(start?, stop), step?) /?= optional

# seq =range(5)

# for i in range():
#     print(i)

# for i in range(2,10):
#     print("start,stop (2,10): ",i)

# for i in range(2,10,2):
#     print("start,stop, step (2,10,2):",i)
    
# for i in range(2,10,2):
#     print("even:",i)
    
# for i in range(1,10,2):
#     print("Odd:",i)
    
#--- print 1 to 100
# for i in range(1,101):
#     print(i)
        
    
#--- print 100 to 1
# for i in range(100,0,-1): # start, stop, step
#     print(i)


# --- print the multiplication table of number n
# n  = int(input("Enter any number : "))
# for i in range(1,11):
#     print("multiplication table of",n,"*",i,":", n*i)


# ---------pass statement: pass is null statement that does nothing.
# -------- it is used as a placeholder for future code.
# for i in range(9):
#     pass        # skip the loop
# print("Hello World")
# i=[5,566,2,542,52]
# i=0
# if i>5:
#     print(i ,"grether than 5")
#     pass
# print("i pass is grearther than 5")
# i=i+1


# #--- find the sum of first n number using while loop
# n = 5
# sum = 0
# count = 1

# while count <= n:
#     sum += count
#     count += 1

# print("The sum of the first", n, "numbers is:", sum)



#--- find the factorial of first n number using for loop
n = 5
factorial = 1

for i in range(1, n+1):
    factorial *= i
    print("Factorial of", n, "is:", factorial)


print("Factorial of", n, "is:", factorial)
