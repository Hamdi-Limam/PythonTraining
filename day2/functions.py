# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# Below are few reason why you want to create a function:
# 1.Reusable code
# 2.Seperating the concern. What I mean here is you want to make your code such that you can seperate out different functionalities of program and convert them as functions.
def greet(firstname):
    lastname = "Limam"
    welcome = f"Welcome {firstname} {lastname}"
    return welcome

print(greet("Hamdi"))

# Default values, one can define default values for each function parameter 
# if an arg for a parameter is not passed, default value is used
def greet(name="Hamdi"):
    print(f"Default parametre is: {name}")

greet()

# Arguments(args) are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# greet("test")
# greet("test","hamdi")

# A parameter is the variable listed inside the parentheses in the function definition.
# def greet(firstname): -> firstname is a parameter

# Keyword arguments(kwargs) -> send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def goldenBall(name1, name2):
  print(f"The best footballer is {name1} but the GOAT is {name2}")

goldenBall(name2 = "Messi", name1 = "Ronaldo")

# *args for variable number of arguments
# This way the function will receive a tuple of arguments
def myFun(*argv):
    print("Printing *args:", end=" ")
    for arg in argv:
        print (arg, end=" ")
   
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print(" ")

# Arbitrary Keyword Arguments(**kwargs), If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments
def goldenBall(**winner):
  print(f"The best footballers are: {winner['name2']} and {winner['name1']}")

goldenBall(name2 = "Messi", name1 = "Ronaldo")

# Passing a List as an Argument, You can send any data types of argument to a function (string, number, list, dictionary etc.)
def my_function(food):
  for x in food:
    print(x, end=" ")

fruits = ["apple", "banana", "cherry"]

my_function(fruits)