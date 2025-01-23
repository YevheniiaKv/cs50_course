# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    # Check if the name starts with the letter "R" or "r":
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
    # Run the function:
name = input("Enter your name: ")
result = are_you_playing_banjo(name)
print(result)