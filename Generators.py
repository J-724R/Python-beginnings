import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

# make fibonaci series
def fibonacci(n):
  temp = 0
  prevFib = 0
  fib = 1

  count = 0
  while count <= n :
    count += 1

    temp = prevFib
    prevFib = fib
    fib = prevFib + temp 

    print(fib)

fibonacci(8)
     