
# If Statement
a = 33
b = 200
print("If Statement")
if b > a:
    print("b is greater than a")


# Elif  statement
a = 33
b = 33
print("elif statement")
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else statement The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
print("Else statement")

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# One line if statement:

if a > b:
    print("a is greater than b")


# And : The and keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if (a > b and c > a):
    print("Both conditions are True")
    
elif (a > b or c > a):
    print("One of the conditions is True")
    
else:
    print("Both conditions are False")

# Nested If: You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

