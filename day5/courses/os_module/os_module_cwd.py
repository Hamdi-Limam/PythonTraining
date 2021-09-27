# OS Module - Handling the Current Working Directory
import os
     
# Function to Get the current working directory
def current_path(text):
    print(f"Current working directory {text}")
    print(os.getcwd())
    print()

# Printing CWD before
current_path("before")
   
# Changing the CWD
os.chdir('day5/courses/os_module/')
   
# Printing CWD after
current_path("after")


# Directories
directory_mkdir = "LetUsDevOps"
directory_makedirs = "PythonTraining"

# Path
path_mkdir = os.path.join(os.getcwd(), directory_mkdir)
path_makedirs = os.path.join("parentDir/", directory_makedirs)


# Create the directory 'LetUsDevOps' in the CWD
os.mkdir(path_mkdir)
print(f"Directory {directory_mkdir} created")

# Create the directory 'PythonTraining' in the CWD/parentDir
os.makedirs(path_makedirs)
print(f"Directory {directory_makedirs} created")