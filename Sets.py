# Sets are lists with no duplicate entries. Let's say you want 
# to collect a list of words used in a paragraph

print(set("my name is Eric and Eric is my name".split()))

# Sets are a powerful tool in Python sice they have the ability to calculate
# diffrences and intersections between other sets. For example, say you have 
# a list of participants in events A and B

a = set(["Jake", "John", "Eric"])
print(a)
print(a)
b = set(["John", "Jill"])
print(b)

# finding which menbers attended both events (intersection)

print(a.intersection(b))
print(b.intersection(a))

# To get a single group of which members attended only one 
# of the events, use the "symmetric_difference" method:

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To find out which members attended only one event and not 
# the other, use the "difference" method. But get separate groups

print(a.difference(b))
print(b.difference(a))

# There is also a union method, get a group of common and uncommond elements

print(a.union(b))

# ! Exercise
# use the given lists to print out a set containing all the
#  participants from event A which did not attend event B.

#! These methods only works with sets

groupA = set(["Jake", "John", "Eric"])
groupB = set(["John", "Jill"])

print("\n Exercise \n")
print(groupA.difference(groupB))