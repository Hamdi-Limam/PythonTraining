## Python Click package
Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

Click in three points:
* arbitrary nesting of commands
* automatic help page generation
* supports lazy loading of subcommands at runtime

### How to use Click package
You can get the library directly from PyPI:
```
pip install click
```
The installation into a [virtualenv](https://click.palletsprojects.com/en/8.0.x/quickstart/#virtualenv) is **heavily recommended**.

Virtualenv is probably what you want to use for developing Click applications. Virtualenv enables multiple side-by-side installations of Python, one for each project. It doesn’t actually install separate copies of Python, but it does provide a clever way to keep different project environments isolated.

### Basic Concepts - Creating a Command
Click is based on declaring commands through decorators. Internally, there is a non-decorator interface for advanced use cases, but it’s discouraged for high-level usage.
A function becomes a Click command line tool by decorating it through `click.command()`. At its simplest, just decorating a function with this decorator will make it into a callable script:
```
import click

@click.command()
def hello():
    click.echo('Hello World!')
```
What’s happening is that the decorator converts the function into a **Command** which then can be invoked:
```
if __name__ == '__main__':
    hello()
```
### Echoing
Why does this example use **echo()** instead of the regular **print()**function? The answer to this question is that Click attempts to support different environments consistently and to be very robust even when the environment is misconfigured. Click wants to be functional at least on a basic level even if everything is completely broken.

What this means is that the **echo()** function applies some error correction in case the terminal is misconfigured instead of dying with an **UnicodeError**.

The echo function also supports color and other styles in output. It will automatically remove styles if the output stream is a file. On Windows, colorama is automatically installed and used. See [ANSI Colors](https://click.palletsprojects.com/en/8.0.x/utils/#ansi-colors).

If you don’t need this, you can also use the print() construct / function.

### Nesting Commands
Commands can be attached to other commands of type Group. This allows arbitrary nesting of scripts. As an example here is a script that implements two commands for managing databases:
```
@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
```
As you can see, the` group()` decorator works like the `command()` decorator, but creates a **Group object** instead which can be given multiple subcommands that can be attached with `Group.add_command()`.

For simple scripts, it’s also possible to automatically attach and create a command by using the Group.command() decorator instead. The above script can instead be written like this:
```
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')
```
You would then invoke the Group in your setuptools entry points or other invocations:
```
if __name__ == '__main__':
    cli()
```

### Registering Commands Later
Instead of using the @group.command() decorator, commands can be decorated with the plain @click.command() decorator and registered with a group later with group.add_command(). This could be used to split commands into multiple Python modules.
```
@click.command()
def greet():
    click.echo("Hello, World!")
```
```
@click.group()
def group():
    pass

group.add_command(greet)
```
### Parameters
Click supports two types of parameters for scripts: `options and arguments`. There is generally some confusion among authors of command line scripts of when to use which, so here is a quick overview of the differences. As its name indicates, an option is optional. While arguments can be optional within reason, they are much more restricted in how optional they can be.

To help you decide between options and arguments, the recommendation is to use **arguments exclusively for things like going to subcommands or input filenames / URLs**, and have everything else be an option instead.

#### Differences
Arguments can do less than options. The following features are only available for options:
* automatic prompting for missing input
* act as flags (boolean or otherwise)
* option values can be pulled from environment variables, arguments can not
* options are fully documented in the help page, arguments are not (this is intentional as arguments might be too specific to be automatically documented)

#### Parameter Types
Parameters can be of different types. Types can be implemented with different behavior and some are supported out of the box:

* str / click.STRING: The default parameter type which indicates unicode strings.
* int / click.INT: A parameter that only accepts integers.
* float / click.FLOAT: A parameter that only accepts floating point values.
* bool / click.BOOL: A parameter that accepts boolean values. This is automatically used for boolean flags. The string values “1”, “true”, “t”, “yes”, “y”, and “on” convert to **True**. “0”, “false”, “f”, “no”, “n”, and “off” convert to **False**.
* click.UUID: A parameter that accepts UUID values. This is not automatically guessed but represented as uuid.UUID.
* class click.File(mode='r', encoding=None, errors='strict', lazy=None, atomic=False): Declares a parameter to be a file for reading or writing. The file is automatically closed once the context tears down.
* class click.Path(exists=False, file_okay=True, dir_okay=True, writable=False, readable=True, resolve_path=False, allow_dash=False, path_type=None): The path type is similar to the File type but it performs different checks. First of all, instead of returning an open file handle it returns just the filename. Secondly, it can perform various basic checks about what the file or directory should be.
* class click.Choice(choices, case_sensitive=True): The choice type allows a value to be checked against a fixed set of supported values. All of these values have to be strings.
* class click.IntRange(min=None, max=None, min_open=False, max_open=False, clamp=False): Restrict an click.INT value to a range of accepted values.
* class click.FloatRange(min=None, max=None, min_open=False, max_open=False, clamp=False): Restrict a click.FLOAT value to a range of accepted values.
* class click.DateTime(formats=None): The DateTime type converts date strings into datetime objects.^

#### Implementing Custom Types
To implement a custom type, you need to subclass the ParamType class. Override the convert() method to convert the value from a string to the correct type.

The following code implements an integer type that accepts hex and octal numbers in addition to normal integers, and converts them into regular integers.
```
import click

class BasedIntParamType(click.ParamType):
    name = "integer"

    def convert(self, value, param, ctx):
        if isinstance(value, int):
            return value

        try:
            if value[:2].lower() == "0x":
                return int(value[2:], 16)
            elif value[:1] == "0":
                return int(value, 8)
            return int(value, 10)
        except ValueError:
            self.fail(f"{value!r} is not a valid integer", param, ctx)

BASED_INT = BasedIntParamType()
```
To add parameters, use the option() and argument() decorators:
```
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")
```
What it looks like:
```
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit.
```
### Switching to Setuptools
In the code you wrote so far there is a block at the end of the file which looks like this: if __name__ == '__main__':. This is traditionally how a standalone Python file looks like. With Click you can continue doing that, but there are better ways through setuptools.

When writing command line utilities, it’s recommended to write them as modules that are distributed with `setuptools` instead of using Unix shebangs. Why would you want to do that? There are a bunch of reasons:

1. One of the problems with the traditional approach is that the first module the Python interpreter loads has an incorrect name. This might sound like a small issue but it has quite significant implications.
The first module is not called by its actual name, but the interpreter renames it to __main__. While that is a perfectly valid name it means that if another piece of code wants to import from that module it will trigger the import a second time under its real name and all of a sudden your code is imported twice.
2. Not on all platforms are things that easy to execute. On Linux and OS X you can add a comment to the beginning of the file (#!/usr/bin/env python) and your script works like an executable (assuming it has the executable bit set). This however does not work on Windows. While on Windows you can associate interpreters with file extensions (like having everything ending in .py execute through the Python interpreter) you will then run into issues if you want to use the script in a virtualenv.
3. The main trick only works if the script is a Python module. If your application grows too large and you want to start using a package you will run into issues.

#### Working with setuptools
To bundle your script with setuptools, all you need is the script in a Python package and a setup.py file.

Imagine this directory structure:
```
yourscript.py
setup.py
```
Contents of yourscript.py:
```
import click

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')
```
Contents of setup.py:
```
from setuptools import setup

setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourscript:cli',
        ],
    },
)
```
The magic is in the `entry_points` parameter. Below `console_scripts`, each line identifies one console script. The first part before the equals sign (=) is the name of the script that should be generated, the second part is the import path followed by a colon (:) with the Click command. That’s it.

#### Testing The Script
To test the script, you can make a new virtualenv and then install your package:
```
virtualenv venv
. venv/bin/activate
pip install --editable .
```
Afterwards, your command should be available:
```
$ yourscript
Hello World!
```
#### Scripts in Packages
If your script is growing and you want to switch over to your script being contained in a Python package the changes necessary are minimal. Let’s assume your directory structure changed to this:
```
project/
    yourpackage/
        __init__.py
        main.py
        utils.py
        scripts/
            __init__.py
            yourscript.py
    setup.py
```
In this case instead of using py_modules in your setup.py file you can use packages and the automatic package finding support of setuptools. In addition to that it’s also recommended to include other package data.

These would be the modified contents of setup.py:
```
from setuptools import setup, find_packages

setup(
    name='yourpackage',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourpackage.scripts.yourscript:cli',
        ],
    },
)
```
