a = int(input("Enter your Age "))
print("Your Age is :", a)
#conditional operator >, <, ==, !=,  <=, >=
print(a>18)
print(a>=18)
print(a<18)
print(a<=18)
print(a==18)
print(a!=18)


# IF ELSE
if  (a > 18):
    print("You can drive")
else:
    print("You are not a child")
    
    # for loop 
def factorial_with_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example: Calculate factorial of 5
result_for = factorial_with_for_loop(5)
print(result_for)