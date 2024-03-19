
# JSON in Python
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

import json

# Parse JSON - Convert from JSON to Python
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Convert from Python to JSON


# a Python object (dict):
x = {
    "name": "Fenil",
    "age": 26,
    "city": "Surat"
}
print(x)
print(type(x))

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))
