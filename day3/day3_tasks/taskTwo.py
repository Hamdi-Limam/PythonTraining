# Task 2: Read and understand what are Regular expressions and they evaluate.

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.
import re

# RegEx Functions$
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# Metacharacters are characters with a special meaning :
# List of metacharacters: https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
# Here are some exmaples:
# ^	Starts with	"^hello"
# $	Ends with	"world$"	

# Searching if a string starts with "The" and ends with "hot" with metacharacters
info = "The weather is hot"
exist = re.search("^The.*hot$", info) # Returns a Match object if there is a match anywhere in the string, else returns None
if exist:
    print("YES! We have a match!")
else:
    print("No match")

# Special Sequences is a "\"" followed by one of the characters and has a special meaning:
# List of special sequences: https://www.w3schools.com/python/gloss_python_regex_sequences.asp
info = "The weather is hot"
exist_start = re.search("\AThe", info) 
exist_end = re.search("hot\Z", info) 
if exist_start and exist_end:
    print("YES! We have a match!")
else:
    print("No match")

# Sets are a set of characters inside a pair of square brackets [] with a special meaning:
# List of sets: https://www.w3schools.com/python/gloss_python_regex_sets.asp
# Examples: 
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n

# Check if the string has any a, r, or n characters:
x = re.findall("[arn]", info)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Replace all white-space characters with "-":

txt = "The rain in Spain"
x = re.sub("\s", "-", txt)
print(x)

# Backtracking occurs when a regular expression pattern contains optional quantifiers or alternation constructs, 
# and the regular expression engine returns to a previous saved state to continue its search for a match
# Example: the regEx engine will BACKTRACK to catch \d{2} => (23) after not matching [a-z]{2} => 3
txt = "abc123def"
x = re.search("\d{2}[a-z]{2}", txt)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Backtracking can be caused by optional quantifiers or alternation constructs, because the regex engine will try to explore every path. 
# If you run the regex a+b against aaaaaaaaaaaaaa there is no match and the engine will find it pretty fast.
# But if you change the regex to (aa*)+b the number of combinations will grow pretty fast, 
# and most (not optimized) engines will try to explore all the paths and will take an eternity to try to find a match or throw a timeout exception. 
# This is called catastrophic backtracking.
# (\s*|\s*#\s*|\s*.\s*|\s*-\s*|\s*:\s+) all alternatives start with \s* here. 
# This causes lots of redundant backtracking as these alternatives can match at the same location in a string. 

# How to avoid it
# Be as specific as possible, reduce as much as possible the possible paths. Make the pattern more specific and linear. 
# The best practice is to use alternatives in an alternation group that do not match at the same location.
# Get rid of as many alternations as possible, use optional non-capturing groups and character classes.
