# Task 1: WAP to create a function which returns the sum of all the element provided to it as an arguement. The arguement list will be dynamic.
print("Welcome to day2 task1 exercuce! using *args")
def sum_list(*list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum

print("The sum of all the element of the list is: ", sum_list(1, 2, 3, 4, 5))


print("Welcome to day2 task1 exercuce! using **kwargs")
def myFun(**kwargs):
    return sum(kwargs.values())

print("The sum of all the element of the list is: ", myFun(first=1, second=2, third=3, fourth=4, last=5))

