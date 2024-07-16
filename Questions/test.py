
def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter the position of the Fibonacci number: "))
# print(f"The {n}th Fibonacci number (recursive) is: {fibonacci_recursive(n)}")
print(f" fibonacii of {n} is : {fibonacci_recursive(n)}")


# ----------------------------------
# The original input string
OriginalString = "The quick brown fox jumps over the lazy dog."
 
# Splitting the string and removing spaces and punctuation.
CleanedString = ''.join(filter(lambda x: x.isalpha() or x.isspace() or x.isdigit(), OriginalString.split()))
 
# To Bring Consistency in the string, converting everything to lowercase
CleanedString = CleanedString.lower()
 
#dictionary comprehension for the frequency count&nbsp;
result = {x: CleanedString.count(x) for x in CleanedString};
 
# Printing the result dictionary
print(result)
            
            
number_list = [x ** 2 for x in range(10) if x % 2 == 0] 
print(number_list)


dimensions = (800, 600)
print(dimensions)
dimensions = (1200, 900)
print(dimensions)





names = ["Jacob", "Joe", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")