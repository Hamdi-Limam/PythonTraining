# id(): memory location address of count(changes by updating the variable)
# old memory will be released by python garbage collector
x = 1
print("id Of count", id(x))

# Mutable and immutable types

# Mutable sequences can be changed after creation. Some of Python’s mutable data types are: lists, arrays, sets, and dictionaries.
# Lists a is a collection of items which can contain elements of multiple data types
sample_list = [1,"Hamdi",['a','e']]
print("Printing the list: ", sample_list)
print("length of the list is :", len(sample_list))
print("Printing ID of list before: ", id(sample_list))
sample_list.append(5)
print("Printing ID of list after: ", id(sample_list))

# Arrays are used to store multiple values in one single variable containing homogeneous elements i.e. belonging to the same data type.
x = [3, 1, 2, 3]
print("Printing the array: ", x)
print("length of the array is :", len(x))
print("Printing ID of the array x before: ", id(x))
x.append(4)  # pushing another value into the array
print("Printing ID of the array x after: ", id(x))

# A set is a collection which is both unordered and unindexed
sample_set = set(('San Francisco', 'Sydney', 'Sapporo'))
print("Printing the set: ", sample_set)
print("length of the set is :", len(sample_set))
print("Printing ID of the set before: ", id(sample_set))
sample_set.pop()
print("Printing ID of the set after: ", id(sample_set))

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
sample_dictionary = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo'
}
print("Printing the dictionary: ", sample_dictionary)
print("length of the dictionary is :", len(sample_dictionary))
print("Printing ID of the dictionary before: ",id(sample_dictionary))
sample_dictionary.update({
    'f': 'foxtrot'
})
print("Printing ID of the dictionary after: ",id(sample_dictionary))

# Immutable can not be changed after creation. Some immutable types include numeric data types, strings, bytes, frozen sets, and tuples.
# tuples are used to store multiple items in a single variable and they are ummutable
numbers = tuple((1, 3, "test"))
# numbers[0] = 10 error tuple cannot be modified
print("Printing the tuple: ", numbers)
print("length of the tuple: ", len(numbers))
# x = numbers[0]
# y = numbers[1]
# z = numbers[2]
x, y, z = numbers
print("Unpacking the tuple", x , y ,z)

#Integer is a whole number, negative, positive or zero.
count = 5
x, y = 1, 2
x = y = 1
print("typeOf count is :", type(count))  # typeOf()
print("Printing ID of the integer before: ", id(count))
count = count + 1
print("Printing ID of the integer after: ", id(count))

# Floating Point Numbers are decimals, positive, negative and zero. Floats can also be represented by numbers in scientific notation which contain exponents.
price = 4.99
print("typeOf price is :", type(price))  # typeOf()
print("Printing ID of the integer before: ", id(price))
price = price + 1
print("Printing ID of the integer after: ", id(price))

# A complex number is defined in Python using a real component + an imaginary component j
comp = 4 + 2j
print("typeOf comp is :", type(comp))  # typeOf()
print("Printing ID of the integer before: ", id(comp))
comp = comp + (1 + -1j)
print("Printing ID of the integer after: ", id(comp))

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
name = "Hamdi"
description = """
Multiple
Lines
"""
print("typeOf name is :", type(name))  # typeOf()
print("Printing ID of the integer before: ", id(name))
name = name + " " + "Limam"
print("Printing ID of the integer after: ", id(name))

# Booleans represent one of two values: True or False.
isvalid = False
print("typeOf isvalid is :", type(isvalid))  # typeOf()
print("Printing ID of the integer before: ", id(isvalid))
isvalid = True
print("Printing ID of the integer after: ", id(isvalid))
