#-----------------------tuples------# -----------Tuples-----------------------

    # build in datatype that lets us create immutable sequences of values--------------------
# x = (1, 2, 'hello', 4.5,2)                       # tuple with mixed data types
# print(type(x))                          #<class 'tuple'>
# print(x)                             # print X
# print(x[1]) 

# tuples methods 
# print(x.index(2))
# print(x.count(2))

# ex3
# Movie = []
# movie1= input( "Enter 1 movie name: ")         # user inputs
# movie2= input( "Enter 2 movie name: ")         # user inputs
# Movie.append(movie1)
# Movie.append(movie2)
# Movie.append(input( "Enter 3 movie name: "))         # user inputs directly append
# # ##Movie.append(movie3)

# print(Movie)

#ex4 check if a list contains a palindrome of elements .(palindrone means maam= maam )
# list=[1,2,3,2,1]
# print("Is the list a palindrome? ", end="")
# if list == list[::-1]:
#    print("Yes.")
# else:
#    print("No.")


#using copy method palindeom

# list1=[1,2,1]
# # list2=[1,2,3]
# copylist1 =list1.copy()
# copylist1.reverse()
# if (copylist1==list1):
#      print ("The list is a palindrome!")
# else:
#     print("The list is not a palindrome!")

#EX
    #count the number of students with the 'A' grade in following tuple.
# grade =("C","A","A","D","B","A","B","A")
# print( "students with the 'A' grade:",grade.count("A"))




# --------------   Dictonary ----------  ---------------------------
# //dictonaries are used to store data values in key:value pairs. 
#  // they are unordered , mutable (changable) and dont allow duplicates keys

# info ={
#     "name":"John Doe",
#     "age":30,
#     "city":"New York",
#     "is Adult":True,
#     "subject": ["math","english"],
#     "marks" : [95,98]
#     }                           
# print(info)
# print("Age",info["age"])
# print("City",info["city"])
# print("Subject",info["subject"])


# info["name"] ="Jane Smith"      # update name
# info["surname"] ="Doe"          # add  new key value pair in exsting dict
# print(info)


#// new dictionary
# Student ={
#     "name":"Dhruv ",
#         "subject": {
#             "math":85,
#             "english":95,
#             "history":76
#         },
#         "roll_no":123
#     }   

# print(Student)
# print(Student.keys())                    #return all keys.4
# print(list(Student.keys( )))             # return list of keys.
# print(len(Student))                     #lenght of student

# print(Student.values())                                #return all values.
# print(list(Student.values()))                         #returns a list of the object’s values.

    # return all (key,val)pairs as tuples.

# print(Student.items())                               # returns a list of tuples containing key-value pairs.
# print(list(Student.items()))      # same as above but returns a list instead of a dictionary view object.
# pairs= list(Student.items())
# print("pairs with list in  items of student ",pairs)


                #return the key according to value. myDict.get(key[,default])
# print(Student["name2"])                 # if there is no such key it will give error so we can provide default value like this:
                                            ## print(Student.get("name"))              # get value by passing key
# print(Student.get["name2"])               # if there is no such key it will give None

                # insert the specified items to dictionaries
# Student.update({"city":"mumbai"})
# print(Student)


# ----------------------SET in Python-----------------------------

#// set collection of unordered items, each elelment in set mustbe unique and immmutable.
# in set list and dict not added.
# collection ={1,2,3,4,5}            #set
# print("collection set :",collection)
# print(type(collection))

# #ex2
# collection ={1,1,1,2,2,3,4,"Hello","Hello","World"}   #set only add one time for  duplicate element.
# print("after removing duplicates from set:", collection)
# print(len(collection))              #length of set

##ex3
# cset=set()      #empty set
# print("empty set :", cset)

#----------set method ---------- mutable but elemrnt is immutable------------------
# // set.add(x)        adds an element
# //set.remove(x)     removes an element x from the set; it should be present in
# //set.clear()       empties the set
# //set.pop()         removes a random value

    # create collection empty set
# collection = set() 
#      # // set.add(x)  
# collection.add(1)              
# collection.add(2)
# collection.add(3)
# collection.add(2)
# print(collection)
        
     # //set.remove(x)
# collection.remove(2)   
# print(collection)

    # //set.clear()
# collection.clear( )             #empyt the set
# print(collection)

    # //set.pop() 
# print(collection.pop())          # remove a random item from the set
# print(collection.pop())          # remove a random item from the set
# print(collection)      

    #// set.union(set2)         #combines both set values and return new
# set1 ={1,2,3}                   #set1
# set2 ={2,3,4}
# print(set1)
# print(set2)

# print("union of set1 and set2: ",set1.union(set2))            #output: {1, 2, 3, 4}

#     #// set.intersection(set2)  #combines common values and return new

# print("intersection of set1 and set2: ",set1.intersection(set2)) #output: {2, 3}


# ////  EX 1 store word meaing in dictionary:
# // table : "a piece of furniture", "list of fact and figures"
# // cat:"a small animal"

# dict={
#     "table":["a piece of furniture" , "list of fact and figures"],
#     "cat":"A small animal",
# }
# print(dict)

# ////  EX 2 you are given a list of subject for students.
# assume one classroom is required for 1 subject. 
# how many classroom are needed by all students.

## "python","java","c++","python","javascript",
##"java","python","java","c++","c"

# store the datain  toset and find length so we have  total number of unique subjects
# subjects={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }

# print(subjects)
# print(len(subjects))        ## output:5

# ////  EX 3 wap to 
# /// enter marks of 3 subject from the user and storethem in dictionary.
# # start with an empty dictionary and add one by one .
# # using subject name as key and marks as value

marks_dic = {}                   ## create empty dictonary
sub1marks = int(input("Enter Marks of first Subject Marks: "))       ## take input from user
marks_dic.update({"Phy": sub1marks})

sub2marks = int(input("Enter Marks of Second Subject Marks: "))       ## take input from user
marks_dic.update({"chem": sub2marks})

sub3marks = int(input("Enter Marks of Third Subject Marks: "))       ## take input from user
marks_dic.update({"maths": sub3marks})

print(marks_dic)


## ////  EX 4
    ##figure out a way to store 9 and 9.0 as seprate values in set.
    ## solu 1
# values ={9,"9.0"}             ## it will consider both 9 and 9.0 as same value due to float precision issue
# print(values)               # to save use string  representation of float i.e., str(9

## solu 2
values ={
    ("float",9.0,),
    ("int",9)
    } 

print(values)   



# ---------------------------------------------------
