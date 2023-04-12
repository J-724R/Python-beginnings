# Dictionaries are similar to arrays, but works with keys and values instead of indexes
# works as the objects in js

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

Ryukchart = {
    "Ryuk" : {
      "age": 8,
      "breed": "Mix"
    },
}
print(Ryukchart)

# using dictionaries with function

def createDogChart(age, breed, size):
    return {
        "age": age,
        "breed": breed,
        "size": size
    }

DogDB = {
    "Ryuk": createDogChart(7, "mix", "medium"),
    "Ora": createDogChart(2, "mix", "medium"),
    "Luna": createDogChart(10, "labrador", "big")
}
print(DogDB)
# Accessing nested elements
print(DogDB['Ora']['breed'])

# Similar to JS objects dictionaries doesn't keeps elements order when iterated


#! To remove values from dictionaries there are two notation

# del dictionary_name["element to delete"]
# or
# dictionary_name.pop("element to delete")