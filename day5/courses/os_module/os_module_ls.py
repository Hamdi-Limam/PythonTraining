# Python program to explain os.listdir() method
import os
 
# Get the list of all files and directories in the CWD
dir_list = os.listdir()
 
print(f"Files and directories in CWD:\n{dir_list}")

# Get the list of all files and directories in the root directory
path = "/"
dir_list = os.listdir(path)
 
print(f"Files and directories in CWD:\n{dir_list}")