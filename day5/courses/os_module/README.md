## OS Module - User Underlying Operating System Functionality
The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.

### Handling the Current Working Directory

#### Getting the Current working directory
Consider **Current Working Directory(CWD)** as a folder, where the Python is operating. Whenever the files are called only by their name, Python assumes that it starts in the CWD which means that name-only reference will be successful only if the file is in the Python’s CWD.

To get the location of the current working directory `os.getcwd()` is used.
Example: Check the python file `os_module_cwd.py`

#### Changing the Current working directory
To change the current working directory(CWD) os.chdir() method is used. This method changes the CWD to a specified path. It only takes a single argument as a new directory path.

Note: The current working directory is the folder in which the Python script is operating.
Example: Check the python file `os_module_cwd.py`

### Creating a Directory
There are different methods available in the OS module for creating a director. These are:
* `os.mkdir()`
* `os.makedirs()` 

#### Using os.mkdir()
`os.mkdir()` method in Python is used to create a directory named path with the specified numeric mode. This method raises FileExistsError if the directory to be created already exists.
Example: Check the python file `os_module_cwd.py`

#### Using os.makedirs()
`os.makedirs()` method in Python is used to create a directory recursively. That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.
This is the **most used and recommended method** to create directories with OS module.
Example: Check the python file `os_module_cwd.py`

### Listing out Files and Directories with Python
`os.listdir()` method in Python is used to get the list of all files and directories in the specified directory. If we don’t specify any directory, then the list of files and directories in the current working directory will be returned.
Example: Check the python file `os_module_ls.py`

### Deleting Directory or Files using Python
OS module proves different methods for removing directories and files in Python. These are:
* Using `os.remove()`
* Using `os.rmdir()`
* Using `os.removedirs()`

#### Using os.remove()
`os.remove()` method in Python is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by the method.
Example: Check the python file `os_module_rm.py`

#### Using os.rmdir()
`os.rmdir()` method in Python is used to remove or delete an empty directory. OSError will be raised if the specified path is not an empty directory. This is the recommended method to delete folders.
Example: Check the python file `os_module_rm.py`

#### Using os.removedirs()
Remove directories recursively. Works like `rmdir()` except that, if the leaf directory is successfully removed, `removedirs()` tries to successively remove every parent directory mentioned in path until an error is raised. This command is a little more dangerous than creating directories recursively using `os.makedirs()`. So usually, when you're going to delete folders, mostly you will use `os.rmdir()` so taht you can specifically delete the exact directory that you want to remove.
Example: Check the python file `os_module_rm.py`

### Renaming a file or a folder
` os.rename()`: A file old.txt can be renamed to new.txt, using the function os.rename(). The name of the file changes only if, the file exists and the user has sufficient privilege permission to change the file.
Example: Check the python file `os_module_rm.py`

### Traverse file system with os.walk
OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
* **dirpath** : the path to the directory
* **dirnames** : a list of the names of the subdirectories in dirpath.
* **filenames** :  a list of the names of the non-directory files in dirpath.
Example: Check the python file `os_module_bonus.py`

### Getting user’s environmental variables with os.environ
`os.environ` in Python is a mapping object that represents the user’s environmental variables. It returns a dictionary having user’s environmental variable as key and their values as value.

os.environ behaves like a python dictionary, so all the common dictionary operations like get and set can be performed. We can also modify os.environ but any changes will be effective only for the current process where it was assigned and it will not change the value permanently.

### OS.path methods
* **os.path.basename()** : returns the final component of a pathname (even fake path)
* **os.path.dirname()** : returns the directory component of a pathname (even fake path)
* **os.path.split()** : splits a pathname. returns tuple "(head, tail)" where "tail" is everything after the final slash (either part may be empty)
* **os.path.exists()** : tests whether a path exists. returns False for broken symbolic links
* **os.path.isdir()** : checks if the path is a directory
* **os.path.isfile()** : checks if the path is a file
* **os.path.splitext()** : splits the extension from a pathname. Extension is everything from the last dot to the end, ignoring leading dots. Returns 2-tuple "(root, ext)" (ext may be empty)




    


