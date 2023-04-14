# Map, Filter, and Reduce are paradigms of functional
# programming. They allow the programmer (you) to write 
# simpler, shorter code, without neccessarily needing to 
# bother about intricacies like loops and branching.

# Reduce method needs to be imported due to is inside the functools module

# ! Maps
# In Python 3, map returns a map object
# The number of arguments to the function passed must be 
# the number of iterables listed.

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)


uppered_pets_map = list(map(str.upper, my_pets))
print("\n With map \n")
print(uppered_pets_map)

# Example of multiple arguments function, since the function 
# require two agruments we need to pass in two iterables

# Progresive rounding circles areas from 1 to list length decimals 

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)

# ? If the numbers of iterables differ, map method stops 
# ? there adn retrun the results so far obtained

# ! Zip() makes a tuples from lists

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)

# As map it stop when the iterables elements differ in length

# ! Filter, filter(func, iterable)
# filter passes each element in the iterable through func and 
# returns only the ones that evaluate to true. I mean, it's right
#  there in the name -- a "filter".

# Filter the students who passed

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

# Fiter palindromes

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

# ! Reduce, reduce(func, iterable[, initial])

# Sum of the number of a lists
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)



# ! Exercise

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x*2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7 , my_names, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
