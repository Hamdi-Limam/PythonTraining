## Pep8 Formatting
PEP 8,  is a document that provides guidelines and best practices on how to write Python code. The primary focus of PEP 8 is **to improve the readability and consistency** of Python code.

PEP stands for `Python Enhancement Proposal`, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

### Why We Need PEP 8
As Guido van Rossum said, “Code is read much more often than it is written.” You may spend a few minutes, or a whole day, writing a piece of code to process user authentication. Once you’ve written it, you’re never going to write it again. But you’ll definitely have to read it again. That piece of code might remain part of a project you’re working on. Every time you go back to that file, you’ll have to remember what that code does and why you wrote it, so readability matters.

If you’re new to Python, it can be difficult to remember what a piece of code does a few days, or weeks, after you wrote it. If you follow PEP 8, you can be sure that you’ve **named your variables well**. You’ll know that you’ve** added enough whitespace** so it’s easier to follow logical steps in your code. You’ll also have **commented your code well**. All this will mean your code is more readable and easier to come back to. As a beginner, following the rules of PEP 8 can make learning Python a much more pleasant task.

### Naming Conventions
When you write Python code, you have to name a lot of things: variables, functions, classes, packages, and so on. Choosing sensible names will save you time and energy later. You’ll be able to figure out, from the name, what a certain variable, function, or class represents. You’ll also avoid using inappropriate names that might result in errors that are difficult to debug.

#### Naming Styles
* **Function**: Use a lowercase word or words. Separate words by underscores to improve readability. Example: `function, my_function`
* **Variable**: Use a lowercase single letter, word, or words. Separate words with underscores to improve readability. Example: `x, var, my_variable`
* **Class**: Start each word with a capital letter. Do not separate words with underscores. This style is called camel case. Example: `Model, MyClass` 
* **Method**: 	Use a lowercase word or words. Separate words with underscores to improve readability. Example: `class_method, method` 
* **Variable**:Use an uppercase single letter, word, or words. Separate words with underscores to improve readability. Example: `CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT` 
* **Module**: Use a short, lowercase word or words. Separate words with underscores to improve readability. Example: `module.py, my_module.py`
* **Package**: Use a short, lowercase word or words. Do not separate words with underscores. Example: `package, mypackage`

##### How to Choose Names
Choosing names for your variables, functions, classes, and so forth can be challenging. You should put a fair amount of thought into your naming choices when writing code as it will make your code more readable. The best way to name your objects in Python is to use descriptive names to make it clear what the object represents.

When naming variables, you may be tempted to reduce the amount of typing you do, it can be tempting to use abbreviations when choosing names. In the example below, I have defined a function db() that takes a single argument x and doubles it:
```
# Not recommended
def db(x):
    return x * 2
```
At first glance, this could seem like a sensible choice. db() could easily be an abbreviation for double. But imagine coming back to this code in a few days. You may have forgotten what you were trying to achieve with this function, and that would make guessing how you abbreviated it difficult. The following example is much clearer. If you come back to this code a couple of days after writing it, you’ll still be able to read and understand the purpose of this function:
```
# Recommended
def multiply_by_two(x):
    return x * 2
```
### Code Layout
How you lay out your code has a huge role in how readable it is. In this section, you’ll learn how to add vertical whitespace to improve the readability of your code. You’ll also learn how to handle the 79 character line limit recommended in PEP 8.

#### Blank Lines
Vertical whitespace, or blank lines, can greatly improve the readability of your code. Code that’s bunched up together can be overwhelming and hard to read. Similarly, too many blank lines in your code makes it look very sparse, and the reader might need to scroll more than necessary. Below are three key guidelines on how to use vertical whitespace.

**Surround top-level functions and classes with two blank lines**. Top-level functions and classes should be fairly self-contained and handle separate functionality. It makes sense to put extra vertical space around them, so that it’s clear they are separate:
```
class MySecondClass:
    pass


def top_level_function():
    return None
```
**Surround method definitions inside classes with a single blank line**. Inside a class, functions are all related to one another. It’s good practice to leave only a single line between them:
```
class MyClass:
    def first_method(self):
        return None

    def second_method(self):
        return None
```
**Use blank lines sparingly inside functions to show clear steps**. Sometimes, a complicated function has to complete several steps before the return statement. To help the reader understand the logic inside the function, it can be helpful to leave a blank line between each step.
```
def calculate_variance(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2
```
#### Maximum Line Length and Line Breaking
PEP 8 suggests lines should be limited to 79 characters. This is because it allows you to have multiple files open next to one another, while also avoiding line wrapping.

Of course, keeping statements to 79 characters or less is not always possible. PEP 8 outlines ways to allow statements to run over several lines. Python will assume line continuation if code is contained within parentheses, brackets, or braces.

If line breaking needs to occur around binary operators, like + and *, it should occur before the operator. This rule stems from mathematics. Mathematicians agree that breaking before binary operators improves readability. 
```
# Not Recommended
total = (first_variable +
         second_variable -
         third_variable)

# Recommended
total = (first_variable
         + second_variable
         - third_variable)
```
#### Identation
Indentation, or leading whitespace, is extremely important in Python. The indentation level of lines of code in Python determines how statements are grouped together. Consider the following example:
```
x = 3
if x > 5:
    print('x is larger than 5')
```
The indented print statement lets Python know that it should only be executed if the if statement returns True. The same indentation applies to tell Python what code to execute when a function is called or what code belongs to a given class.

The key indentation rules laid out by PEP 8 are the following:
* Use 4 consecutive spaces to indicate indentation.
* Prefer spaces over tabs.

#### Tabs vs Spaces
As mentioned above, you should use spaces instead of tabs when indenting code. You can adjust the settings in your text editor to output 4 spaces instead of a tab character, when you press the Tab key.

Python 3 does not allow mixing of tabs and spaces. Therefore, if you are using Python 3, then these errors are issued automatically: `TabError: inconsistent use of tabs and spaces in indentation`.
 
You can write Python code with either tabs or spaces indicating indentation. But, if you’re using Python 3, you must be consistent with your choice. Otherwise, your code will not run. PEP 8 recommends that you always **use 4 consecutive spaces to indicate indentation**.

#### Indentation Following Line Breaks
When you’re using line continuations to keep lines to under 79 characters, it is useful to use indentation to improve readability. It allows the reader to distinguish between two lines of code and a single line of code that spans two lines. There are two styles of indentation you can use.

The first of these is to align the indented block with the opening delimiter:
```
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
```
Sometimes you can find that only 4 spaces are needed to align with the opening delimiter. This will often occur in if statements that span multiple lines as the if, space, and opening bracket make up 4 characters. In this case, it can be difficult to determine where the nested code block inside the if statement begins:
```
x = 5
if (x > 3 and
    x < 10):
    print(x)
```
In this case, PEP 8 provides two alternatives to help improve readability:
* Add a comment after the final condition. Due to syntax highlighting in most editors, this will separate the conditions from the nested code:
```
x = 5
if (x > 3 and
    x < 10):
    # Both conditions satisfied
    print(x)
```
* Add extra indentation on the line continuation:
```
x = 5
if (x > 3 and
        x < 10):
    print(x)
```
An alternative style of indentation following a line break is a hanging indent. This is a typographical term meaning that every line but the first in a paragraph or statement is indented. You can use a hanging indent to visually represent a continuation of a line of code. Here’s an example:
```
var = function(
    arg_one, arg_two,
    arg_three, arg_four)
```
Note: When using a hanging indent, there must not be any arguments on the first line and add extra indentation to distinguish the continued line from code contained inside the function.

Instead, it’s better to use a double indent on the line continuation. This helps you to distinguish between function arguments and the function body, improving readability:
```
def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one
```
#### Where to Put the Closing Brace
Line continuations allow you to break lines inside parentheses, brackets, or braces. It’s easy to forget about the closing brace, but it’s important to put it somewhere sensible. Otherwise, it can confuse the reader. PEP 8 provides two options for the position of the closing brace in implied line continuations:
* Line up the closing brace with the first non-whitespace character of the previous line
* Line up the closing brace with the first character of the line that starts the construct
```
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]

list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
```
You are free to chose which option you use. But, as always, consistency is key, so try to stick to one of the above methods.

### Comments
You should use comments to document code as it’s written. It is important to document your code so that you, and any collaborators, can understand it. When you or someone else reads a comment, they should be able to easily understand the code the comment applies to and how it fits in with the rest of your code. Here are some key points to remember when adding comments to your code:
1. Limit the line length of comments and docstrings to 72 characters.
2. Use complete sentences, starting with a capital letter.
3. Make sure to update comments if you change your code.

### Block Comments
Use block comments to document a small section of code. They are useful when you have to write several lines of code to perform a single action, such as importing data from a file or updating a database entry. They are important as they help others understand the purpose and functionality of a given code block. PEP 8 provides the following rules for writing block comments:
1. Indent block comments to the same level as the code they describe.
2. Start each line with a # followed by a single space.
3. Separate paragraphs by a line containing a single #.

Here is a block comment explaining the function of a for loop. Note that the sentence wraps to a new line to preserve the 79 character line limit:
```
for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n')
```
Sometimes, if the code is very technical, then it is necessary to use more than one paragraph in a block comment:
```
def quadratic(a, b, c, x):
    # Calculate the solution to a quadratic equation using the quadratic
    # formula.
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2.
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)
    return x_1, x_2
```
### Inline Comments
Inline comments explain a single statement in a piece of code. They are useful to remind you, or explain to others, why a certain line of code is necessary. Here’s what PEP 8 has to say about them:
1. Separate inline comments by two or more spaces from the statement.
2. Start inline comments with a # and a single space, like block comments.
3. Don’t use them to explain the obvious.
```
x = 5  # This is an inline comment
```
### Documentation Strings
Documentation strings, or docstrings, are strings enclosed in double (""") or single (''') quotation marks that appear on the first line of any function, class, method, or module. You can use them to explain and document a specific block of code. The most important rules applying to docstrings are the following:
1. Surround docstrings with three double quotes on either side, as in """This is a docstring""".
2. Write them for all public modules, functions, classes, and methods.
3. Put the """ that ends a multiline docstring on a line by itself:
```
def quadratic(a, b, c, x):
    """Solve quadratic equation via the quadratic formula.

    A quadratic equation has the following form:
    ax**2 + bx + c = 0

    There always two solutions to a quadratic equation: x_1 & x_2.
    """
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return x_1, x_2
```

### Whitespace Around Binary Operators
Surround the following binary operators with a single space on either side:
* Assignment operators (=, +=, -=, and so forth)
* Comparisons (==, !=, >, <. >=, <=) and (is, is not, in, not in)
* Booleans (and, not, or)

When there’s more than one operator in a statement, adding a single space before and after each operator can look confusing. Instead, it is better to only add whitespace around the operators with the lowest priority, especially when performing mathematical manipulation.

You can also apply this to if statements where there are multiple conditions:
```
# Not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')
```
In the above example, the and operator has lowest priority. It may therefore be clearer to express the if statement as below:
```
# Recommended
if x>5 and x%2==0:
    print('x is larger than 5 and divisible by 2!')
```
### When to Avoid Adding Whitespace
In some cases, adding whitespace can make code harder to read. Too much whitespace can make code overly sparse and difficult to follow. PEP 8 outlines very clear examples where whitespace is inappropriate.

The most important place to avoid adding whitespace is at the end of a line. This is known as trailing whitespace. It is invisible and can produce errors that are difficult to trace.

The following list outlines some cases where you should avoid adding whitespace:
* Immediately inside parentheses, brackets, or braces
* Before a comma, semicolon, or colon
* Before the open parenthesis that starts the argument list of a function call
* Before the open bracket that starts an index or slice
* Between a trailing comma and a closing parenthesis
* To align assignment operators

### Programming Recommendations
You will often find that there are several ways to perform a similar action in Python. In this section, you’ll see some of the suggestions PEP 8 provides to remove that ambiguity and preserve consistency.

**Don’t compare Boolean values to True or False using the equivalence operator**. You’ll often need to check if a Boolean value is True or False. When doing so, it is intuitive to do this with a statement like the one below:
```
# Not recommended
my_bool = 6 > 5
if my_bool == True:
    return '6 is bigger than 5'
```
The use of the equivalence operator, ==, is unnecessary here. bool can only take values True or False. It is enough to write the following:
```
# Recommended
if my_bool:
    return '6 is bigger than 5'
```
**Use the fact that empty sequences are falsy in if statements**. If you want to check whether a list is empty, you might be tempted to check the length of the list. If the list is empty, it’s length is 0 which is equivalent to False when used in an if statement. Here’s an example:
```
# Not recommended
my_list = []
if not len(my_list):
    print('List is empty!')
```
However, in Python any empty list, string, or tuple is falsy. We can therefore come up with a simpler alternative to the above:
```
# Recommended
my_list = []
if not my_list:
    print('List is empty!')
```
**Use is not rather than not ... is in if statements**. If you are trying to check whether a variable has a defined value, there are two options. The first is to evaluate an if statement with x is not None, as in the example below:
```
# Recommended
if x is not None:
    return 'x exists!'
```
A second option would be to evaluate x is None and then have an if statement based on not the outcome:
```
# Not recommended
if not x is None:
    return 'x exists!'
```
**Don’t use if x: when you mean if x is not None:**. Sometimes, you may have a function with arguments that are None by default. A common mistake when checking if such an argument, arg, has been given a different value is to use the following:
```
# Not Recommended
if arg:
    # Do something with arg...
```
This code checks that arg is truthy. Instead, you want to check that arg is not None, so it would be better to use the following:
```
# Recommended
if arg is not None:
    # Do something with arg...
```
**Use .startswith() and .endswith() instead of slicing**. If you were trying to check if a string word was prefixed, or suffixed, with the word cat, it might seem sensible to use list slicing. However, list slicing is prone to error, and you have to hardcode the number of characters in the prefix or suffix. 

### Tips and Tricks to Help Ensure Your Code Follows PEP 8
There is a lot to remember to make sure your code is PEP 8 compliant. Luckily, there are tools that can help speed up this process. There are two classes of tools that you can use to enforce PEP 8 compliance: linters and autoformatters.

#### Linters
Linters are programs that analyze code and flag errors. They provide suggestions on how to fix the error. Linters are particularly useful when installed as extensions to your text editor, as they flag errors and stylistic problems while you write.
Best linters: 
* [pycodestyle](https://pypi.org/project/pycodestyle/)
* [flake8](https://pypi.org/project/flake8/)

#### Autoformatters
Autoformatters are programs that refactor your code to conform with PEP 8 automatically. Once such program is [black](https://pypi.org/project/black/), which autoformats code following most of the rules in PEP 8. One big difference is that it limits line length to 88 characters, rather than 79. However, you can overwrite this by adding a command line flag `--line-length=79`.