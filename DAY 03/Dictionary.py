dict1 = {"good": "Somthing pleasant", 
         "bad": "Something bad"}

dict2 = {"name": "Dhruv", 
        "age": 30, 
        "city": "Delhi"}
print(dict1)
print(dict2)

print(dict2["name"])
print(dict2.get("name"))
print(dict2.get)

print(len(dict1))
print(dict1.keys())
print(dict2.keys())
print(dict1.update(dict2)) # Updating the dictionary with another one
print(dict1)
print(dict2)
