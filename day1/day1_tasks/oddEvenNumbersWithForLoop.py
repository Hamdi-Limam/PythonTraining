# Generating even numbers
print('Welcome to Generating Odd and Even numbers exerice with For loops!')
finished = False
while not finished:
    try:
        limit = int(input("Please enter the limit: "))
        print("The even numbers are: ")
        for i in range(1, limit+1):
            if i % 2 == 0:
                print(i, end=" ")
        print(" ")
        print("The odd numbers are: ")
        for i in range(1, limit+1):
            if i % 2 != 0:
                print(i, end=" ")
        finished = True
    except ValueError:
        print("Make sure to enter a number!")
        finished = False

