mylist3 = [9,5,2,99,12,88,34]
mylist3.sort(reverse=True) # Sort list in descending order
print(mylist3)

mystring = "WELCOME"
listdv= list(mystring)
print(listdv)

rangeof40numberineven= [i for i in range(1,40) if i % 2 ==0]
print("", rangeof40numberineven)

listofnum=[1,2,3,4]
for i in listofnum:    
    l1 = [print("{} is Even Number".format(i)) if i%2==0 
        else print("{} is odd number".format(i))]
