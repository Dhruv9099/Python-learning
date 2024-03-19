# python can be used to perform operation on a file(read write data)
# type of all files
# 1. text files : .txt , .doc, .rtf etc
# 2. binary files: images, videos,.mp4,.mov,.png,.jpeg etc.


# open ,read and close file

# we have to open file before reading or writing.
# f=open("file_name",'operation')    # 'r' for read only,'w' for write only,'a' for append('a'+ will add the content at
# file = open("sample.txt", "r")   # r for read mode , w for write mode , a for append mode
# print(file.read())    # it  will print whole content of the file
# file.close()          # after using we must close the file otherwise it may create problem in    future
#                       # if you don't close the file then your system will run out of memory

"""
Syntax :
     fp = open(filename,mode)
     filename is required , mode is also required
     modes are :
         Mode    | Description
        ---------|-------------------------------
           'r'   | Read only
           'w'   | Write only (overwrites existing file)
           'a'   | Append (write only if file exists)
           'ab'  | Append binary (works like 'a' but doesn't convert \n to \r\n)
           'r+'  | Read & Write (existing file)
           'w+'  | Read & Write (create new file if not exist)
           'c'   | Create (Creates new file and writes to it). Rais es an error if the file already exists.
           'x'   | Create and exclusive (Raises an OSError if the file already exists.).
           'X'   | Create and exclusive (like 'x' but raises an IOError instead of OSError if the file already exists
"""
#--------------------------------------------------
#// read method
# f = open("file.txt","r")
# data= f.read()
# print(data)
# print(type(data))
# f.close() 

# //ex2 of read method
# f = open("file.txt","r")
# data= f.read(5) # specify characters
# print(data)
# f.close() 

# //ex3 of read method f.readline()
# f = open("file.txt","r")
# line1= f.readline() # reads one line at a time
# print(line1)

# line2= f.readline() # reads one line at a time
# print(line2)

# line3= f.readline() # reads one line at a time
# print(line3)

# f.close() 

#--------------------------------------------------
#write  method -- files.txt

# f = open('files.txt', 'w')
# f.write("Hello World!") 
# print("File written successfully.")
# f.close()

# #add \n for next line in text file

# f = open('files.txt','a')
# f.write("\nI love Python!")
# f.close()

# #append mode

# f =open ('files.txt', 'a+') 
# text = f.read()
# print(text)
# f.close()

# f=open("file.txt","+a" ) # append mode, add text at end of file
# f.write("\nHello World!")
# print ("Text written successfully")
# f.close()

#---------------------------------------------------
#additional methods:
'''
- seek(): Moves the cursor position to specific point in the file.
- tell(): Returns current location of the cursor.
'''
# seek and tell method 


# // ------With syntax----------------
# // with open("demo.txt","a") as f:
# // data= f.read()


# with open("file.txt","r") as f:
#     data= f.read()
#     print(data)
    
# with open("file.txt","w") as f:
#   f.write("New DATA ENTRY")

#---------Deleting a file-----------------------------------------
#// using the os module:- module like a code library is a file written by another programmer that generally has a functions we can use.
#// import os
#// os.remove(filename)

# f = open('sample.txt', 'w')
# f.write("Hello World!") 
# print("File written successfully.")
# f.close()
#// delete sample.txt
# import os
# os.remove("sample.txt")
#--------------------------------------------------

# with open ("prac.txt","w") as f:
#     f.write("hi everyone \n we are leaning fileIO \n using java.\n i like programming in java ")
# print("File written successfully.")
# f.close()

# ///
# with open("prac.txt","r") as f:
#     data =f.read()
# new_data = data.replace("java","python")
# print(new_data)
# with  open ('prac.txt','w')as f :
#     f.write(new_data)


#--------------------------------------------------
# ///
# word= "python"
# with open("prac.txt","r") as f:
#     data =f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")
        
        
#///
# def check_for_line():
#     word="python"
#     data=True
#     line_no=1
#     with open("prac.txt","r")as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1
# print(check_for_line())

#-------#-------------------------------------------
#// from a file containing numbers separated by comma ,print the count of even numbers.
with open("pract.txt","r") as f:
    data= f.read()
    print(data)
#1,2,3,45,85,62,56,95,64,102
    
nums = [int(i) for i in data.split(',')]
even_count = sum([1 for num in nums if num % 2 ==0])
print(even_count)














