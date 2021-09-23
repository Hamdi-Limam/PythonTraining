## Python Virtual Environments

### Why the Need for Virtual Environments?
Python, like most other modern programming languages, has its own unique way of downloading, storing, and resolving packages (or modules). While this has its advantages, there were some interesting decisions made about package storage and resolution, which has lead to some problems—particularly with how and where packages are stored.

There are a few different locations where these packages can be installed on your system. For example, most system packages are stored in a child directory of the path stored in `sys.prefix`.

More relevant to the topic of this article, third party packages installed using easy_install or pip are typically placed in one of the directories pointed to by `site.getsitepackages`.

### Why do all of these little details matter?
It’s important to know this because, by default, every project on your system will use these same directories to store and retrieve **site packages** (third party libraries). At first glance, this may not seem like a big deal, and it isn’t really, for **system packages** (packages that are part of the standard Python library), but it does matter for **site packages**.

Consider the following scenario where you have two projects: ProjectA and ProjectB, both of which have a dependency on the same library, ProjectC. The problem becomes apparent when we start requiring different versions of ProjectC. Maybe ProjectA needs v1.0.0, while ProjectB requires the newer v2.0.0, for example.

This is a real problem for Python since it can’t differentiate between versions in the site-packages directory. So both v1.0.0 and v2.0.0 would reside in the same directory with the same name.

Since projects are stored according to just their name, there is no differentiation between versions. Thus, both projects, ProjectA and ProjectB, would be required to use the same version, which is unacceptable in many cases.

This is where virtual environments and the [virtualenv](https://virtualenv.readthedocs.org/en/latest/)/[venv](https://docs.python.org/3/library/venv.html) tools come into play…

### What Is a Virtual Environment?
At its core, the main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

In our little example above, we’d just need to create a separate virtual environment for both ProjectA and ProjectB, and we’d be good to go. Each environment, in turn, would be able to depend on whatever version of ProjectC they choose, independent of the other.

The great thing about this is that there are no limits to the number of environments you can have since they’re just directories containing a few scripts. Plus, they’re easily created using `the virtualenv or pyenv command line tools`.

### Using Virtual Environments
To get started, if you’re not using Python 3, you’ll want to install the `virtualenv` tool with `pip`. If you are using Python 3, then you should already have the `venv` module from the standard library installed.

Create a new virtual environment inside the directory:
> python3 -m venv env
The Python 3 venv approach has the benefit of forcing you to choose a specific version of the Python 3 interpreter that should be used to create the virtual environment. This avoids any confusion as to which Python installation the new environment is based on.

From Python 3.3 to 3.4, the recommended way to create a virtual environment was to use the `pyvenv` command-line tool that also comes included with your Python 3 installation by default. But on 3.6 and above, `python3 -m venv` is the way to go.

Here’s what each folder contains:
* bin: files that interact with the virtual environment
* include: C headers that compile the Python packages
* lib: a copy of the Python version along with a site-packages folder where each dependency is installed

Further, there are copies of, or [symlinks](https://en.wikipedia.org/wiki/Symbolic_link) to, a few different Python tools as well as to the Python executables themselves. These files are used to ensure that all Python code and commands are executed within the context of the current environment, which is how the isolation from the global environment is achieved. We’ll explain this in more detail in the next section.

More interesting are **the activate scripts** in the bin directory. These scripts are used to set up your shell to use the environment’s Python executable and its site-packages by default.

In order to use this environment’s packages/resources in isolation, you need to “activate” it. To do this, just run the following:
```
$ source env/bin/activate
(env) $
```
Notice how your prompt is now **prefixed with the name of your environment** (`env`, in our case). This is the indicator that env is currently active, which means the python executable will only use this environment’s packages and settings.

If we need to go back to the “system” context, we should executie `deactivate`:
```
(env) $ deactivate
$
```
Now your shell session is back to normal, and the python command refers to the global Python install. Remember to do this whenever you’re done using a specific virtual environment.

### How Does a Virtual Environment Work?
What exactly does it mean to “activate” an environment? Knowing what’s going on under the hood can be pretty important for a developer, especially when you need to understand execution environments, dependency resolution, and so on.

To explain how this works, let’s first check out the locations of the different python executables. With the environment “deactivated,” run the following:
```
$ which python
/usr/bin/python
```
Now, activate it and run the command again:
```
$ source env/bin/activate
(env) $ which python
/Users/michaelherman/python-virtual-environments/env/bin/python
```
After activating the environment, we’re now getting a different path for the python executable because, in an active environment, the $PATH environment variable is slightly modified.

In the latter example, our virtual environment’s bin directory is now at the beginning of the path. That means it’s the first directory searched when running an executable on the command line. Thus, the shell uses our virtual environment’s instance of Python instead of the system-wide version.

This raises the following questions:

What’s the difference between these two executables anyway?
How is the virtual environment’s Python executable able to use something other than the system’s site-packages?
This can be explained by how Python starts up and where it is located on the system. There actually isn’t any difference between these two Python executables. **It’s their directory locations that matter**.

When Python is starting up, it looks at the path of its binary. In a virtual environment, it is actually just a copy of, or symlink to, your system’s Python binary. It then sets the location of `sys.prefix and sys.exec_prefix` based on this location, omitting the bin portion of the path.

In our example, the binary is located at /Users/michaelherman/python-virtual-environments/env/bin, which means `sys.prefix` would be `/Users/michaelherman/python-virtual-environments/env`, and therefore the `site-packages` directory used would be `/Users/michaelherman/python-virtual-environments/env/lib/pythonX.X/site-packages`. Finally, this path is stored in the sys.path array, which contains all of the locations where a package can reside.

### Managing Virtual Environments With virtualenvwrapper
While virtual environments certainly solve some big problems with package management, they’re not perfect. After creating a few environments, you’ll start to see that they create some problems of their own, most of which revolve around managing the environments themselves. To help with this, the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) tool was created. It’s just some wrapper scripts around the main `virtualenv` tool.

A few of the more useful features of virtualenvwrapper are that it:
* Organizes all of your virtual environments in one location
* Provides methods to help you easily create, delete, and copy environments
* Provides a single command to switch between environments

While some of these features may seem small or insignificant, you’ll soon learn that they’re important tools to add to your workflow. To get started, you can download the wrapper with pip:
```
$ pip install virtualenvwrapper
```
Once it’s installed, we’ll need to activate its shell functions. We can do this by running source on the installed virtualenvwrapper.sh script. When you first install it with pip, the output of the installation will tell you the exact location of virtualenvwrapper.sh or you can use `which virtualenvwrapper.sh`.

Using that path, add the following three lines to your shell’s startup file. If you’re using the Bash shell, you would place these lines in either the ~/.bashrc file or the ~/.profile file. For other shells, like zsh, csh, or fish, you would need to use the startup files specific to that shell. All that matters is that these commands are executed when you log in or open a new shell and then reload the startup file with 
`source ~/.bashrc`.
```
export WORKON_HOME=$HOME/.virtualenvs   # Optional
export PROJECT_HOME=$HOME/projects      # Optional
source /usr/local/bin/virtualenvwrapper.sh
```
You’ll also now have the shell commands available to you to help you manage the environments. Here are just a few of the ones available:
`workon, deactivate, mkvirtualenv,cdvirtualenv, rmvirtualenv, etc...`.
For more info on commands, installation, and configuring virtualenvwrapper, check out the [documentation](http://virtualenvwrapper.readthedocs.org/en/latest/install.html).

Now, anytime you want to start a new project, you just have to do this:
```
$ mkvirtualenv my-new-project
(my-new-project) $
```
This will create and activate a new environment in the directory located at $WORKON_HOME, where all virtualenvwrapper environments are stored.
To stop using that environment, you just need to deactivate it like before:
```
(my-new-project) $ deactivate
$
```
If you have many environments to choose from, you can list them all with the workon function:
```
$ workon
my-new-project
my-django-project
web-scraper
```
Finally, here’s how to activate:
```
$ workon web-scraper
(web-scraper) $
```

### Conclusion
In this course, you learned about not only how Python dependencies are stored and resolved, but also how you can use different community tools to help get around various packaging and versioning problems.