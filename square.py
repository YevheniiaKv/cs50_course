from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# the second way:
import functions

for i in range(11):
    print(f"The square of {i} is {functions.square(i)}")