"""
INF360 VA - Programming with Python
Jarrett Smolarkiewicz
Assignment 4

(1/1 point) - Initial comments*
(2/2 points) - Read the file story.txt and store the lines as a variable called story. You must use relative paths, assume the story.txt file is in the same folder as your script.
(5/5 points) - Write a regular expression that will find all occurances of the phrase,  "Sherlock Holmes".
(5/5 points) - Using the substitue method, replace all occurances of "Sherlock Holmes" with your name, storing the count of these occurances as a variable called foundCount.
(2/2 points) - Write a regular expression that will find all occurances of the phrase, "the".
(3/3 points) - Create a variable called theCount, that stores the total number of occurances of the phrase "the".
(3/3 points) - Print to the user, the original name, the replacement name, and the total number of occurances using a print command with a formatted string literal using a string that starts with f".
(3/3 points) - Print to the user the a string that tells the user the total number of occurances of "the" using a print command with a formatted string literal using a string that starts with f".
(1/1 points) - Save the story out to a new file called new_story.txt.
"""
# import Regular Expressions
import re
# import Path from Path Library (pathlib)
from pathlib import Path

# Read the file story.txt and store the lines as a variable called story. You must use relative paths, assume the story.txt file is in the same folder as your script.
story = Path("story.txt").read_text()

# Write a regular expression that will find all occurances of the phrase,  "Sherlock Holmes".
# The original name in the story
original_name = 'Sherlock Holmes'
print(re.findall(original_name, story))

# Using the substitue method, replace all occurances of "Sherlock Holmes" with your name, storing the count of these occurances as a variable called foundCount.
# The replacement name (my name)
replacement_name = 'Jarrett Smolarkiewicz'
foundCount = re.sub(original_name, replacement_name, story).count(replacement_name)

# Write a regular expression that will find all occurances of the phrase, "the".
re.findall("the", story)

# Create a variable called theCount, that stores the total number of occurances of the phrase "the".
theCount = story.count("the")

# Print to the user, the original name, the replacement name, and the total number of occurances using a print command with a formatted string literal using a string that starts with f".
print(f"The original name in this story is {original_name}, which is replaced by the name {replacement_name}, each of the {foundCount} times it occurs within the story.")

# Print to the user the a string that tells the user the total number of occurances of "the" using a print command with a formatted string literal using a string that starts with f".
print(f"During this story, 'the' occurs {theCount} times.")

# Save the story out to a new file called new_story.txt.
try:
    f = open("new_story.txt", "x")
    f.write(re.sub(original_name, replacement_name, story))
    f.close()
except:
    print("new_story.txt already exists!")
