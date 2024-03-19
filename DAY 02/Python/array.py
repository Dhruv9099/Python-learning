#Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Get the value of the first array item:
x = cars[0]
print(x)
y = len(cars)
print("car count is "  + str(y)) 

# Adding Array Elements
# You can use the append() method to add an element to an array.

# Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# You can use the pop() method to remove an element from the array.
cars.pop(2)
print(cars)

# Delete the element that has the value "Volvo":
cars.remove("Volvo")
print(cars)