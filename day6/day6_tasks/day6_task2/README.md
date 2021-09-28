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
