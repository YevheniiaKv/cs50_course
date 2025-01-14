# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

n = str(input("Your name: "))

if n[0] == "R" or "r":
    print (f"{n} plays banjo")

else:
    print(f"{n} does not play banjo")

