# Python program to explain os.remove() and os.rmdir() method
import os
     
# File name
file = 'file1.txt'



# File location
location = os.path.join(os.getcwd(), "day5/courses/os_module/")
os.chdir(location)

# Renaming the file filee1.txt to file1.txt
os.rename("filee1.txt", "file1.txt")

# # Path
# path = os.path.join(os.getcwd(), file)
     
# # Remove the file 'file1.txt'
# os.remove(path)

# print(f"File {file} deleted")

# # Directories name
# directory_rmdir = "LetUsDevOps"
# directory_removemdirs = "parentDir"

# # Path
# path_rmdir = os.path.join(os.getcwd(), directory_rmdir)

# # Remove the Directory "LetUsDevOps" using rmdir()
# os.rmdir(path_rmdir)
# print(f"Directory {directory_rmdir} deleted")
