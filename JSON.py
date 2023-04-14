# the #! json.loads 
# Converts json to python
# turns a string into a json object datastructure

# ! json.dumps
# Converts form python to json
# methods takes an object and returns a String

#! Exercise
# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# The json.dumps() method has parameters to make it easier to read the result:

print(json.dumps(x, indent=4))

# The json.dumps() method has parameters to order the keys in the result:

json.dumps(x, indent=2, sort_keys=True)