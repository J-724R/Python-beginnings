# In python thera two types of loops, for and while

#! the for loop

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# range functio after python 3


#! while loops

# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# In python "break" and "continue" also exist

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

