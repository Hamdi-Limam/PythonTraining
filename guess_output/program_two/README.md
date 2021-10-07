## Explanation of the second program

This program is based on:
1. True and False Value
2. Operator Precedence

So we got three variables:
```
p = (1,10) -> True non empty list
q = 0 -> False
r = [] -> False
```

Then, we got an if-else condition statement, with condition of 
`p or q and r`.

As you see there are two operators which are `or` and `and`. When the expression contains more than one operator. Then, there is a order to evaluate that expression which is called `Precedence`.

Here, `AND` operator has a higher precedence than the `OR`.
So first, this condition will execute `q and r` then `p or (result of q and r)`.

What's the result of q and r?
Like we saw before, both zero and empty list will be traited as False values. So, `q` is False and `p` is also False.

### How the `AND` operator works?
* FALSE AND FALSE -> False
* FALSE AND TRUE -> False
* TRUE AND FALSE -> False
* TRUE AND TRUE -> True

The `AND` operator will only return true if both variables are True. In our case, both q and r are False, so our expression will return **False**.

### How the `OR` operator works?
* FALSE OR FALSE -> False
* FALSE OR TRUE -> True
* TRUE OR FALSE -> True
* TRUE OR TRUE -> True

The `OR` operator will return true if both variables are True. or one of them is True. In our case, the result of `q and r` is False, but the variable p is a non empty list which means it is considered as a True value. so our final expression `TRUE or False` will return **True** and we will print it.