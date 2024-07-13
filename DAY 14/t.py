
# txt = "Hello {word}"
# print(txt.format(word = 'World!'))

# message1 = 'Hi, My name is {} and I am {} years old.'
# print(message1.format('Bob', 36))

# message2 = 'Hi, My name is {name} and I am {number} years old.'
# print(message2.format(name ='Bob', number = 36))

# message3 = 'Hi, My name is {0} and I am {1} years old.'
# print(message3.format('Bob', 36))

# nlis = ['python', 3.14, 2022, [1, 1]]
# print(nlis)
# print(len(nlis))
# l=[1,2,2]
# list.append(nlis,l)
# print(nlis)

# list.extend(nlis,["as","as"])
# print(nlis)

for x in range(1,2):
    for y in range(1,11):
        print(x,"*",y,"=",x*y)

list=[1,2,3,4]

count=0
for i in list:
    count+= i 

print(count)

print ("average of count: " ,count/len(list))


# my_list = [i for i in range(1, 10)]
# print(my_list)

# my_tuple = (i for i in range(10, 21))
# print(my_tuple)
# list.extend(,my_tuple)
# print(my_list)



# 

class monkey:
    def patch(self):
          print ("patch() is being called")

def monk_p(self):
    print ("monk_p() is being called")

# replacing address of "patch" with "monk_p"
monkey.patch = monk_p

obj = monkey()

obj.patch()
# monk_p() is being called

class all:
    def sum(self,a,b):
        return self.a + self.b
    
    def sub(self,a,b):
        return self.a * self.b 
    
    

def str_replace(text,ch):
    result = ''
    for i in text: 
            if i == ' ': 
                i = ch  
            result += i 
    return result

text = "D t C mpBl ckFrid yS le"
ch = "a"

str_replace(text,ch)
# 'DataCampBlackFridaySale' 
