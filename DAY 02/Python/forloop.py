num=[10,20,30,40,50]
for i in num:
    print(i)

for char in 'hello':
    print(char)
    #character and number also prints values

# For Loop with Dictory 
number ={1:'one',2:'two',3:'three'}
for pa in number.items():
    print(pa)
    
# 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def default(a,b):
    return "Default Case"

d = {"+":add,"-":sub,"*":mul,"/":div}

def switch(operator,x,y):
    return(d.get(operator,default))(x,y)

result = switch("+", 5, 3)
print("result: ", result)  # Output: 8



i = 1
while i<5:
    i= i+1
    if i ==3:
        continue 
    print(i)




# Firstname= input( "Enter your First name: " )
# print("your first name is " + Firstname)



