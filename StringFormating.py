name = "Ryuk"
print("My dog name is %s" % name)

weight = 18
print("%s weights %d Kg" %(name, weight))

mylist = [1,2,3]
print("A list: %s" % mylist)

#* Basics arguments specifiers

# %s, %d, %f, %.<number if digits>f

#Exercise

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s $s. Your current balance is $%f."

print(format_string % data)

