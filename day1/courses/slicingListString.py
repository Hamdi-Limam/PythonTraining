my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]
print(my_list[::-1])


text= 'http://google.com'

# Reverse the url
print(text[::-1])

# Get the top level domain
print(text[-3:])

# Print the url without the http://
print(text[7:])

# Print the url without the http:// or the top level domain
print(text[7:-4])