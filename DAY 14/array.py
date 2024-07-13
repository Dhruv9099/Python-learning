import array

# Creating an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements in the array
print("Array elements:", my_array[0], my_array[1], my_array[2])

# Adding elements to the array
my_array.append(6)
print("Updated array:", my_array)
print(my_array[2])



# Create a 2D array (3x3)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements in the 2D array
element_1_2 = matrix[0][1]

# Display the accessed element
print("Element at row 1, column 2:", element_1_2)