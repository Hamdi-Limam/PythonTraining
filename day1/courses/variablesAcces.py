# Python doesn't have block scoop (you can access to a variable declared in IF statement outside it)

# local scoop (function)
def greet():
    if True:
        message = "I'm local variable"
    print(message)


greet()
# global scoop
msg = "I'm global varialbe"


def test():
    # Not the same global var, this another local var with different address memory
    msg = "Changing global variable inside fct"
    print(msg)


test()
print("Its back to the first value ", msg)

