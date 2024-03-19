#date 07/3/2024
# Here we have to first pass a parameter then try to check with which case the parameter is getting satisfied. 
#If we find a match we will do something and if there is no match at all we will do something else.

a = int(input("Enter the  value of 'a': "))
match a:
    case 1:
        print('Value is 1')
    case 2:
        print('Value is 2')
    case 3:
        print('Value is 3')
    case 4:
        print('Value is 4')
    case 5:
        print('Value is 5')
    case _:
        print('Value is not Found')
