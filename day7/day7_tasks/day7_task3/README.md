## What are generators and how to use them?

Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.

Now that you have a rough idea of what a generator does, you might wonder what they look like in action. Let’s take a look at two examples. In the first, you’ll see how generators work from a bird’s eye view. Then, you’ll zoom in and examine each example more thoroughly.

### Example 1: Reading Large Files
A common use case of generators is to [work with data streams or large files](https://realpython.com/working-with-files-in-python/), like [CSV files](https://realpython.com/courses/reading-and-writing-csv-files/). These text files separate data into columns by using commas. This format is a common way to share data. Now, what if you want to count the number of rows in a CSV file? The code block below shows one way of counting those rows:
```
with open("employee_birthday.csv") as csv_file:
    csv_gen = csv.reader(csv_file, delimiter=',')
    row_count = 0

    for row in csv_gen:
        print(row)
        row_count += 1

print(f"Row count is {row_count}")
```
Looking at this example, you might expect csv_gen to be a list. To populate this list, csv_reader() opens a file and loads its contents into csv_gen. Then, the program iterates over the list and increments row_count for each row.

This is a reasonable explanation, but would this design still work if the file is very large? What if the file is larger than the memory you have available? To answer this question, let’s assume that csv_reader() just opens the file and reads it into an array:
```
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```
This function opens a given file and uses file.read() along with .split() to add each line as a separate element to a list. If you were to use this version of csv_reader() in the row counting code block you saw further up, then you’d get the following output:
```
Traceback (most recent call last):
  File "ex1_naive.py", line 22, in <module>
    main()
  File "ex1_naive.py", line 13, in main
    csv_gen = csv_reader("file.txt")
  File "ex1_naive.py", line 6, in csv_reader
    result = file.read().split("\n")
MemoryError
```
In this case, `open()` returns a generator object that you can lazily iterate through line by line. However, `file.read().split()` loads everything into memory at once, causing the **MemoryError**.

Before that happens, you’ll probably notice your computer slow to a crawl. You might even need to kill the program with a KeyboardInterrupt. So, how can you handle these huge data files? Take a look at a new definition of csv_reader():
```
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```
In this version, you open the file, iterate through it, and yield a row. This code should produce the following output, with no memory errors. What’s happening here? Well, you’ve essentially **turned csv_reader() into a generator function**. This version opens a file, loops through each line, and yields each row, instead of returning it.

You can also define a generator expression (also called a generator comprehension), which has a very similar syntax to list comprehensions. In this way, you can use the generator without calling a function:
```
csv_gen = (row for row in open(file_name))
```
This is a more succinct way to create the list csv_gen. You’ll learn more about the Python yield statement soon. For now, just remember this key difference:
* Using yield will result in a generator object.
* Using return will result in the first line of the file only.

## Example 2: Generating an Infinite Sequence
Let’s switch gears and look at infinite sequence generation. In Python, to get a finite sequence, you call range() and evaluate it in a list context:
```
a = range(5)
list(a)
[0, 1, 2, 3, 4]
```
Generating an infinite sequence, however, will require the use of a generator, since your computer memory is finite:
```
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```
This code block is short and sweet. First, you initialize the variable num and start an infinite loop. Then, you immediately yield num so that you can capture the initial state. This mimics the action of range(). After yield, you increment num by 1. If you try this with a for loop, then you’ll see that it really does seem infinite.

The program will continue to execute until you stop it manually. Instead of using a for loop, you can also call `next()` on the generator object directly. This is especially useful for testing a generator in the console.

### Example 3: Detecting Palindromes
You can use infinite sequences in many ways, but one practical use for them is in building palindrome detectors. A palindrome detector will locate all sequences of letters or numbers that are palindromes. These are words or numbers that are read the same forward and backward, like 121. First, define your numeric palindrome detector. Check code of file `detect_palindromes`

Don’t worry too much about understanding the underlying math in this code. Just note that the function takes an input number, reverses it, and checks to see if the reversed number is the same as the original.

Now that you’ve seen a simple use case for an infinite sequence generator, let’s dive deeper into how generators work.

### Understanding Generators
So far, you’ve learned about the two primary ways of creating generators: by using generator functions and generator expressions. You might even have an intuitive understanding of how generators work. Let’s take a moment to make that knowledge a little more explicit.

Generator functions look and act just like regular functions, but with one defining characteristic. Generator functions use the Python yield keyword instead of return.

This looks like a typical function definition, except for the Python yield statement and the code that follows it. **yield indicates where a value is sent back to the caller**, but unlike return, you don’t exit the function afterward.

Instead, the **state of the function is remembered**. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again. Since generator functions look like other functions and act very similarly to them, you can assume that generator expressions are very similar to other comprehensions available in Python.

#### Building Generators With Generator Expressions
Like list comprehensions, generator expressions allow you to quickly create a generator object in just a few lines of code. They’re also useful in the same cases where list comprehensions are used, with an added benefit: you can create them without building and holding the entire object in memory before iteration. In other words, you’ll have no memory penalty when you use generator expressions. Take this example of squaring some numbers:
```
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))
```
ums_squared_lc and nums_squared_gc look basically the same, but there’s one key difference. Can you spot it? Take a look at what happens when you inspect each of these objects:
```
>>> nums_squared_lc
[0, 1, 4, 9, 16]
>>> nums_squared_gc
<generator object <genexpr> at 0x107fbbc78>
```
The first object used brackets to build a list, while the second created a generator expression by using parentheses. The output confirms that you’ve created a generator object and that it is distinct from a list.

#### Profiling Generator Performance
You learned earlier that generators are a great way to optimize memory. While an infinite sequence generator is an extreme example of this optimization, let’s amp up the number squaring examples you just saw and inspect the size of the resulting objects. **You can do this with a call to sys.getsizeof()**:
```
import sys
nums_squared_lc = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)
87624
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
120
```
In this case, the list you get from the list comprehension is 87,624 bytes, while the generator object is only 120. This means that the list is over 700 times larger than the generator object!

There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory, then **list comprehensions can be faster to evaluate than the equivalent generator expression**. If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.

#### Understanding the Python Yield Statement
On the whole, yield is a fairly simple statement. Its primary job is to control the flow of a generator function in a way that’s similar to return statements. As briefly mentioned above, though, the Python yield statement has a few tricks up its sleeve.

When you call a generator function or use a generator expression, you return a special iterator called a generator. You can assign this generator to a variable in order to use it. When you call special methods on the generator, such as next(), the code within the function is executed up to yield.

When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. (In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.

This allows you to resume function execution whenever you call one of the generator’s methods. In this way, all function evaluation picks back up right after yield. You can see this in action by using multiple Python yield statements:
```
>>> def multi_yield():
...     yield_str = "This will print the first string"
...     yield yield_str
...     yield_str = "This will print the second string"
...     yield yield_str
...
>>> multi_obj = multi_yield()
>>> print(next(multi_obj))
This will print the first string
>>> print(next(multi_obj))
This will print the second string
```
yield can be used in many ways to control your generator’s execution flow. The use of multiple Python yield statements can be leveraged as far as your creativity allows.

### Using Advanced Generator Methods
You’ve seen the most common uses and constructions of generators, but there are a few more tricks to cover. In addition to yield, generator objects can make use of the following methods:
* .send()
* .throw()
* .close()

#### How to Use .send()
For this next section, you’re going to build a program that makes use of all three methods. This program will print numeric palindromes like before, but with a few tweaks. Upon encountering a palindrome, your new program will add a digit and start a search for the next one from there. You’ll also handle exceptions with `.throw()` and stop the generator after a given amount of digits with `.close()`. We will use the same `is_palindrome` function of your palindrome detector.  You’ll also need to modify your original infinite sequence generator, like so:
```
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1
```
There are a lot of changes here! The first one you’ll see is in line 5, where i = (yield num). Though you learned earlier that yield is a statement, that isn’t quite the whole story.

As of Python 2.5 (the same release that introduced the methods you are learning about now), yield is an **expression**, rather than a statement. Of course, you can still use it as a statement. But now, you can also use it as you see in the code block above, where i takes the value that is yielded. This allows you to manipulate the yielded value. More importantly, it allows you to **.send() a value back to the generator**. When execution picks up after yield, i will take the value that is sent.

You’ll also check if i is not None, which could happen if next() is called on the generator object. (This can also happen when you iterate with a for loop.) If i has a value, then you update num with the new value. But regardless of whether or not i holds a value, you’ll then increment num and start the loop again.

Now, take a look at the main function code, which sends the lowest number with another digit back to the generator. For example, if the palindrome is 121, then it will .send() 1000:
```
pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
```
With this code, you create the generator object and iterate through it. The program only yields a value once a palindrome is found. It uses len() to determine the number of digits in that palindrome. Then, it sends 10 ** digits to the generator. This brings execution back into the generator logic and assigns 10 ** digits to i. Since i now has a value, the program updates num, increments, and checks for palindromes again.

Once your code finds and yields another palindrome, you’ll iterate via the for loop. This is the same as iterating with next(). The generator also picks up at line 5 with i = (yield num). However, now i is None, because you didn’t explicitly send a value.

What you’ve created here is a coroutine, or a generator function into which you can pass data. These are useful for constructing data pipelines, but as you’ll see soon, they aren’t necessary for building them. (If you’re looking to dive deeper, then [this course on coroutines and concurrency](http://www.dabeaz.com/coroutines/) is one of the most comprehensive treatments available.)

#### How to Use .throw()
.throw() allows you to throw exceptions with the generator. In the below example, you raise the exception in line 6. This code will throw a ValueError once digits reaches 5:
```
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
```

This is the same as the previous code, but now you’ll check if digits is equal to 5. If so, then you’ll .throw() a ValueError. To confirm that this works as expected, take a look at the code’s output:
```
11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 47, in <module>
    main()
  File "advanced_gen.py", line 41, in main
    pal_gen.throw(ValueError("We don't like large palindromes"))
  File "advanced_gen.py", line 26, in infinite_palindromes
    i = (yield num)
ValueError: We don't like large palindromes
```
`.throw()` is useful in any areas where you might need to catch an exception. In this example, you used `.throw()` to control when you stopped iterating through the generator. You can do this more elegantly with `.close()`.

#### How to Use .close()
As its name implies, .close() allows you to stop a generator. This can be especially handy when controlling an infinite sequence generator. Let’s update the code above by changing .throw() to .close() to stop the iteration:
```
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
```
Instead of calling .throw(), you use .close() in line 6. The advantage of using .close() is that it raises StopIteration, an exception used to signal the end of a finite iterator:
```
11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 46, in <module>
    main()
  File "advanced_gen.py", line 42, in main
    pal_gen.send(10 ** (digits))
StopIteration
```
### Conclusion
In this tutorial, you’ve learned about generator functions and generator expressions.