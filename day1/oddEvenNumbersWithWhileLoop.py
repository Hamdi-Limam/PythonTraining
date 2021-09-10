# Generating even and odd numbers
print('Welcome to Generating Odd and Even numbers exerice with while loops!')
finished = False
while not finished:
    try:
        limit = int(input("Please enter the limit: "))
        i = 1
        print("The even numbers are: ")
        while (i <= limit):
            if i % 2 == 0:
                print(i, end=" ")
            i = i + 1
        print(" ")
        print("The odd numbers are: ")
        i = 1
        while (i != limit):
            if i % 2 != 0:
                print(i, end=" ")
            i = i + 1
        finished = True
    except ValueError:
        print("Make sure to enter a number!")
        finished = False
