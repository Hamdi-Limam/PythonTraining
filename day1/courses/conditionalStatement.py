#Python supports the usual logical conditions from mathematics:
# Equals: a == b
#  Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

age = 0
if age >= 18 and age <= 20:
    print("true") # If statement, without indentation (will raise an error).
elif age >= 23:
    print("false")
else:
    print("none of them")

# Short Hand If, If you have only one statement to execute, you can put it on the same line as the if statement.
a = 20
b = 18
if a > b: print("a is greater than b")

# logical operators and/or/not
name = ""
if not name:
    print("name is empty")

# ternary operator
msg = "adult" if age >= 18 else "child"
print(msg)

# Match Case 
# The match case structure is available for python version 3.10 and onwards.
# http_code = "418"
# match http_code:
#   case "200":
#        print("OK")
#        do_something_good()
#    case "404":
#       print("Not Found")
#        do_something_bad()
#    case "418":
#        print("I'm a teapot")
#        make_coffee()
#    case _:
#        print("Code not found")
