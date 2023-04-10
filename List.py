ryuksfriends=[]
ryuksfriends.append("Ora")
ryuksfriends.append("Blonder")
ryuksfriends.append("Perrita de ToyoTachira")
ryuksfriends.append("Perrita del Pollito")
ryuksfriends.append("Perritas del metro")

print(ryuksfriends[0])


print("Looping")
for x in ryuksfriends:
    print(x)


#Exercise from https://www.learnpython.org/en/Lists
print(" ")
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
