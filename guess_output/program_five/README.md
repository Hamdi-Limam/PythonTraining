## Explanation of the fifth program

First of all, we got a for-loop with range(1, 20).

Inside the for-loop, we got a if-else condition statement. 

In the if we can see the condition `i==5` then break statement will execute else we print the value of i.

Note: The break statement terminates the loop containing it.

For the for-loop, we can see the else block. We can use this else block with for-loop or while loop in python.

### What's going on in the for-loop
Initially, the value of i will be 1. It will check if it is equal to 5 or not if it is it will break the for-loop otherwise it will print the value of i.

So for the value of i = 1, it will print 1.

Same thing to 2, 3 and 4. The program will print them.

The interesting part happends when the value of i becomes equal to 5.

The condition `i==5` will become True, so it will execute this break statement. We know that, when the break statement executes control will come out of the loop and it will not execute any other statement of that loop.

### What about the else block
The else block is executed only when the for loop is not terminated by a break statement. So in out case, the else block will not be executed.

Here is another example where the else block will be executed:
```
for i in range(1,20):
    if i==5:
        continue
    else: 
        print(i)
else:
    print("Hello")
```