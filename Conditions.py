x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#True and False needs to be with start with capital letters


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


#! The "in" operator
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# Python doesn't need brackets, code blocks are defined by indentation


#! The 'is' operator
# Unlike the double equals operator "==", the "is" operator does not match 
# the values of the variables, but the instances themselves. For example

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
