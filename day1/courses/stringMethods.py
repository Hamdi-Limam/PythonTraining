# Strings
course = "python programming"

print("length of string course", len(course))  # length of course
print("first char", course[0], "last char", course[-1])  # length of course
# substring so OP but python allocate new memory
print("substring", course[0:3])
print("Checking first letter", course.startswith("p"))

# formated strings
first = "Hamdi"
last = "Nait Limam"
full = f"{first} {last}"
print("Concating string with formated string ", full)

# String methods
first.upper()  # UpperCase
first.lower()  # LowerCase
first.title()  # Upper the first char of each word
first.strip()  # Remove all the useless whitespaces
test = course.replace("p", "-")  # Replace each equal char by another
print(course.find("p"))  # Returns the index of first char otherwise returns - 1
# Join 2 strings ["bla",""], "" is the default value
joinedString = last.join(['Hamdi ', ''])
print("this is joinedLAST ", joinedString)
splited = joinedString.split()  # split string to a list
print("this is splitedLAST", splited)
# check the existing of char or string in a string returns boolean
print("amd" in first, "amd" not in first)
