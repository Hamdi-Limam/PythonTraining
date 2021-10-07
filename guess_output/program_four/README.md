## Explanation of the fourth program

First of all, we got a list named `list1` that contains two strings.

Next, we can see a for-loop. Inside it, we are applying `.append()` method on each element of the list.

Note: `.append()` is a list method, that adds an element at the end of the list

Outside the loop, we are simply printing the list.

### What's going on in the for-loop
Whenever this for-loop will execute, it will append that new value to the list1.

So, the first value of i will be "abc". the method `.append()` will append the i value to the list. The list become:
```
list1 = ["abc", "123", "abc"]
```
Next, i value became "123" now. Again, it will append it to the list and our list become like that:$
```
list1 = ["abc", "123", "abc", "123"]
```
Again, i value became "abc" and it will again append the value...

So, whenever the for-loop body will execute, it will append a new value to list1. That's why this for-loop will become infinite. There is no stop, it will not go out of the for-loop and it will not print anything.

Note: if your program still running and you want to close it. Press `CTRL+C` to interrupt it.