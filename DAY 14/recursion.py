# // when a function calls repeatedly.

# // print n to 1 backwards
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(4)

# // call stack : when we write function  inside the other function, it's like putting a box in another box.
'''
when we call show(4), it will put 4 in the box and then call itself with argument 3.
when we call show(3), it will put 3 in the box and call itself with argument 2.
it keeps going until it gets to 0, which is the base case for recursion.
then it starts coming back out of the boxes, printing each number as it goes.
so you get: 4, 3, 2, 1, 0 ,here we use n-1 so output is 4,3,2,1'''

# //returns n!

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(4))

# //write a recursive function to calculate the sum of first n natural numbers.

# def cal_sum(n):
#     if(n==0):
#         return 0

#     return cal_sum(n-1) + n
# sum =cal_sum(5)
# print(sum)


# // write a recursive function to print all elements in list .use list and index as parameter.

def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)


fruit = ['apple', 'banana', 'cherry', 'orange', 'grape']
print_list(fruit)
