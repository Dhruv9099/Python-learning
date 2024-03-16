# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key


# Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])
print(type(thisdict))
x = thisdict.get("model")

#Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.get("name")