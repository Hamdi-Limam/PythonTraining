## What Is Pip?
[pip](https://pip.pypa.io/en/stable/) is the standard package manager for Python. It allows you to install and manage additional libraries and dependencies that are not part of the [Python standard library](https://docs.python.org/3/py-modindex.html). This article is an introduction to pip for new Pythonistas.

**In this tutorial, you’ll learn about:**
* Installing additional packages not included with the standard Python distribution
* Finding packages published to the [Python Package Index (PyPI)](https://pypi.org/)
* Managing requirements for your scripts and applications
* Uninstalling packages and their dependencies

Package management is so important that pip has been included with the Python installer since versions 3.4 for Python 3 and 2.7.9 for Python 2, and it’s used by many Python projects, which makes it an essential tool for every Pythonista.

### Installing Packages with pip
Python is considered a batteries included language. This means that the Python standard library includes an extensive set of packages and modules to help developers with their scripts and applications.

At the same time, Python has a very active community that contributes an even bigger set of packages that can help you with your development needs. These packages are published to the [Python Package Index](https://pypi.org/), also known as PyPI. PyPI hosts an extensive collection of packages that include development frameworks, tools, and libraries.

Many of these packages simplify Python development by providing friendly interfaces to functionality that already exists in the standard library.

### Basic Package Installation
PyPI hosts a very popular library to perform HTTP [requests](https://pypi.org/project/requests/) called requests. You can learn all about it in its official [documentation site](http://docs.python-requests.org/en/master/).

The first step is to install the requests package into your environment. You can learn about pip supported commands by running it with help:
```
pip help
```
As you can see, pip provides an install command to install packages. You can run it to install the requests package:
```
pip install requests
```
You use pip with an install command followed by the name of the package you want to install. pip looks for the package in PyPI, calculates its dependencies, and installs them to ensure requests will work.

You can also see that the current environment is using pip version 18.1, but version 19.0.1 is available. It also shows the command you should use to update pip, so let’s do that:
```
python -m pip install --upgrade pip
```
Notice that you use python -m to update pip. The -m switch tells Python to run a module as an executable. This is necessary because in order for you to update pip, the old version has to be uninstalled before installing the new version, and removing it while running the tool can cause errors.

When you run pip as a module, Python loads the module in memory and allows the package to be removed while it is being used. You can run packages as if they were scripts if the package provides a [top-level script](https://docs.python.org/3/library/__main__.html) `__main__.py`.

Now that you have installed requests and upgraded pip, you can use the `list` command to see the packages installed in your environment:
```
pip list
```
The pip install <package> command always looks for the latest version of the package and installs it. It also searches for dependencies listed in the package metadata and installs those dependencies to insure that the package has all the requirements it needs.

As you can see, multiple packages were installed. You can look at the package metadata by using the `show` command in pip:
```
pip show requests
```
You can import the requests package as any other standard package because it is now installed in your environment.

### Using Requirement Files
The pip install command always installs the latest published version of a package, but sometimes, you may want to install a specific version that you know works with your code.

You want to create a specification of the dependencies and versions you used to develop and test your application, so there are no surprises when you use the application in production.

Requirement files allow you to specify exactly which packages and versions should be installed. Running pip help shows that there is a `freeze` command that outputs the installed packages in requirements format. You can use this command, redirecting the output to a file to generate a requirements file:
```
pip freeze > requirements.txt
cat requirements.txt

certifi==2018.11.29
chardet==3.0.4
idna==2.8
requests==2.21.0
urllib3==1.24.1
```
The `freeze` command dumps all the packages and their versions to standard output, so you can redirect the output to a file that can be used to install the exact requirements into another system. The convention is to name this file `requirements.txt`, but you can give it any name you want.

When you want to replicate the environment in another system, you can run pip install specifying the requirements file using the -r switch:
```
pip install -r requirements.txt
```