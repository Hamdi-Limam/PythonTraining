## Explanation of the third program

First of all, we got a list named `list1` that contains three strings with lower and upper case characters.

Next, we can see a for-loop. Inside it, we are applying `.lower()` method on each element of the list.

Note: .lower() is a string method that converts a string into lower case and returns it.

Outside the loop, we are simply printing the list.

### What's going on in the for-loop
So, the first value of i will be "ABC". Here, we see all the characters are in upper case letters. then we are calling the .lower() method to convert it to lower case letters.

But, you need to remember one thing, `.lower()` method **will not modify the original string**. It will return a new string with the lower case letters. And in our case, we are not storing that new string anywhere, that's why the result will be destroyed and value of `i` will be the same.

### Storing the result of lower method
Here is an example, where we store the result of lower method into another list then printing it:
```
list1 = ["ABC", "XYZ", "pqR"]
list2 = []
for i in list1:
    list2.append(i.lower())

print(list1)
print(list2)
```