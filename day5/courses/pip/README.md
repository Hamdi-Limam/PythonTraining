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
### Fine-Tuning Requirements
The problem with hardcoding the versions of your packages and their dependencies is that packages are updated frequently with bug and security fixes, and you probably want to leverage those as soon as they are published.

The requirements file format allows you to specify dependency versions using logical operators that give you a bit of flexibility to insure packages are updated, but still define the base versions of a package.

Open the requirements.txt file in your favorite editor and make the following changes:
```
certifi>=2018.11.29
chardet>=3.0.4
idna>=2.8
requests>=2.21.0, <3.0
urllib3>=1.24.1
```
You can change the logical operator to >= to tell pip to install an exact or greater version that has been published. When you set a new environment using the requirments.txt file, pip looks for the latest version that satisfies the requirement and installs it.

In an ideal world, new versions of packages would be backwards compatible and would never introduce new bugs. Unfortunately, **new versions can introduce changes that will break your application**. The requirements file syntax supports additional [version specifiers](https://www.python.org/dev/peps/pep-0440/#version-specifiers) to fine-tune your requirements.

Changing the version specifier for the requests package ensures that any version greater or equal to 3.0 does not get installed. The pip documentation provides all the information about the [requirements file format](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format), and you can consult it to learn more about it.

### Production vs Development Dependencies
Not all packages that you install during the development of your applications are going to be application dependencies. There are many packages published to PyPI that are development tools or libraries that you want to leverage during the development process.

As an example, you’ll probably want to unit test your application, so you need a unit test framework. A popular framework for unit testing is pytest. You want to install it in your development environment, but you do not want it in your production environment because it isn’t an application dependency.

You can create a second requirements file (requirements_dev.txt) to list additional tools to set up a development environment. This requires you to use pip to install both requirement files: requirements.txt and requirements_dev.txt. Fortunately, pip allows you to specify additional parameters within a requirements file. You can modify requirements_dev.txt to also install the requirements from the production requirements.txt file:
```
# In requirements_dev.txt
-r requirements.txt
pytest>=4.2.0
``` 

### Freezing Requirements for Production
You created the production and development requirement files and added them to source control. The files use flexible version specifiers to ensure that you leverage bug fixes published by your dependencies. You are also testing your application and are ready to deploy it to production.

You probably want to ensure that the versions of the dependencies you deploy to production are the exact same versions you used in your integration pipeline or build process because you know all the tests pass and the application works.

The current version specifiers don’t guarantee that the same versions will be deployed to production, so you want to freeze the production requirements as you saw earlier.

You create a clean production virtual environment and install the production requirements using the `requirements.txt` file. Once the requirements are installed, you can freeze the specific versions, dumping the output to a `requirements_lock.txt` file that you use in production. The `requirements_lock.txt` file will contain exact versions specifiers and can be used to replicate the environment.

### Finding Packages to Use
As you become a more experienced Pythonista, there’ll be a set of packages that you’ll know by heart and that you’ll use in most of your applications. The requests and pytest packages are good candidates to become useful tools in your Python toolbox.

There will be times though when you will need to solve a different problem, and you will want to look for a different tool or library that can help you with it. As you can see above, pip help shows that there is a `search` command that looks for packages published to PyPI.

The command takes a set of options listed above and a `<query>`. The query is just a string to search for and will match packages and their descriptions.

Most of the time, you want to search for packages directly in the [PyPI](https://pypi.org/) website. PyPI provides search capabilities for its index and a way to filter results by the metadata exposed in the package, like framework, topic, development status, and so on.

Another option to find a package is to Google it. Widely used Python libraries will show up at the top of google searches, and you should be able to find a link to the package in PyPI or its source code repository.

### Uninstalling Packages
Once in a while, you will have to uninstall a package. You either found a better library to replace it, or it is something you don’t really need. Uninstalling packages can be a bit tricky.

Notice that, when you installed `requests`, `pip` installed other dependencies too. The more packages you install, the bigger the chances that multiple packages depend on the same dependency. This is where the `show` command in pip comes in handy.

Before you uninstall a package, make sure you run the `show` command for that package. Notice the last two fields `Requires` and `Required-by`. The `show` command tells us that requests requires `urllib3, certifi, chardet, and idna`. You probably want to uninstall those two. You can also see that requests is not required by any other package, so it is **safe to uninstall it**.

You should run the `show` command against all of the requests dependencies to make sure that no other libraries also depend on them. Once you understand the dependency order of the packages you want to uninstall, you can remove them using the `uninstall` command:
```
pip uninstall certifi
```
You can specify all the packages you want to uninstall in a single call: 
```
pip uninstall -y urllib3 chardet idna requests
```