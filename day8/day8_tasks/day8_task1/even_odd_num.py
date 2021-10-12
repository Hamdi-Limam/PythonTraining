# Write a program to generate all even and odd numbers using list comprehension.

even_num =  [i for i in range(1, 101) if i % 2 == 0]

odd_num = [i for i in range(1, 101) if i % 2 != 0]

print("Even number list: ", even_num)

print("Odd number list: ", odd_num)