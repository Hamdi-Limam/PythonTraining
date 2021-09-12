# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
for x in "Python":
    print(x, end=" ")
else:
    print(" ")
    print("Finally finished!")

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
print("Printing range(5) loop:")
for x in range(5):
    print(x, end=" ")

print(" ")
print("Printing range(2,6) loop:")
for x in range(2,6):
    print(x, end=" ")

print(" ")
print("Printing range(0,10,2) loop:")
for x in range(0,10,2):
    print(x, end=" ")

# for..else
print(" ")
names = ["Hamdi", "Achref"]
names_copy = names[:]
print("Copy of names list", names_copy)
print("Checking if an array has a name that starts with A:", end=" ")
for name in names:
    if name.startswith("A"):
        print("Found")
        break
else:
    print("name not found")

# List comprehension
output = [5*value for value in range(1,11)]
print("Printing List comprehension result: ", output)

# while..else loops
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    print("Congratz you guessed the answer")
