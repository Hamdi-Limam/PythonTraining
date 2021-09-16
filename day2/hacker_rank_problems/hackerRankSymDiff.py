# HackerRank problem for Sets. Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

# If the inputs are given on one line separated by a character (the delimiter), 
# use split() to get the separate values in the form of a list. 
# The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). 
# Example: 
# a = input("Enter numbers: ")
# lis = a.split(",")
# print(lis)
# print(type(lis))

# If the list values are all integer types, use the map() method to convert all the strings to integers.
# Example: 
# newlis = list(map(int, lis))
# print (newlis)

# Sets are an unordered collection of unique values. A single set contains values of any immutable data type.
#  myset = {1, 2} # Directly assigning values to a set
#  myset = set()  # Initializing a set
#  myset = set(['a', 'b']) # Creating a set from a list

# Task: Given  sets of integers,  and , print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

m = int(input("Enter the size of the first set :"))
first_set = set(input("Enter the elements of the first set seperated by space :").split())
n = int(input("Enter the size of the second set :"))
second_set = set(input("Enter the elements of the second set seperated by space :").split())

print("\n".join(sorted(list(first_set.symmetric_difference(second_set)), key=int)))


# a,b = [set(input().split()) for _ in range(4)][1::2] -> List[start:end:jump]
# print ('\n'.join(sorted(a^b, key=int)))
