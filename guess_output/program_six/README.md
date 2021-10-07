## Explanation of the sixth program

First of all, we got a list named `list1` that contains string and a nested list of strings.

Next, we have three print functions to print some specific elements of the list.

Note: To understand this program, you should have a knowledge of slicing operation as well as nested list concept.

So, the slicing operation will give you the sublist from a list right. its syntax is list1[start, end, step]


Let's jump to the first print function `print(list1[3:4])`
Here, 3 is the start value and 4 is the end value.

But, don't forget that 4 is exclusive, so this operation will return a list with the value present at the index 3 which is in our case the nested list.

So the result of the slicing operation is a list and the value presented in the index 3 is a nested list so the result is: `[['few', 'words']]`.


Moving to the next print function `print(list1[3:4][0])`, As we saw before, the result of `list1[3:4]` is `[['few', 'words']]`. In that we want the first element that in nothing but the element present in the index 0.

Here, we can see in the list `[['few', 'words']]` only one value is present that is this list: `['few', 'words']`. So, that's out output for print function two.

Finally, the last print function `print(list1[3:4][0][1][2])`.
We already have the result of this operation `list1[3:4][0]` right? that is `['few', 'words']`

As you see, it is a list of two string the first element of index 0 is 'few' and the last element of index 1 is 'words'

Here we want the element of index 1 `list1[3:4][0][1]` that is the `'words'` string. But, in the program we are not asking about that, we mention another index also, that's nothing but in this 'words' string, we want the element of index present in the second index. So we got:
* w -> index of 0
* o -> index of 1
* r -> index of 2 -> that's what we want

So our output here is the character 'r'.