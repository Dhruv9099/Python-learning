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


i = 1
while i<5:
    i= i+1
    if i ==3:
        continue 
    print(i)



nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print(nlis)
clone_list = nlis[:]
print(clone_list)
print('clone_list[0]:', clone_list[0])
nlis[0] = 'hello, python!'
print('nlis[0]:', nlis[0])
print(clone_list)
print(nlis)

Firstname= input( "Enter your First name: " )
print("your first name is " + Firstname)



