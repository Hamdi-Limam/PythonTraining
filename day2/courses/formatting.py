
person = {'name': 'Hamdi', 'age': 22}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

# Repeating String while string formatting
tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

# Formatting Dictionnary
sentence = 'My friend is {name} and She is {age} years old.'.format(name='Amal', age='25')
print(sentence)

# Using **kwargs to unpack dictionnary
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

# Adding digits to integers
for i in range(1, 3):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

# Controlling decimal places
# pi = 3.14159265
# sentence = 'Pi is equal to {:.2f}'.format(pi)
# print(sentence)

# Adding comma to big number
sentence = '1 MB is equal to {:,} bytes'.format(1000**2)

print(sentence)

# Formatting date 
import datetime

# Documentation about strftime() and strptime() Format Codes. Link: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
my_date = datetime.datetime(2021, 9, 27, 15, 30, 45)
print(my_date)

# March 01, 2021
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2021 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)