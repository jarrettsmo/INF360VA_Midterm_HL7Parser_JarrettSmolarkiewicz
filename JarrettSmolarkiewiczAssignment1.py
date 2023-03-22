# INF360 VA - Programming with Python
# Jarrett Smolarkiewicz
# Assignment 1

# 1/1 point - Initial comments*
# 2/2 points - Use of the print() function to display a welcome and prompt a question to the user.
# 2/2 points - Use of the input() function and store in a variable called myInput.
# 1/1 point - Use the print() function to print the contents of myInput.
# 2/2 points - Use two different math operators from Table 1-1 in your script. This may be used to manipulate some input from the user.
# 2/2 points - Use string concatenation.

print("Welcome!")

print("What is your name?")

myInput = input("> ")

print("Hello, " + myInput + "! " + "How many people are currently in your family?")

familySize = input("> ")

familySizeInt = int(familySize) + 1

familySizeIntSub = int(familySize) - 1

print("If you invited me to your house for dinner, you would need to make enough for " + str(familySizeInt) + " people.")

print("If you and I went out for dinner, the rest of your family would only need to make enough dinner at home for " + str(familySizeIntSub) + ".")

print("Unfortunately, we can't do that, because I'm just a Python program, and I don't eat food.")
